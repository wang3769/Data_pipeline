import os
from huggingface_hub import snapshot_download

# Define the local path
local_dir = "../models/tinyllama-chat"

# Create the directory if it doesn't exist
os.makedirs(local_dir, exist_ok=True)

# Download the model snapshot to that directory
model_path = snapshot_download(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    local_dir=local_dir,
    local_dir_use_symlinks=False
)

print(f"Model downloaded to: {model_path}")

'''
how to load and use it
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(local_dir)
model = AutoModelForCausalLM.from_pretrained(local_dir)

'''