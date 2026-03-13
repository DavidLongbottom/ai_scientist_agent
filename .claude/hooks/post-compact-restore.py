import os
import json

path = "experiments/plans/RESEARCH_STATE.json"
if os.path.exists(path):
    with open(path, "r") as f:
        state = json.load(f)
    print("Post-compact restore successful. Prior state summary:")
    print(json.dumps(state, indent=2))
else:
    print("No RESEARCH_STATE.json found. Fresh start after compact.")
