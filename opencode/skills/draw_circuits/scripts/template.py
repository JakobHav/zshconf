import schemdraw
import schemdraw.elements as elm
import matplotlib

matplotlib.use("Agg")

with schemdraw.Drawing() as d:
    d.config(unit=2)  # unit=2 makes elements have shorter than normal leads
    with d.hold():
        R1 = elm.Resistor().down().label('20Ω')
        V1 = elm.SourceV().down().reverse().label('120V')
        elm.Line().right(3).dot()
    elm.Line().right(3).dot()
    elm.SourceV().down().reverse().label('60V')
    elm.Resistor().label('5Ω').dot()
    elm.Line().right(3).dot()
    elm.SourceI().up().label('36A')
    elm.Resistor().label('10Ω').dot()
    elm.Line().left(3).hold()
    elm.Line().right(3).dot()
    R6 = elm.Resistor().toy(V1.end).label('6Ω').dot()
    elm.Line().left(3).hold()
    elm.Resistor().right().at(R6.start).label(
        '1.6Ω').dot(open=True).label('a', 'right')
    elm.Line().right().at(R6.end).dot(open=True).label('b', 'right')

    d.save("filepath.png", dpi=150)

print("<task> <file>.png saved.")
