(WandB)=
# WandB 

## Tutorials & Courses

```{note}
**Everyone training AI models take time to learn how to use WandB to keep track of your trainings and visualize your data.**
```

[**Official WandB Model Documentation**](https://docs.wandb.ai/?_gl=1*gp3xf8*_gcl_au*NjI3ODIyMzguMTczMzQxNzc1OA..)
[**Official WandB Weave Documentation**](https://weave-docs.wandb.ai/?utm_source=app&utm_medium=app&utm_campaign=weave-nudge)
[**Official WandB Courses**](https://www.wandb.courses/pages/w-b-courses)
[**Official WandB educational Github page**] (https://github.com/wandb/edu)

## Install WandB 

Full instruction to get started with WandB [here](https://docs.wandb.ai/quickstart/)
Start installing WandB using pip: 

```bash 
pip install wandb
```

Then log in your W&B account by running: 

```bash
wandb login
``` 
## Include WandB in your project 

Including WandB in your project provides a lot of advantages since it can help you track your trainings and visualize your data during training which should always be done !

### Initialize WandB 

To start using WandB in your project you need to import it and initialize. 

```python
import wandb 

wand.init(project='my_project_name')

```

Choose your project name carefully in order to be able to come back to it to compare the results you got with different versions of your code. You can for example use the name of the git repository or even the name of the code used. 

### Log Hyperparameters

In order to be able to distinguish between your different versions of model and compare them a good practice is to create a config dictionnary with all your hyperparameters and add it in your initialization of wandb. You can put in the config dictionnary all the informations you need to be able to distinguish between your models.  

```python 
config = {"learning_rate": 0.001, "batch_size": 32}
wandb.init(project="my_project_name", config=config)
```


**If you use the config dictionnary method to distinguish between your different models be sure to use the infos in config for your training and not to use some local variables like:**
```python
config = {"learning_rate": 0.001, "batch_size": 32}
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
```
**Instead use:**
```python
config = {"learning_rate": 0.001, "batch_size": 32}
train_loader = DataLoader(train_dataset, batch_size=config["batch_size"], shuffle=True)
```


### Log metrics 

WandB can be used to store your computed metrics, to do so you can use someting like this: 

```python 
for epoch in range(10):
    loss = compute_loss()
    wandb.log({"epoch": epoch, "loss": loss})
```



