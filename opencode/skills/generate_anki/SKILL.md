---
name: generate-anki
description: >
  Use this skill whenever the user wants to generate Anki flashcard decks
  (.apkg files) from lecture notes, PDFs, or study material — especially
  university topics with math formulas. Trigger for any mention of Anki,
  flashcards, genanki, spaced repetition, or "Lernkarten". Also trigger
  when the user wants to turn a knowledge base, Obsidian vault, or lecture
  script into a deck.
---

# Generate Anki Decks

Generate `.apkg` Anki decks using `genanki`. Always use `uv` — follow the
`uv-venv` skill for environment setup.

```bash
uv venv && source .venv/bin/activate && uv pip install genanki
```

## Card Design Rules

- Use Anki math syntax: inline `\( ... \)`, block `\[ ... \]`
- Don't make questions too specific — test understanding, not memorization
- Orient heavily on past exam questions
- Mix Basic (Q&A) and Cloze (fill-in-the-blank) cards
- Always use raw strings (`r"..."`) for LaTeX to avoid backslash issues

## Workflow

1. Understand the topic structure first (vault, PDF chapters, lecture outline)
2. Map structure → one `genanki.Deck` per topic/chapter
3. Generate the script from `scripts/template.py`
4. Run it — each deck produces a separate `.apkg` file

## Script Template

See `scripts/template.py` for the full boilerplate. Key patterns:

```python
# Basic card
basic("Was ist die Update-Regel beim Gradientenabstieg?",
      r"\[ x_{k+1} = x_k - \alpha_k \nabla f(x_k) \]")

# Cloze card
cloze(r"\(f\) ist konvex \(\Leftrightarrow\) {{c1::Hesse-Matrix \(\succeq 0\)}}")
```

Deck IDs must be unique integers — increment per deck (e.g. 2059400101, 2059400102, ...).
