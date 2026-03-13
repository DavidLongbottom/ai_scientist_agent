import sys
import os
import argparse
import json
import shutil
from datetime import datetime
import torch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_scientist.treesearch.perform_experiments_bfts_with_agentmanager import perform_experiments_bfts
from ai_scientist.treesearch.bfts_utils import idea_to_markdown, edit_bfts_config_file

def get_available_gpus(gpu_ids=None):
    if gpu_ids is not None:
        return [int(gpu_id) for gpu_id in gpu_ids.split(",")]
    return list(range(torch.cuda.device_count()))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--idea", type=str, required=True, help="Path to a JSON file containing pregenerated ideas")
    parser.add_argument("--idea-idx", type=int, default=0, help="Index of idea to run")
    parser.add_argument("--output-json", action="store_true", help="Output result as JSON")
    args = parser.parse_args()

    try:
        with open(args.idea, "r") as f:
            ideas = json.load(f)
            
        idea = ideas[args.idea_idx]
        
        date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        idea_dir = f"experiments/{date}_{idea['Name']}"
        os.makedirs(idea_dir, exist_ok=True)

        idea_path_md = os.path.join(idea_dir, "idea.md")
        idea_to_markdown(idea, idea_path_md, None)

        idea_path_json = os.path.join(idea_dir, "idea.json")
        with open(idea_path_json, "w") as f:
            json.dump(idea, f, indent=4)

        config_path = "bfts_config.yaml"
        idea_config_path = edit_bfts_config_file(
            config_path,
            idea_dir,
            idea_path_json,
        )

        perform_experiments_bfts(idea_config_path)

        # Basic copy of results
        experiment_results_dir = os.path.join(idea_dir, "logs/0-run/experiment_results")
        if os.path.exists(experiment_results_dir):
            shutil.copytree(
                experiment_results_dir,
                os.path.join(idea_dir, "experiment_results"),
                dirs_exist_ok=True,
            )

        if args.output_json:
            result = {
                "status": "completed",
                "experiment_dir": idea_dir,
            }
            print(json.dumps(result))
            sys.exit(0)

    except Exception as e:
        if args.output_json:
            print(json.dumps({"status": "failed", "error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
