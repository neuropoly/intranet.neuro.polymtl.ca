(WandB)=
# WandB

## Tutorials & Courses

```{note}
**Everyone training AI models should take time to learn how to use WandB to track their training and visualize data.**
```

[**Official WandB Model Documentation**](https://docs.wandb.ai/?_gl=1*gp3xf8*_gcl_au*NjI3ODIyMzguMTczMzQxNzc1OA..)
[**Official WandB Weave Documentation**](https://weave-docs.wandb.ai/?utm_source=app&utm_medium=app&utm_campaign=weave-nudge)
[**Official WandB Courses**](https://www.wandb.courses/pages/w-b-courses)
[**Official WandB Educational GitHub Page**](https://github.com/wandb/edu)

## Install WandB

Full instructions to get started with WandB can be found [here](https://docs.wandb.ai/quickstart/).
To install WandB using pip:

```bash
pip install wandb
```

Then log in to your WandB account by running:

```bash
wandb login
```

## Include WandB in Your Project

Integrating WandB into your project provides numerous benefits, such as tracking training progress and visualizing data in real time.

### Initialize WandB

To start using WandB in your project, import and initialize it:

```python
import wandb

wandb.init(project='my_project_name')
```

Choose a meaningful project name so you can easily compare different runs. You can use your Git repository name or a descriptive identifier for your experiment.

### Log Hyperparameters

To differentiate between different model versions and compare results, create a `config` dictionary with hyperparameters and pass it to WandB:

```python
config = {"learning_rate": 0.001, "batch_size": 32}
wandb.init(project="my_project_name", config=config)
```

**Ensure you use the config dictionary values in your training pipeline instead of hardcoded variables:**

**Incorrect:**
```python
config = {"learning_rate": 0.001, "batch_size": 32}
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
```

**Correct:**
```python
config = {"learning_rate": 0.001, "batch_size": 32}
train_loader = DataLoader(train_dataset, batch_size=config["batch_size"], shuffle=True)
```

### Log Metrics

WandB can store computed metrics. Example:

```python
for epoch in range(10):
    loss = compute_loss()
    wandb.log({"epoch": epoch, "loss": loss})
```

### Log Images

When applying transformations to images during training, it’s essential to verify them visually. Use WandB to log images:

```python
import numpy as np
import matplotlib.pyplot as plt

img = np.random.rand(28, 28)
wandb.log({"random_image": wandb.Image(img, caption="Sample Image")})
```

For 3D medical imaging data (e.g., `nii.gz` files), WandB does not support direct 3D visualization. Instead, select key slices and log them as 2D images:

```python
# Function to visualize slices
def plot_slices(image):
    image = image.float().numpy()
    mid_sagittal = image.shape[0] // 2
    fig, axs = plt.subplots(1, 6, figsize=(12, 6))
    for i in range(6):
        axs[i].imshow(image[mid_sagittal - 3 + i, :, :].T, cmap='gray')
        axs[i].axis('off')
    plt.tight_layout()
    return fig

# Include this in your training pipeline:
for epoch in range(epochs):
    model.train()
    for batch in train_loader:
        inputs = batch["image"].cuda()
        train_image = inputs[0].detach().cpu().squeeze()
        fig = plot_slices(train_image)
        wandb.log({"training images": wandb.Image(fig)})
        plt.close(fig)
        # Rest of the training pipeline...
```

### Save Model Artifacts

Save trained models with WandB:

```python
artifact = wandb.Artifact("model", type="model")
artifact.add_file("model.pth")
wandb.log_artifact(artifact)
```

### Finish a WandB Session

At the end of your script, ensure you close the WandB session:

```python
wandb.finish()  
```

## Check WandB Logs

There are two ways to check logs:

1. Log in to [WandB](https://wandb.ai/)
2. Use the link provided in the terminal when running your script.

When running your script with WandB, you should see an output similar to this:

```bash
wandb: Tracking run with wandb version 0.19.0
wandb: Run data is saved locally in /tmp/wandb/run-20250202_102609-84gg26e2
wandb: 🚀 View run at https://wandb.ai/<id/project_name/run_id>
```

Use the provided `View run` link to directly access the logs and visualizations of your training session. The same link will appear again when the session ends:

```bash
wandb: 🚀 View run at https://wandb.ai/<id/project_name/run_id>
wandb: ⭐ View project at https://wandb.ai/<id/project_name>
```

