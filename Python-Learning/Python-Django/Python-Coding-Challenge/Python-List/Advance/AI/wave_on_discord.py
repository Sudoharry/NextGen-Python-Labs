from transformers import BertModel, BertConfig
import torch

# Load the model config
config = BertConfig.from_pretrained("bert-base-uncased")  # or local path to config.json

# Create the model
model = BertModel(config)

# Load the weights
state_dict = torch.load(r"C:\Users\Nilesh\Downloads\weights.bin", map_location="cpu")
model.load_state_dict(state_dict)
