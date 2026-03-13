import sys
import os
import argparse
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_scientist.perform_plotting import aggregate_plots
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment-dir", type=str, required=True, help="Directory containing the experiment")
    parser.add_argument("--model", type=str, default="o3-mini-2025-01-31", help="Model to use for plot aggregation")
    parser.add_argument("--output-json", action="store_true", help="Output result as JSON")
    args = parser.parse_args()

    try:
        aggregate_plots(base_folder=args.experiment_dir, model=args.model)
        
        # Original logic cleans up
        shutil.rmtree(os.path.join(args.experiment_dir, "experiment_results"), ignore_errors=True)

        if args.output_json:
            print(json.dumps({
                "status": "completed",
                "experiment_dir": args.experiment_dir
            }))
            sys.exit(0)
    except Exception as e:
        if args.output_json:
            print(json.dumps({"status": "failed", "error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
