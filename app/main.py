import torch
import io
# This adds type hints and checking to our data 
from pydantic import BaseModel 
from torchvision.models import ResNet
from fastapi import FastAPI, File, UploadFile, Depends
from app.model import load_model, load_transforms 
from torchvision.transforms import v2 as transforms
from PIL import Image
import torch.nn.functional as F


class Result(BaseModel):
    category: str
    confidence: float