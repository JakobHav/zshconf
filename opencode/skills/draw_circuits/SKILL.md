---
name: draw_circuits
description: >
  Use this skill whenever the user wants to draw, generate, or render
  electrical circuit diagrams — op-amps, resistors, capacitors, voltage
  sources, filters, amplifiers, or any circuit schematic. Trigger for any
  mention of schemdraw, circuit diagrams, Schaltpläne, Schaltbilder,
  op-amp circuits, or "draw this circuit". Also trigger when the user
  wants to visualize a circuit from a homework or exam problem.
---

# Draw Circuits with schemdraw

Generate circuit diagrams as PNG using `schemdraw` + `matplotlib`.
Always use `uv` — follow the `uv-venv` skill for environment setup.

```bash
uv venv && source .venv/bin/activate && uv pip install schemdraw matplotlib
```

Always check the gallery: `https://schemdraw.readthedocs.io/en/stable/gallery/index.html` for an existing circuit or close template and webfetch if found.

Always set the matplotlib backend before drawing to avoid display errors:
```python
import matplotlib
matplotlib.use("Agg")
```

## Key Concepts

**Coordinate system**: schemdraw draws elements sequentially. Each element
starts where the last one ended. Use `.at(pos)` to jump to a specific point.

**Op-amp anchors** — the most important reference points:
```python
op = d.add(elm.Opamp(leads=True).at((4, 0)))
op.in1   # inverting input (-)
op.in2   # non-inverting input (+)
op.out   # output
```

## Saving

```python
d.save("output/circuit.png", dpi=150)
```

## Template

You can find a Template in `scripts/template.py`
