---
name: draw-plots
description: >
  Use this skill whenever the user wants to generate, draw, or render plots
  or graphs as image files — signal curves, Kennlinien, Bodediagramme,
  frequency responses, time series, or any numerical visualization with
  matplotlib. Trigger for any mention of plot, matplotlib, pyplot, Diagramm,
  Kennlinie, or "visualize data". Do NOT trigger for circuit diagrams
  (use draw_circuits) or Anki cards (use generate_anki).
---

# Draw Plots with matplotlib + numpy

Generate plots as PNG using `matplotlib` and `numpy`.
Always use `uv` — follow the `uv-venv` skill for environment setup.

```bash
uv venv && source .venv/bin/activate && uv pip install numpy matplotlib
```

Use `scripts/template.py` as the starting point for every new plot.

## Defaults — always apply these

```python
plt.tight_layout()
plt.savefig("output.png", dpi=150)
```

Use bare `plt.plot()` — no `fig, ax = plt.subplots()`.

- Use matplotlib's **default color cycle** — do not hardcode colors unless
  the plot specifically requires it (e.g. dual-axis where axis label color
  must match line color)
- Labels always with LaTeX for math: `"$V_{out}$"`, `"$\\omega$ [rad/s]"`
- Always call `ax.legend()` when there are multiple lines
- Always set `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()`

## Subplots

Use the `plt.subplot(rows, cols, index)` style:

```python
plt.subplot(1, 3, 1)
plt.plot(t, signal1)
plt.title("Signal 1")
plt.xlabel("Zeit [s]")
plt.ylabel("Spannung [V]")

plt.subplot(1, 3, 2)
plt.plot(t, signal2)
plt.title("Signal 2")
plt.xlabel("Zeit [s]")

plt.subplot(1, 3, 3)
plt.plot(t, signal3)
plt.title("Signal 3")
plt.xlabel("Zeit [s]")

plt.tight_layout()
plt.savefig("output.png", dpi=150)
```

## File header

Always include the docstring from the template:

```python
"""
Plot for ...
ai_generated: True
verified_by_human: False
"""
```
