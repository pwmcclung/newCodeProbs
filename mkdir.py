import os
import os.path

def mkdirp(*directories):
    path = os.path.join(*directories) 
    try:
        os.makedirs(path, exist_ok=True) 
    except OSError as e:
        print(f"Error creating directory: {e}")