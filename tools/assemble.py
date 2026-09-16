"""Assembles the single-file handbook edition from part files, with title page and TOC."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER = [
    "part01-fluid-mechanics-foundations.md",
    "part02-aerodynamics-fundamentals.md",
    "part03-from-aircraft-to-race-car.md",
    "part04-f1-aerodynamic-architecture.md",
    "part05-ground-effect.md",
    "part06-vortices-and-flow-structures.md",
    "part07-wings-and-downforce.md",
    "part08-drag.md",
    "part09-tyres-wheels-and-wakes.md",
    "part10-aero-balance.md",
    "part11-wind-tunnel.md",
    "part12-cfd-fundamentals.md",
    "part13-cfd-for-f1.md",
    "part14-reading-cfd-results.md",
    "part15-f1-aerodynamic-development.md",
    "part16-knowledge-map.md",
    "part17-final-checklist.md",
    "part18-engineering-audit.md",
    "appendix-a-notation-units.md",
    "appendix-b-formula-sheet.md",
    "bibliography.md",
]

TITLE = """# FORMULA 1 AERODYNAMICS
## A Technical Study Guide & Handbook

**From fluid mechanics to CFD-driven development — a structured reference for an engineering student**

*Constructed September 2026 from verified public sources (FIA regulations, peer-reviewed literature, canonical textbooks, reputable technical press). Claims are tiered: verified / engineering inference / estimate — see the Engineering Audit (Part XVIII).*

**Level markers:** 🟢 FOUNDATION · 🟡 ENGINEERING · 🔴 AERODYNAMIC DEVELOPMENT

**How to use this handbook:** each part opens with purpose and course-connection lines; worked problems end with a mandatory *engineering interpretation*; quick-recall sections are for spaced repetition; misconception boxes correct the folklore. The single-file edition concatenates all parts — the folder edition (README.md + part files + diagrams/) is the same content for chapter-by-chapter study.

---

## CONTENTS

"""

def main():
    toc_lines = []
    body_parts = []
    for fn in ORDER:
        with open(os.path.join(ROOT, fn), encoding="utf-8") as f:
            text = f.read().rstrip() + "\n"
        m = re.match(r"^# (.+)$", text, flags=re.M)
        title = m.group(1) if m else fn
        toc_lines.append(f"- {title}")
        body_parts.append(text)
    out = TITLE + "\n".join(toc_lines) + "\n\n---\n\n" + "\n\n---\n\n".join(body_parts)
    dest = os.path.join(ROOT, "F1-Aerodynamics-Handbook-COMPLETE.md")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", dest, len(out), "chars")

if __name__ == "__main__":
    main()
