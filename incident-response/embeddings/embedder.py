# embeddings/embedder.py
from transformers import AutoTokenizer, AutoModel
import torch

# Load SBERT model (example with 'sentence-transformers' variant of BERT)
model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def generate_embedding(text):
    """
    Generates an embedding for the given text using the SBERT model.
    
    Args:
        text (str): The text to embed.
        
    Returns:
        list: The embedding vector as a list of floats.
    """
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    
    # Generate the embedding
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Take the mean of the last hidden state to get a single vector embedding
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
    return embedding
