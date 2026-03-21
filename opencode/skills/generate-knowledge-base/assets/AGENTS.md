# AGENTS.md

## Project Scope

This project builds an excellent, exam-oriented learning knowledge base from past exams and lecture material.

The final structure is strictly hierarchical:

exams and script → topics → concepts

exams are a collection of Questions, each targeting a specific topic.
To understand a topic, one must understand a set of key concepts.

All documents are written in **Obsidian Markdown** and must be:

- Mathematically and electrically precise
- Structurally consistent
- Cross-linked via `[[wikilinks]]`
- Exam-grounded
- Concise but complete

The knowledge base must scale to many exams without redundancy or structural drift.

---

## AI-Generated Content Convention

All AI-generated notes **must** include the following frontmatter field:

```yaml
ai_generated: true
verified_by_human: false
```

This signals that the note has not been proofread by a human.

---

## Folder Structure

The project uses a strict folder hierarchy:

.
├── exam
│ ├── pdf # All individual exams as raw pdfs
│ └── markdown # All individual exams as markdown files. The exam depends heavily on images, so make sure to pull them from the exam and include where appropriate.
├── knowledge_base # Concept notes (atomic, reusable, mathematically precise)
├── topics # Collection of topics that exam question terget
├── exercises # exercises for practice or derivations
├── script # script to reference and link from topics/concepts
└── anki # Collection of anki decks, each deck targets one topic and is a sub-deck of the lecture deck.

### Folder Guidelines

- **exam/markdown**
  - Each exam note contains metadata, all questions, and solutions (if provided).
  - Links to relevant topics only.
  - Obsidian frontmatter must follow the standardized schema.
  - How to handle Diagrams — markdown tables/text for simple structures, extracted .png images for complex visuals

- **exam/topics**
  - Each topic note summarizes related theory, key concepts, and example exam tasks.
  - Contains a table of occurrences across exams.
  - Links to concepts and relevant lectures.

- **knowledge_base**
  - Each concept note is atomic and reusable across topics.
  - Includes definitions, formulas, properties, and minimal examples.
  - Includes _all_ names circuits from the script

- **excercises**
  - Includes Excercises from the lecture.

- **script**
  - The content serves as reference material for topics and concepts.

---

### Frontmatter format

Exam markdown notes MUST use the shape of this example frontmatter:

```yaml
source_pdf: "[[exam-WS2122.pdf]]"
semester: WS 21/22
date: 2022-03-04
duration_minutes: 135
total_points: 125
num_questions: 5
has_solutions: false
training_exam: false
thought_protocol: false
instructors:
  - Hannah Bast
  - Allthetu Tors
allowed_materials: "1 DIN A4 page (front + back), self-created"
course_name: Information Retrieval
topics:
  - "[[Inverted Index and Ranking]]"
  - "[[List Intersection and Search]]"
  - "[[Encodings and Compression]]"
  - "[[SPARQL and Knowledge Graphs]]"
  - "[[Fuzzy Search and Q-Grams]]"
  - "[[Web Applications]]"
  - "[[Naive Bayes Classification]]"
  - "[[Latent Semantic Indexing]]"
  - "[[Linear Classifiers and Logistic Regression]]"
```

## Core Principles

### 1. Exams Drive Structure

- The script is the primary source of truth. It includes a lot of circuit diagrams and images you should use.
- Topics are derived from recurring exam and excercise themes and names circuits in the script.
- Review the lab reports and also include topics from them.
- Concepts are derived from topic decomposition.

No topic or concept should exist without justification from:

- At least one exam task, or
- Essential lecture theory required to solve exam tasks.

---

### 2. Strict Normalization

- No duplicate topics.
- No duplicate concepts.
- Canonical naming must be consistent.
- Reuse existing notes instead of creating variants.

If unsure whether something is new:

- Prefer merging over duplicating.

---

### 3. Information Hierarchy

#### Exams

Contain:

- Metadata (strict frontmatter format)
- All tasks
- Solutions (optionaly provided)
- Links to topics (in task headers if possible)

Exams do not explain theory in depth. They just contain the questions.

#### Topics

Contain:

- High-level summary
- Structured explanation of required theory
- Decomposition into concepts
- Example exam questions with solutions
- Exam occurrence table
- Links to lecture notes

Topics synthesize. They do not duplicate full concept explanations.

#### Concepts

Contain:

- Formal definitions
- Mathematical formulas
- Properties
- Edge cases
- Minimal examples

