---
name: typst
description: >
  Write, create, or edit Typst (.typ) documents — a modern markup-based typesetting system
  that compiles to PDF. Use this skill whenever the user asks to create a Typst file, write
  a .typ document, build a Typst template, convert content to Typst, style a Typst document,
  or asks about Typst syntax, set/show rules, or layout. Also trigger for any document type
  (report, paper, CV, letter, slides, thesis) when the user specifies Typst or PDF as the format.
---

# Typst Skill

Typst is a markup-based typesetting system — a modern alternative to LaTeX. Files are `.typ`,
output is PDF. Reference: https://typst.app/docs/

---

## Three Modes

| Mode   | Enter with          | Purpose                        |
|--------|---------------------|--------------------------------|
| Markup | default             | prose, headings, lists         |
| Math   | `$...$`             | inline or block equations      |
| Code   | `#` prefix          | scripting, functions, logic    |

In code mode (inside `#{}` or after `#`), no further `#` prefix is needed.

---

## Markup Cheatsheet

```typ
= Heading 1
== Heading 2
=== Heading 3

*bold*   _italic_   `monospace`   #strike[strikethrough]   #underline[underline]

- unordered list
  - nested

+ ordered list
+ second item

1. also works
1. for ordered lists

#quote(attribution: [Author])[Block quote text]

#link("https://typst.app")[link text]

@label-name          // cross-reference
<label-name>         // attach label to element

---                  // horizontal rule
\                    // explicit line break
~                    // non-breaking space
```

---

## Math

```typ
Inline: $a^2 + b^2 = c^2$

Block (spaces around content):
$ integral_0^1 f(x) dif x = F(1) - F(0) $

$ mat(1, 0; 0, 1) $          // matrix
$ vec(x, y, z) $             // vector
$ sum_(i=0)^n i = (n(n+1))/2 $
$ cases(x & "if" x > 0, -x & "otherwise") $

// Multi-letter identifiers are functions — quote for text:
$ sin(theta) + "const" $
```

---

## Set Rules — Global Defaults

```typ
#set text(font: "New Computer Modern", size: 11pt, lang: "en")
#set page(paper: "a4", margin: (x: 2.5cm, y: 3cm), numbering: "1")
#set par(justify: true, leading: 0.65em)
#set heading(numbering: "1.1")

// Conditional set rule
#set text(red) if condition
```

Set rules apply from their position to the end of the current scope. Later rules win on conflict.

---

## Show Rules — Element Transformation

```typ
// Show-set rule (targeted set rule)
#show heading: set text(font: "Inria Serif")
#show heading.where(level: 1): set text(size: 16pt)

// Transformational show rule
#show heading: it => block[
  #set text(weight: "regular")
  #counter(heading).display(it.numbering). #it.body
]

// String replacement
#show "Typst": [*Typst*]

// Everything rule (wrap entire doc in template)
#show: doc => template(doc)
// or with named args:
#show: template.with(title: "My Doc", author: "Me")
```

---

## Page & Layout

```typ
#set page(
  paper: "a4",           // "us-letter", "a5", etc.
  margin: (top: 2cm, bottom: 2cm, left: 2.5cm, right: 2.5cm),
  header: align(right)[My Header],
  footer: align(center)[#counter(page).display("1 / 1", both: true)],
  numbering: "1",
  columns: 2,
  background: ...,
  foreground: ...,
)

#pagebreak()
#colbreak()

#columns(2)[
  Content in two columns.
  #colbreak()
  Column 2 starts here.
]

#align(center)[Centered content]
#align(right + bottom)[Bottom right]
```

---

## Common Functions

```typ
// Text styling
#text(size: 14pt, fill: blue, weight: "bold")[styled text]
#highlight(fill: yellow)[highlighted]
#smallcaps[Small Caps]
#super[superscript]  #sub[subscript]

// Blocks & boxes
#block(fill: luma(240), inset: 10pt, radius: 4pt)[Box content]
#box(width: 1fr)[inline box]

// Spacing
#v(1em)       // vertical space
#h(0.5em)     // horizontal space

// Images
#figure(
  image("path/to/image.png", width: 80%),
  caption: [Figure caption],
) <fig-label>

// Tables
#figure(
  table(
    columns: (auto, 1fr, 1fr),
    align: (left, center, right),
    table.header([Name], [Value], [Unit]),
    [R], [10], [Ω],
    [C], [100], [nF],
  ),
  caption: [Component values],
)

#align(right)[] // algining content

#place(right)[] // placing content (align without taking height / space)


// Code blocks
#raw(lang: "python", block: true, "def f(x):\n    return x")
// or with fences:
```python
def f(x):
    return x
```
```

---

## Scripting

