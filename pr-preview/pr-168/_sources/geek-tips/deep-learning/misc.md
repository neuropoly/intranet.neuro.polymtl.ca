# Misc

## Isolating GPUs \(without Docker\) <a id="isolating_gpus_without_docker"></a>

You can isolate the GPU that your software will be able to see using a NVIDIA environment called `CUDA_VISIBLE_DEVICES`, where you can select which GPUs will be visible to your software. Let's say you want to execute `my_script.py` and you want only the GPU 0 \(zero\) to be visible for your process:

```text
  CUDA_VISIBLE_DEVICES=0 python my_script.py
```

If you execute your script with this environment set, your script will only be able to see the GPU 0.

