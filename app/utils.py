import os
def ensure_dirs():
    base = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(os.path.join(base, 'uploads'), exist_ok=True)
    os.makedirs(os.path.join(base, 'indexes'), exist_ok=True)
