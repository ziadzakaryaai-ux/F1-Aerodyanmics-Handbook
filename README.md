# F1 Aerodynamics — A Technical Study Guide & Handbook

**A structured reference for an engineering student studying "Basics of Aerodynamics in F1 + CFD"**

Built from verified public sources: FIA regulations, peer-reviewed papers, canonical textbooks, and reputable motorsport-engineering journalism. Where public data is incomplete, claims are labelled as **engineering inference** or **estimate** rather than presented as fact.

---

## 1. How to use this handbook

- **Read Part I–II before anything else.** Everything downstream depends on pressure fields, boundary layers and the momentum picture of lift. Do not skip the misconception boxes — most self-taught aero knowledge contains at least two of them.
- **Work the MINI PROBLEMS with a calculator.** They are deliberately small (5–15 minutes) but they convert reading into intuition. Every solution ends with an *Engineering Interpretation* — that is the part that matters.
- **Use QUICK RECALL as spaced repetition.** Cover the answers, answer aloud, then check. Revisit parts after you cover the corresponding course module.
- **The ENGINEERING INTUITION boxes** compress each section to the one sentence an aerodynamicist would actually carry in their head.
- **LEVEL markers** tell you how deep you are:
  - 🟢 **LEVEL 1 — FOUNDATION**: understand the concept itself.
  - 🟡 **LEVEL 2 — ENGINEERING**: apply it to a race car.
  - 🔴 **LEVEL 3 — DEVELOPMENT**: reason about design, CFD, testing and trade-offs like an aerodynamicist.

## 2. Structure of the guide

| Part | File | Topic | Level |
|---|---|---|---|
| I | `part01-fluid-mechanics-foundations.md` | Fluid mechanics foundations | 🟢→🟡 |
| II | `part02-aerodynamics-fundamentals.md` | Forces, pressure fields, boundary layers, lift | 🟢→🟡 |
| III | `part03-from-aircraft-to-race-car.md` | Why race-car aero ≠ aircraft aero | 🟡 |
| IV | `part04-f1-aerodynamic-architecture.md` | F1 car as an aerodynamic system | 🟡→🔴 |
| V | `part05-ground-effect.md` | Ground effect, underbody, diffuser, porpoising | 🟡→🔴 |
| VI | `part06-vortices-and-flow-structures.md` | Vortices, flow conditioning, wake management | 🟡→🔴 |
| VII | `part07-wings-and-downforce.md` | Wing theory → F1 front/rear wings | 🟡→🔴 |
| VIII | `part08-drag.md` | Drag taxonomy and F1 drag sources | 🟡 |
| IX | `part09-tyres-wheels-and-wakes.md` | Rotating wheels and wheel wake | 🟡→🔴 |
| X | `part10-aero-balance.md` | Aero balance, handling, setup | 🟡→🔴 |
| XI | `part11-wind-tunnel.md` | Wind-tunnel testing and model testing | 🟡→🔴 |
| XII | `part12-cfd-fundamentals.md` | CFD from first principles | 🟡→🔴 |
| XIII | `part13-cfd-for-f1.md` | A realistic F1 CFD workflow + failure modes | 🔴 |
| XIV | `part14-reading-cfd-results.md` | Interpreting CFD output with judgment | 🔴 |
| XV | `part15-f1-aerodynamic-development.md` | The development loop + worked case studies | 🔴 |
| — | `part16-knowledge-map.md` | Final knowledge structure & connection maps | — |
| — | `part17-final-checklist.md` | "Can I actually understand F1 aerodynamics yet?" | — |
| — | `part18-engineering-audit.md` | Weak evidence, disagreements, simplifications | — |
| — | `appendix-a-notation-units.md` | Symbols and units | — |
| — | `appendix-b-formula-sheet.md` | One-page formula sheet | — |
| — | `bibliography.md` | All sources, mapped to their use | — |

A single-file edition (`F1-Aerodynamics-Handbook-COMPLETE.md`) concatenates everything for reading/printing.

## 3. Callout conventions

```text
> **ENGINEERING INTUITION**      → the "if you remember only one thing" box
> **COMMON MISCONCEPTIONS**      → wrong-but-common statements, corrected
> **TERM** blocks                → Simple / Technical / F1-relevance definition
> **COURSE CONNECTION**          → where to slot this into your course (fill in as you go)
```

## 4. Course-integration protocol

Your course is the syllabus; this handbook is the backbone. Every part ends with a *Course connection* line. Since the handbook was built without access to your course materials, these lines map each part to the **canonical textbook chapters and public references** that typically carry the same material (e.g., Anderson ch. 4 ↔ airfoil theory; Katz ch. 2–4 ↔ race-car fundamentals). When you reach the matching module, annotate the line with the module/lecture number — that annotation is your revision index.

If the course presents something this handbook flags as a misconception (e.g., "equal transit time" style lift explanations), the handbook deliberately does not reproduce it: the flagged, technically accurate version is given instead, with the reasoning.

## 5. Citation policy

- **VERIFIED**: confirmed against a primary or reputable source during construction (FIA regulations, journal papers, textbooks, major technical press). Cited per part and in `bibliography.md`.
- **ENGINEERING INFERENCE**: a logical engineering conclusion from verified physics, not a published number. Marked inline.
- **ESTIMATE / PUBLIC-DATA LIMITED**: order-of-magnitude figures circulating in the public domain (downforce multiples, drag areas). Always given as ranges, never as team data.
- No confidential team information appears anywhere. Approximate values are marked "approximately", "order of", or "depends on configuration" — per the no-fake-precision rule.

## 6. Notation

SI units throughout (see Appendix A). Key conventions:

- Aerodynamic forces are expressed through non-dimensional coefficients and the **reference area** $S$ (or "area" $A$); F1 teams quote **downforce area** $C_L A$ and **drag area** $C_D A$ because reference-area conventions vary between teams and regulations eras.
- "Lift" of an F1 car is **negative lift = downforce**. In this handbook, downforce is treated as positive-down unless a formula inherits the aviation sign convention.
- $y^+$, $C_p$, $Re$, $Ma$ are dimensionless by construction — unit errors elsewhere are the classic student failure mode; check units on every worked problem.

## 7. Source tiers (as applied)

1. **Tier 1** — FIA Formula 1 Technical Regulations & Sporting Regulations; peer-reviewed journal papers (Journal of Aircraft, AIAA Journal, ASME JFE); canonical textbooks (Anderson; Katz; Hucho; Versteeg & Malalasekera).
2. **Tier 2** — Motorsport-engineering technical press (Racecar Engineering, Autosport technical, Motorsport Magazine), papers by former F1 aerodynamicists (e.g., W. Toet).
3. **Tier 3** — General references, used only for clarification and marked as such.
