#!/usr/bin/env python3
r"""Generate Anki decks for <topic>

<short introduction>
"""

import genanki
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

BASIC_MODEL_ID = 1607392327
CLOZE_MODEL_ID = 1607392328

basic_model = genanki.Model(
    BASIC_MODEL_ID,
    "Opti Basis",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[
        {
            "name": "Karte 1",
            "qfmt": "{{Front}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
        }
    ],
    css=(
        ".card { font-family: sans-serif; font-size: 16px; text-align: left; }"
        " .card img { max-width: 100%; } code { background: #f4f4f4; padding: 2px 4px; }"
        " table { border-collapse: collapse; margin: 8px 0; }"
        " th, td { border: 1px solid #ccc; padding: 4px 8px; }"
    ),
)

cloze_model = genanki.Model(
    CLOZE_MODEL_ID,
    "Opti Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[
        {
            "name": "Lückentext",
            "qfmt": "{{cloze:Text}}",
            "afmt": "{{cloze:Text}}<br>{{Extra}}",
        }
    ],
    model_type=genanki.Model.CLOZE,
    css=(
        ".card { font-family: sans-serif; font-size: 16px; text-align: left; }"
        " code { background: #f4f4f4; padding: 2px 4px; }"
    ),
)

PARENT = "<topic>"


def basic(front: str, back: str) -> genanki.Note:
    return genanki.Note(model=basic_model, fields=[front, back])


def cloze(text: str, extra: str = "") -> genanki.Note:
    return genanki.Note(model=cloze_model, fields=[text, extra])


# ──────────────────────────────────────────────────────────────
# 1. Konvexität
# ──────────────────────────────────────────────────────────────
def deck_konvexitaet():
    d = genanki.Deck(2059400101, f"{PARENT}::Konvexität")
    cards = [
        # Definitionen
        basic(
            "Definition einer konvexen Funktion",
            r"\(f\colon \mathbb{R}^n \to \mathbb{R}\) heißt konvex, wenn für alle \(x, y\) und \(\lambda \in [0,1]\):"
            r"<br>\[ f(\lambda x + (1-\lambda)y) \leq \lambda f(x) + (1-\lambda)f(y) \]",
        ),
        basic(
            "Zweite-Ordnung-Bedingung für Konvexität",
            r"\(f\) ist konvex \(\Leftrightarrow\) die Hesse-Matrix \(\nabla^2 f(x) \succeq 0\) für alle \(x\).",
        ),
        ...
        # Exam-Fragen
        basic(
            r"Wahr oder Falsch: \(f(x) = 2x^2 + 1\) ist streng konvex.",
            r"<b>Wahr.</b> \(f''(x) = 4 > 0\) für alle \(x\).",
        ),
        ...
    ]
    for c in cards:
        d.add_note(c)
    return d


# ──────────────────────────────────────────────────────────────
# 2. Gradientenverfahren
# ──────────────────────────────────────────────────────────────
def deck_gradientenverfahren():
    d = genanki.Deck(2059400111, f"{PARENT}::Gradientenverfahren")
    cards = [
        basic(
            "Update-Regel beim Gradientenabstieg",
            r"\[ x_{k+1} = x_k - \alpha_k \nabla f(x_k) \]",
        ),
        ...
    ]
    for c in cards:
        d.add_note(c)
    return d


# ──────────────────────────────────────────────────────────────
# Generate all decks
# ──────────────────────────────────────────────────────────────
def main():
    deck_fns = [
        ("Konvexitaet", deck_konvexitaet),
        ("Gradientenverfahren", deck_gradientenverfahren),
    ]

    for name, fn in deck_fns:
        deck = fn()
        filepath = os.path.join(OUTPUT_DIR, f"{name}.apkg")
        genanki.Package(deck).write_to_file(filepath)
        print(f"  {filepath} ({len(deck.notes)} Karten)")

    total = sum(len(fn().notes) for _, fn in deck_fns)
    print(f"\nFertig! {total} Karten insgesamt über {len(deck_fns)} Decks.")


if __name__ == "__main__":
    main()
