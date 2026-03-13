import sys
import os
import argparse
import json
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_scientist.llm import create_client
from ai_scientist.perform_llm_review import perform_review, load_paper
from ai_scientist.perform_vlm_review import perform_imgs_cap_ref_review

def find_pdf_path_for_review(idea_dir):
    pdf_files = [f for f in os.listdir(idea_dir) if f.endswith(".pdf")]
    reflection_pdfs = [f for f in pdf_files if "reflection" in f]
    if reflection_pdfs:
        final_pdfs = [f for f in reflection_pdfs if "final" in f.lower()]
        if final_pdfs:
            return os.path.join(idea_dir, final_pdfs[0])
        else:
            reflection_nums = []
            for f in reflection_pdfs:
                match = re.search(r"reflection[_.]?(\d+)", f)
                if match:
                    reflection_nums.append((int(match.group(1)), f))
            if reflection_nums:
                highest_reflection = max(reflection_nums, key=lambda x: x[0])
                return os.path.join(idea_dir, highest_reflection[1])
            else:
                return os.path.join(idea_dir, reflection_pdfs[0])
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment-dir", type=str, required=True, help="Experiment directory")
    parser.add_argument("--type", type=str, choices=["llm", "vlm"], required=True, help="Type of review")
    parser.add_argument("--model", type=str, default="gpt-4o-2024-11-20")
    parser.add_argument("--output-json", action="store_true", help="Output result as JSON")
    args = parser.parse_args()

    try:
        pdf_path = find_pdf_path_for_review(args.experiment_dir)
        if not pdf_path or not os.path.exists(pdf_path):
            if args.output_json:
                print(json.dumps({"status": "failed", "error": "No PDF found"}))
            sys.exit(1)

        client, client_model = create_client(args.model)

        if args.type == "llm":
            paper_content = load_paper(pdf_path)
            review_text = perform_review(paper_content, client_model, client)
            out_file = os.path.join(args.experiment_dir, "review_text.txt")
            with open(out_file, "w") as f:
                f.write(json.dumps(review_text, indent=4))
        else:
            review_img_cap_ref = perform_imgs_cap_ref_review(client, client_model, pdf_path)
            out_file = os.path.join(args.experiment_dir, "review_img_cap_ref.json")
            with open(out_file, "w") as f:
                json.dump(review_img_cap_ref, f, indent=4)

        if args.output_json:
            print(json.dumps({
                "status": "completed",
                "experiment_dir": args.experiment_dir,
                "review_file": out_file
            }))
            sys.exit(0)

    except Exception as e:
        if args.output_json:
            print(json.dumps({"status": "failed", "error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
