import sys
import os
import argparse
import json
import logging
from datetime import datetime

# Add AI-Scientist root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_scientist.llm import create_client
from ai_scientist.perform_ideation_temp_free import generate_temp_free_idea

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workshop-file", type=str, required=True, help="Markdown file describing workshop/direction")
    parser.add_argument("--model", type=str, default="gpt-4o-2024-05-13")
    parser.add_argument("--max-num-generations", type=int, default=20)
    parser.add_argument("--num-reflections", type=int, default=5)
    parser.add_argument("--output-json", action="store_true", help="Output result as JSON for the skill layer")
    args = parser.parse_args()

    client, client_model = create_client(args.model)

    with open(args.workshop_file, "r") as f:
        workshop_description = f.read()

    output_path = args.workshop_file.replace(".md", ".json")

    try:
        ideas = generate_temp_free_idea(
            idea_fname=output_path,
            client=client,
            model=client_model,
            workshop_description=workshop_description,
            max_num_generations=args.max_num_generations,
            num_reflections=args.num_reflections,
            reload_ideas=True,
        )

        if args.output_json:
            result = {
                "status": "completed",
                "ideas_file": output_path,
                "ideas_count": len(ideas) if ideas else 0
            }
            print(json.dumps(result))
            sys.exit(0)
            
    except Exception as e:
        if args.output_json:
            print(json.dumps({"status": "failed", "error": str(e)}))
        else:
            logging.exception("Failed to run ideation")
        sys.exit(1)

if __name__ == "__main__":
    main()
