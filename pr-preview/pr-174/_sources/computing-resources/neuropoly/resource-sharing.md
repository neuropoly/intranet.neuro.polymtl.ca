# Resource sharing and booking

There are two systems for resource sharing on GPU clusters: GPU sharing and CPU/memory sharing.
GPU sharing is managed through a calendar. CPU and memory are shared using resource quotas (and the calendar).

### GPU booking

Please allocate your GPUs on the [computer resource calendar](https://calendar.google.com/calendar?cid=NG1nNmJnZDlwdjU1dGhmOTQ4NnQybWlodDhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ).

```{warning}
**IMPORTANT:** If you don't have writing permission on this calendar please contact your supervisor; all NeuroPoly accounts should have access by default.
```

Use this format: u918374@rosenberg:gpu\[3\].

Note that the GPUs are numbered from 0, as you can see in `nvidia-smi`.

To train, run your scripts like this:

```text
u918374@rosenberg:~$ CUDA_VISIBLE_DEVICES="3" ./train.sh
```

You can book multiple GPUs just with commas: u918374@rosenberg:gpu\[2,3,5\]

and use them with

```text
u918374@rosenberg:~$ CUDA_VISIBLE_DEVICES="2,3,5" ./train.sh
```

### Running memory- and CPU-intensive tasks

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

**To run a heavy process**:
1. Book one or more GPU slots (See [GPU booking](#gpu-booking) above). For joplin, select a range of
  slots between 0 and 3, inclusive, representing ¼ of available CPUs each.
2. Use the `set_slot` utility script to assign your process to the appropriate slice:
```
set_slot <slot_number> [command] [args...]
```

- `<slot_number>` is 0, 1, 2, or 3, corresponding to the GPU you are using, e.g., `set_slot 0 ...` for GPU0.
  - If you've reserved more than one slot, you can specify an inclusive range, e.g., `set_slot 0-1 ...`
    for slots 0 and 1.
- `[command] [args...]` is the (optional) command as you would normally run it in the shell, e.g., `python model.py`.
- If you don't specify a command, you'll be placed in a bash login shell. Running `set_slot 0` is the equivalent of running `set_slot 0 bash -l`.

For example:
```
set_slot 2 CUDA_VISIBLE_DEVICES=2 python3 myscript.py
set_slot 0-3
```

#### Special considerations

- **Environment variables are not currently passed through** by `set_slot`. To run in a specific environment,
for example a venv, use `set_slot` to start a shell (e.g. `set_slot 0 bash`) and then work in that shell. (_NB: the shell will not persist unless you run it in `tmux` or `screen`_).

- **If you need `conda` inside `set_slot`**, run `set_slot` without specifying the command. This will place you
  inside a bash login shell, which will put the proper folder inside the `PATH` environment variable.

- **If you need to access duke inside `set_slot`**, run `set_slot` inside a shell (e.g., `set_slot 0`), then
  run `cifscreds add duke.neuro.polymtl.ca` in that shell. This will ensure that duke is still
  accessible when you detach or logout
  - [Github issue](https://github.com/neuropoly/computers/issues/996)

- **tmux/screen**: You must start your session before you use set_slot. `tmux` and `screen` manage their own child
processes, and will bypass our systemd slices and run in the limited user resource pool.
Do NOT do `set_slot 3 tmux new -s mysession`! **If you are using a shell AND tmux/screen** you
should do so in this order:
  1. `tmux` or `tmux new -s mysession`
  2. `set_slot 0`

- **set_slot does not know anything about GPUs**, so you still need to set the options with your tooling
to use the appropriate GPU, e.g., `CUDA_VISIBLE_DEVICES`

### set_slot FAQ
#### What happens if I forget to do this, and accidentally run my training without set_slot?

- Your training won't have enough resources to run properly
- Your individual user session may be borked
- Nobody else's sessions or work will be borked

#### What happens if I send my process to the wrong pool? (e.g. I did set_slot 1, when I meant set_slot 0)

- This won't affect which GPU will be used.
- BUT, you might end up competing for resources with someone else.
- Try not to do this, and ask for help if you realize that you have.

#### What resources are available to me for trainings?

Right now each GPU pool is limited to:

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
- `ml.slice/ml-1slot.slice/ml-1slot-0.slice` corresponds with a single slot invoked with `set_slot 0`.
- `ml.slice/ml-4slots.slice/ml-4slots-03.slice` corresponds to a groups of four slots invoked with `set_slot 0-3`.

To see which processes are running in which slots, you can use:
```
systemd-cgls /ml.slice
```

#### What resources are available to me for trainings?

Right now each GPU pool is limited to:
- romane: ~100GB of RAM and 14 CPUs
- tassan: ~46GB of RAM and 20 CPUs
