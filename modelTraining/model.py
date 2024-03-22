from transformers import AutoTokenizer, AutoModelForCasualLM

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
model = AutoModelForCasualLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

# https://discuss.huggingface.co/t/how-to-finetune-with-a-own-private-data-and-then-build-chatbot-on-that/48734/5
# https://huggingface.co/docs/transformers/en/training