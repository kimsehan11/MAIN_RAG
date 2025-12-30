from datasets import load_dataset
from dotenv import load_dotenv
import os

load_dotenv()

def load_arc_dataset():
    dataset=load_dataset(
        "allenai/ai2_arc",
        "ARC-Challenge",
        split="train",
        )
    return dataset