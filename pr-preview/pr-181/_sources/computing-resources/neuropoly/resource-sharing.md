# Resource sharing and booking

There are two systems for resource sharing on GPU clusters: GPU sharing and CPU/memory sharing.
GPU sharing is managed through a calendar. CPU and memory are shared using resource quotas (and the calendar).

## GPU and CPU booking

Please allocate your GPUs (for romane, rosenberg, and tassan) and CPU time (for joplin) on the [computer resource calendar](https://calendar.google.com/calendar?cid=NG1nNmJnZDlwdjU1dGhmOTQ4NnQybWlodDhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ).

```{warning}
**IMPORTANT:** If you don't have writing permission on this calendar please contact your supervisor; all NeuroPoly accounts should have access by default.
```

Use this format: your-name@rosenberg:gpu\[3\].

Note that the GPUs are numbered from 0, as you can see in `nvidia-smi`.

To train, run your scripts like this:

```text
your-name@rosenberg:~$ CUDA_VISIBLE_DEVICES="3" ./train.sh
```

You can book multiple GPUs just with commas: your-name@rosenberg:gpu\[2,3,5\]

and use them with

```text
your-name@rosenberg:~$ CUDA_VISIBLE_DEVICES="2,3,5" ./train.sh
```

## Running memory- and CPU-intensive tasks using `set_slot`

```{note}
At the moment, this section only applies to romane, tassan, and joplin.
```

<details>
<summary>Some context</summary>

In order to prevent unresponsive systems due to resource intensive ML processes, some clusters have strict
resource controls in place. Essentially, we impose limits on the amount of CPU and RAM available to a user
(i.e., a single core of the CPU and a few GB of RAM). Most regular commands (git, scp, etc) should
run fine under these limitations.

</details>

Most commands (git, scp, tmux, etc) should run just fine without modification.

For processes that need to use the full resources of the system, we have dedicated "slots" with
a share of the system's RAM and CPU.

### Method 1: Running inside a shell (recommended)

1. Make sure you've booked one or more GPU or CPU slots (See [booking](#gpu-and-cpu-booking) above). For joplin, select a range of
  slots between 0 and 3, inclusive, representing ¼ of available CPUs each.
2. Start your `tmux` or `screen` session:
```shell
$ tmux
```
3. Enter the slot(s). This will start a shell with the appropriate resources allocated:
```shell
$ set_slot <slot_number>
```

`<slot_number>` is 0, 1, 2, or 3, corresponding to the GPU you are using, e.g., `set_slot 0 ...` for GPU0.
If you've reserved more than one slot, you can specify an inclusive range, e.g., `set_slot 0-1 ...`
for slots 0 and 1.

4. **(Important)** Run any environment setup steps, like `conda activate` or `source .venv/bin/activate`. When you enter a slot, your environment is reset, so environment changes from your session _before_ `set_slot` will not persist.

### Method 2: Running a single command inside a slot

If you don't want or need an interactive shell, you can also run one-off commands inside a slot:

```shell
$ set_slot <slot_number> [command] [args...]
```

- `[command] [args...]` is the (optional) command as you would normally run it in the shell, e.g., `python model.py`.
- Note that environment variables will not be passed through to the command. If you need to modify the command environment,
  use Method 1 above.
- If you don't specify a command, you'll be placed in a bash login shell. Running `set_slot 0` is the equivalent of running `set_slot 0 bash -l`.

For example:
```
set_slot 2 CUDA_VISIBLE_DEVICES=2 python3 myscript.py
set_slot 0-3
```

### Special considerations

- **Environment variables are not currently passed through** by `set_slot`. To run in a specific environment,
for example a venv, use `set_slot` to start a shell (e.g. `set_slot 0 bash`) and then work in that shell. (_NB: the shell will not persist unless you run it in `tmux` or `screen`_).

- **If you need `conda` inside `set_slot`**, run `set_slot` without specifying the command. This will place you
  inside a bash login shell, which will put the proper folder inside the `PATH` environment variable.

- **If you need to access duke inside `set_slot`**, run `set_slot` inside a shell (e.g., `set_slot 0`), then
  run `cifscreds add duke.neuro.polymtl.ca` in that shell. This will ensure that duke is still
  accessible when you detach or logout
  - [Github issue](https://github.com/neuropoly/computers/issues/996)

- **tmux/screen**: You must start your session _before_ you use `set_slot`. `tmux` and `screen` manage their own child
processes, and will bypass our systemd slices and run in the limited user resource pool.
Do NOT do `set_slot 3 tmux new -s mysession`! **If you are using a shell AND tmux/screen** you
should do so in this order:
  1. `tmux` or `tmux new -s mysession`
  2. `set_slot 0`

- **set_slot does not know anything about GPUs**, so you still need to set the options with your tooling
to use the appropriate GPU, e.g., `CUDA_VISIBLE_DEVICES`

- **Using VSCode on servers with set_slot**: unfortunately, the VSCode server, especially when paired with automation
tools like Claude Code, tends to use up all available memory outside of your slot, making your user session unresponsive.
Running VSCode server inside a slot may interfere with resource availability for other users who have booked computing resources for trainings and analyses, so we typically advise against it.
Instead, we recommend running VSCode locally and copying files onto the server using tools like `scp`, `rsync`, etc.
If you want help setting this up, please reach out to a sysadmin.

### set_slot FAQ
#### What happens if I forget to do this, and accidentally run my training without set_slot?

- Your training won't have enough resources to run properly
- Your individual user session may be borked
- Nobody else's sessions or work will be borked

#### What happens if I send my process to the wrong pool? (e.g. I did set_slot 1, when I meant set_slot 0)

- This won't affect which GPU will be used.
- BUT, you might end up competing for resources with someone else.
- Try not to do this, and ask for help if you realize that you have.

#### How do I terminate `set_slot` once I am done with it?

You can either kill the `tmux` or `screen` session in which you launched your `set_slot` shell, or you can exit the shell directly with `exit`.

#### How do I know which slots are currently in use?

Run:
```
systemd-cgtop ml.slice
```

The output will look something like this:
```
CGroup                                                             Tasks   %CPU   Memory  Input/s Output/s
ml.slice                                                             340   99.8    43.0G        -        -
ml.slice/ml-4slots.slice                                             338   99.8    36.7G        -        -
ml.slice/ml-4slots.slice/ml-4slots-03.slice                          338   99.8    36.7G        -        -
ml.slice/ml-4slots.slice/ml-4slots-03.slice/run-u959.service         338   99.8    36.7G        -        -
ml.slice/ml-1slot.slice                                                2      -     6.2G        -        -
ml.slice/ml-1slot.slice/ml-1slot-0.slice                               2      -     6.2G        -        -
ml.slice/ml-1slot.slice/ml-1slot-0.slice/run-u803.service              2      -     6.2G        -        -
```

The numbers next to `ml.slice` show you the total resource usage for all slots combined.

Other lines correspond to classes of slots, particular slots, and process groups within slots. For example:
- `ml.slice/ml-1slot.slice/ml-1slot-0.slice` corresponds to a single slot invoked with `set_slot 0`.
- `ml.slice/ml-4slots.slice/ml-4slots-03.slice` corresponds to a groups of four slots invoked with `set_slot 0-3`.

To see which processes are running in which slots, you can use:
```
systemd-cgls /ml.slice
```

#### How can I tell if my shell is running in a slot?

If you typically use `set_slot` to run a bash login shell (the default behaviour), then you can add the following to your `~/.bashrc`:
```
# Detect if in slot and modify prompt
IN_SLOT=false
if [[ $(cat /proc/self/cgroup 2>/dev/null || true) == 0::/ml.slice* ]]; then
  IN_SLOT=true
fi
if [[ $IN_SLOT == true ]]; then
  PS1='\[\e[1;34m\][set_slot]\[\e[0m\] '"$PS1"
fi
```

(Right after you edit the file, you'll need to run `source ~/.bashrc` in your active session for this to take effect. Subsequent logins/sessions will load this automatically, so no need to run this command in the future.)

This will add a blue `[set_slot]` tag to the beginning of your command prompt when you are in a `set_slot` shell. You can also `echo $IN_SLOT`.

#### What resources are available to me for trainings?

Right now resource limitations for slots are as follows:

**romane:**
- ~91GB of RAM for a single slot
- 14 CPU cores for a single slot
- Up to 4 slots available (corresponding with 4 GPUs)

**tassan:**
- ~46GB of RAM for a single slot
- 20 CPU cores for a single slot
- Up to 2 slots available (corresponding with 2 GPUs)

**joplin:**
- ~46GB of RAM for a single slot
- 30 CPU cores for a single slot
- Up to 4 slots available (No GPUs)
