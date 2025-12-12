import os
import wandb
from loadotenv import load_env

# Local folder and filename for the downloaded model
MODELS_DIR = "../models"
MODEL_FILENAME = "best_model.pth"


load_env()

# TODO: wrap into a function

def download_artifact():
    assert 'WANDB_API_KEY' in os.environ, "WANDB_API_KEY not found in environment variables"
    wandb_api_key = os.getenv("WANDB_API_KEY")
    wandb.login(key=wandb_api_key)
    api = wandb.Api()
    
    wandb_org = os.environ.get("WANDB_ORG")
    wandb_project = os.environ.get("WANDB_PROJECT")
    wandb_model_name = os.environ.get("WANDB_MODEL_NAME")
    wandb_model_version = os.environ.get("WANDB_MODEL_VERSION")


    artifact_path = f"{wandb_org}/{wandb_project}/{wandb_model_name}:{wandb_model_version}"
    artifact = api.artifact(artifact_path, type="model")
    print(f"Downloading artifact from {artifact_path}")
    artifact.download(root=MODELS_DIR)

download_artifact()