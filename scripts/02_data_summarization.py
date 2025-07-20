from transformers import pipeline

from transformers import AutoModelForCausalLM, AutoTokenizer

local_dir = "../models/tinyllama-chat"
tokenizer = AutoTokenizer.from_pretrained(local_dir)
model = AutoModelForCausalLM.from_pretrained(local_dir)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Run inference
output = generator("cat is mean.", max_new_tokens=100)
print(output[0]['generated_text'])