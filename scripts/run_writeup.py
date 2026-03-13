import sys
import os
import argparse
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_scientist.perform_writeup import perform_writeup as normal_writeup
from ai_scientist.perform_icbinb_writeup import perform_writeup as icbinb_writeup, gather_citations

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment-dir", type=str, required=True, help="Experiment directory")
    parser.add_argument("--type", type=str, choices=["normal", "icbinb"], default="icbinb")
    parser.add_argument("--citations-only", action="store_true")
    parser.add_argument("--model-writeup", type=str, default="o1-preview-2024-09-12")
    parser.add_argument("--model-citation", type=str, default="gpt-4o-2024-11-20")
    parser.add_argument("--model-writeup-small", type=str, default="gpt-4o-2024-05-13")
    parser.add_argument("--num-cite-rounds", type=int, default=20)
    parser.add_argument("--output-json", action="store_true", help="Output result as JSON")
    args = parser.parse_args()

    try:
        citations_text = gather_citations(
            args.experiment_dir,
            num_cite_rounds=args.num_cite_rounds,
            small_model=args.model_citation,
        )

        if args.citations_only:
            if args.output_json:
                print(json.dumps({"status": "completed", "citations_gathered": bool(citations_text)}))
            sys.exit(0)

        writeup_success = False
        if args.type == "normal":
            writeup_success = normal_writeup(
                base_folder=args.experiment_dir,
                small_model=args.model_writeup_small,
                big_model=args.model_writeup,
                page_limit=8,
                citations_text=citations_text,
            )
        else:
            writeup_success = icbinb_writeup(
                base_folder=args.experiment_dir,
                small_model=args.model_writeup_small,
                big_model=args.model_writeup,
                page_limit=4,
                citations_text=citations_text,
            )

        if args.output_json:
            print(json.dumps({
                "status": "completed" if writeup_success else "failed",
                "experiment_dir": args.experiment_dir
            }))
            sys.exit(0 if writeup_success else 1)

    except Exception as e:
        if args.output_json:
            print(json.dumps({"status": "failed", "error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
