
from pathlib import Path
import pickle 
import skops.io as sio


project_dir = Path(__file__).resolve().parents[0]

with open(project_dir / "best_model.pickle", "rb") as f:
    model = pickle.load(f)
        
        
model_skops = sio.dumps(model)


