import os
import pickle

def save_data(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

def load_data(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, 'rb') as inp:
        return pickle.load(inp)
