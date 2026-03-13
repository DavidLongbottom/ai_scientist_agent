---
name: paper-compile
description: Compiles the latex and reads the log for errors.
---

# Paper Compile Workflow

This skill handles building LaTeX documents and handling standard errors.

## Operations
1. Execute `pdflatex` or similar tools (e.g., `latexmk -pdf`) on the target `.tex` file in the experiment `latex/` subdirectory.
2. Parse the compilation log.
3. If build fails due to typical LaTeX errors (e.g., missing package, undefined control sequence, mismatched braces):
   - Locate the exact line number.
   - Automatically propose a fix using file edit tools.
   - Retry Compilation.
4. Verify the final `paper.pdf` is generated successfully.
