---
name: reading_pdf
description: >
  Use this skill whenever the user wants to read, analyze, or process a PDF
  in OpenCode with Claude Opus, especially university lecture notes, math
  scripts, or any PDF containing formulas, diagrams, or images. Trigger
  whenever the user mentions reading a PDF with Opus, passing a document to
  an AI in the terminal, or analyzing a PDF that may contain math or figures.
---

# OpenCode PDF Reader

Extracts text, LaTeX-rendered math, and embedded images from PDFs using
`pymupdf`, then passes everything to Opus in OpenCode.

## Why pymupdf

`pymupdf` (fitz) reads directly from PDF vectors, much better than
poppler-based tools for math-heavy documents. It also extracts embedded
images, which is essential for diagrams, plots, and proofs rendered as
raster images. Opus is multimodal and can interpret both.

## Step 1: Install dependency (once)

```bash
uv pip install pymupdf
```

## Step 2: Extract text + images

Run this script on the target PDF:

```python
#!/usr/bin/env python3
# extract_pdf.py
import fitz  # pymupdf
import sys
import os

pdf_path = sys.argv[1]
out_dir = "/tmp/pdf_extract"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
full_text = []

for page_num, page in enumerate(doc):
    # Text (preserves layout better than plain extract)
    text = page.get_text("text")
    full_text.append(f"--- Page {page_num + 1} ---\n{text}")

    # Images
    for img in page.get_images(full=True):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n > 4:  # CMYK ¿ RGB
            pix = fitz.Pixmap(fitz.csRGB, pix)
        img_path = f"{out_dir}/page{page_num+1}_img{xref}.png"
        pix.save(img_path)

text_path = f"{out_dir}/text.txt"
with open(text_path, "w") as f:
    f.write("\n".join(full_text))

print(f"Text saved: {text_path}")
print(f"Images saved: {out_dir}/")
```

```bash
python3 extract_pdf.py skript.pdf
```

## Step 3 ¿ Pass to Opus in OpenCode

**Text only** (fast, for straightforward questions):
```bash
opencode "$(cat /tmp/pdf_extract/text.txt)

---
Frage: [deine Frage hier]"
```

**Text + images** (for diagrams, plots, proofs as images):
```bash
# OpenCode supports attaching files ¿ list images alongside text
opencode --attach /tmp/pdf_extract/*.png \
  "$(cat /tmp/pdf_extract/text.txt)

---
Frage: [deine Frage hier]"
```

## Tips

- **Scanned PDFs** (no embedded text): run `ocrmypdf input.pdf output.pdf` first, then re-extract.
- **Large scripts (100+ pages)**: chunk by chapter. Extract page ranges with `doc.select([0..20])` to avoid context overflow.
- **Math formulas**: `pymupdf` preserves them as Unicode approximations (e.g. `¿`, `¿`). Opus handles this well. For perfect LaTeX, use `marker` (`uv pip install marker-pdf`) with `--output-format markdown` ¿ slower but cleaner.