Concepts are atomic and reusable. They contain no exam tables.

---

## Writing Standards

### Mathematical Rigor

- Use LaTeX for formulas.
- Define all variables.
- Always use Units.
- State assumptions explicitly.
- Avoid vague wording.
- Use only formulas directly from the script!

### Abstraction Level

- University-level precision!
- No oversimplified explanations.
- No unnecessary verbosity.

### Structure

Use consistent sections:

Topics

# Topic Name

## Summary

## Key Concepts

## Example Exam Questions

## Exam Appearances

## Related Lecture Notes

Concepts

# Concept Name

## Definition

## Formula

## Properties

## Example

---

## Obsidian Requirements

- Use `[[wikilinks]]` everywhere appropriate.
- Use callouts for:
  - Questions → `> [!question]`
  - Solutions → `> [!success]`
  - Important insights → `> [!note]`
- Use tables for exam appearances.
- Do not use raw URLs when internal links exist.

---

## Token Efficiency Guidelines

The agent must operate topic-scoped.

Never:

- Re-read the full vault.
- Regenerate entire notes unless requested.
- Reprocess unrelated topics.
- generate images.

Always:

- Work on one exam, excercise or one topic at a time.
- Only generate missing sections.
- Prefer deterministic structure generation (tables, metadata) outside the LLM when possible.
- Take and crop images from the script if possible.
- Avoid redundant explanation of already-defined concepts.
- use the skills provided to read pdf etc.

High quality must come from:

- Focused relevant context
- Not global context

---

## Update Policy

When updating notes:

- Preserve existing structure.
- Append or refine — do not rewrite unless necessary.
- Maintain consistent terminology.
- Keep cross-links intact.

---

## Quality Criteria

A topic note is considered complete when:

- All theory required for solving its exam tasks is explained.
- All formulas are correct and derived where necessary.
- All referenced concepts exist.
- The occurrence table is accurate.
- No redundancy with other topics exists.

A concept note is complete when:

- It is self-contained.
- It is mathematically und electrically precise.
- It is reusable across topics.

---

## Non-Goals

- No motivational text.
- No conversational tone.
- No speculation beyond lecture/exam scope.
- No duplication of lecture notes without synthesis.
- no ascii / text circuit diagrams!

---

## Ultimate Goal

The knowledge base should allow a student to:

1. Start from an exam.
2. Navigate to topics.
3. Drill down into concepts.
4. Fully understand and reproduce any solution independently.

The structure must remain scalable, normalized, and academically rigorous.

## Additional

### Script Structure (SS2019, 395 pages)
- **Pages 1-50**: Grundlagen (force, energy, charge, voltage, current, complex numbers, Ohm's law)
- **Pages 51-100**: Electrical components (resistivity, capacitors, inductors, magnetic fields)
- **Pages 101-150**: Network analysis (Kirchhoff's laws, voltage/current dividers, star-delta, Thévenin/Norton, superposition)
- **Pages 151-200**: Mesh current analysis, AC fundamentals (RMS, impedance, phase)
- **Pages 201-250**: AC power (Wirk-/Schein-/Blindleistung), filters, resonance (ω₀=1/√LC), transfer functions, Bode plots
- **Pages 251-300**: 2nd order filters, switching transients (RC/RL/RLC with τ), digital logic (Boolean algebra, De Morgan, gates)
- **Pages 301-350**: Semiconductors (Si, Ge doping), PN junction, diodes, bipolar transistors (NPN/PNP)
- **Pages 351-395**: MOSFETs (enhancement/depletion), CMOS, electromechanics (actuators, motors)

### Named Circuits from Script
- **Passive**: Plate capacitor, Coaxial cable, Multi-layer capacitor, Rotary capacitor, Wound capacitor, Cylindrical coil
- **Networks**: Wheatstone bridge, Ladder network, Star-delta conversion
- **Filters**: RC/RL low-pass/high-pass, RLC series/parallel (resonance), Bandpass/Bandstop 2nd order
- **Logic**: Half-adder, Full-adder, 4-bit parallel adder, S-R Flip-Flop, RTL NOR gate, CMOS inverter
- **Actuators/Motors**: Differential capacitor (accelerometer), Electromagnet (Schieber), DC commutator motor, 3-phase AC motor, Stepper motor

### Exam Topics Cross-Reference
Based on processed exams (SS2020, SS2021, SS2024, ET-Klausur), all topics map to script sections above.