```typ
// Variables and functions
#let x = 42
#let greeting(name) = [Hello, #name!]
#greeting("World")

// Control flow
#if condition [true branch] else [false branch]

#for item in (1, 2, 3) [
  - Item #item
]

// Arrays and dicts
#let arr = (1, 2, 3)
#let dict = (key: "value", n: 42)
#dict.key       // field access
#arr.at(0)      // index

// Content blocks
#let note = [This is *content* stored in a variable.]
#note

// Joining content
#{ [Hello ] + [World] }
```

---

## Counters & References

```typ
// Label and reference
= Introduction <intro>
See @intro for details.

// Figure references work the same:
#figure(image("f.png"), caption: [Plot]) <plot>
As shown in @plot...

// Manual counter
#let my-counter = counter("custom")
#my-counter.step()
#my-counter.display()

// Page counter
#counter(page).display("1 of 1", both: true)
```

---

## Template Pattern

Best practice for reusable templates (`template.typ`):

```typ
#let template(
  title: "",
  author: "",
  doc,
) = {
  // Page setup
  set page(paper: "a4", numbering: "1", margin: 2.5cm)
  set text(font: "New Computer Modern", size: 11pt)
  set par(justify: true)
  set heading(numbering: "1.")

  // Title block
  align(center)[
    #text(18pt, weight: "bold")[#title]
    #v(0.5em)
    #text(12pt)[#author]
    #v(1em)
    #line(length: 100%)
    #v(1em)
  ]

  // Render document
  doc
}
```

Usage in main file:

```typ
#import "template.typ": template
#show: template.with(title: "My Report", author: "Jane Doe")

= Introduction
...
```

---

## Packages (Typst Universe)

Local package:

- When Tasked to create a worksheet or document related to university at all, use this template:
```typ
/*
Created by AI on behalf of Jakob Haverkamp
*/
#import "@local/ufr-sheet-universal:0.1.0": conf

#show: doc => conf(
  doc,
  subject: "Einführung in die Programmierung",
  date: "04.02.2026",
  prof: "Prof. Dr. Peter Thiemann",
  semester: "WS 2025/2026",
  title: [Klausur für mein Tutorat],
  left_header: [\ Autor: \ Jakob Haverkamp ],
  header: ([EidP], [Tutorklausur WS 25/26], "Jakob H."),
)

```

Import from the package registry:

```typ
#import "@preview/package-name:0.1.0": function-name
```

Common packages:
- `@preview/cetz:0.3.0` — TikZ-like drawing
- `@preview/fletcher:0.5.0` — diagrams with arrows
- `@preview/algo:0.3.3` — algorithm pseudocode
- `@preview/codly:1.0.0` — code blocks with line numbers
- `@preview/physica:0.9.3` — physics notation
- `@preview/tablex:0.0.9` — advanced tables

---

## Common Pitfalls

| Problem | Fix |
|---|---|
| `#` inside string doesn't start code | Strings use `"..."`, not markup |
| Show rule not applying | Check scope — rules end at closing `}` or `]` |
| `set` inside show rule not overridable | Use show-set rules instead of set inside transformational show |
| Two content args to function | Use trailing `[...]` syntax: `f(arg)[content]` |
| Math identifier renders wrong | Quote multi-letter text: `$"velocity"$` or define op: `#let vel = math.op("vel")` |
| Landscape page for one page | `#set page(flipped: true)` scoped in a block |


# Compilation

## Core Commands

```bash
# Compile to PDF (output inferred from input name)
typst compile file.typ
 
# Explicit output path
typst compile file.typ output.pdf
 
# Watch mode — recompiles on every save
typst watch file.typ
 
# Init a project from a template (Typst Universe)
typst init @preview/charged-ieee
typst init @preview/charged-ieee:0.1.0  # pinned version
```
 
## Output Formats
 
```bash
# PDF (default)
typst compile file.typ output.pdf
 
# PNG — {p} required for multi-page docs
typst compile file.typ page-{p}.png
typst compile file.typ page-{0p}-of-{t}.png   # zero-padded, with total
typst compile file.typ page-{p}.png --ppi 300  # high-res
 
# SVG
typst compile file.typ page-{p}.svg
 
# HTML (experimental)
typst compile file.typ output.html
```
 
## Useful Flags
 
```bash
# Custom font directories
typst compile file.typ --font-path ./fonts
# or via env var
TYPST_FONT_PATHS=./fonts typst compile file.typ
 
# List all discovered fonts
typst fonts
typst fonts --font-path ./fonts
 
# Compile specific pages only
typst compile file.typ out.pdf --pages 1-3,5
 
# PDF/A standard
typst compile file.typ out.pdf --pdf-standard a-1b
 
# Open result after compile
typst compile file.typ --open
 
# Pass variables into the document
typst compile file.typ --input key=value
# Access in .typ: #sys.inputs.at("key")
 
# Set project root (controls what files the document can access)
typst compile file.typ --root ./project
```

---

## Output

Always produce complete, compilable `.typ` files. Include all necessary `#import` and `#set`
rules at the top. Do not omit boilerplate — Typst has no implicit defaults beyond its built-ins.
