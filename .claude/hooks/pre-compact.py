import os
import json
from datetime import datetime

# Dump any live running state for skills.
# Here we'd save whatever is in the environment
state = {
    "sys_time": str(datetime.now()),
    "compression_trigger": True,
    "active_experiments": [],
    "recent_logs": []
}

if os.path.exists("experiments"):
    # List subdirectories that look like timestamped experiment folders
    dirs = [d for d in os.listdir("experiments") if os.path.isdir(os.path.join("experiments", d))]
    state["active_experiments"] = dirs

os.makedirs("experiments/plans", exist_ok=True)
with open("experiments/plans/RESEARCH_STATE.json", "w") as f:
    json.dump(state, f, indent=4)

print("Pre-compact triggered. State safely recorded to RESEARCH_STATE.json.")
