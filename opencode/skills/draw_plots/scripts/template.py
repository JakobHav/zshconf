"""
Plot for ...

ai_generated: True
verified_by_human: False

"""

import matplotlib.pyplot as plt
import numpy as np


def V_out(V_in):
    if -V_in > 0.7:
        return V_in - (-0.7)
    return 0


t = np.linspace(0, 7, 101)
V_in = np.sin(t)*10
V_o = [V_out(vi) for vi in V_in]

plt.title("Spannung über der Diode")

plt.plot(t, V_in, label="V_in")
plt.plot(t, V_o, label="V_out")

plt.xlabel("Zeit [s]")
plt.ylabel("Spannung [V]")

plt.tight_layout()

plt.legend()
plt.savefig("ex01-circ01.png")

print("<plot> generated!")
