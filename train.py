import random
import sys
from dvclive import Live
import mlflow


with Live(save_dvc_exp=True) as live:
    with mlflow.start_run():

     epochs = 10
    live.log_param("epochs", epochs)
    mlflow.log_param("epochs", epochs)
    for epoch in range(epochs):
        live.log_metric("train/accuracy", epoch + random.random())
        live.log_metric("train/loss", epochs - epoch - random.random())
        live.log_metric("val/accuracy",epoch + random.random() )
        live.log_metric("val/loss", epochs - epoch - random.random())

        mlflow.log_metric("train/accuracy", epoch + random.random())
        mlflow.log_metric("train/loss", epochs - epoch - random.random())
        mlflow.log_metric("val/accuracy",epoch + random.random() )
        mlflow.log_metric("val/loss", epochs - epoch - random.random())
        live.next_step()