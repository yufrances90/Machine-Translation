import os

def load_data(filepath):
    
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
        
    return data