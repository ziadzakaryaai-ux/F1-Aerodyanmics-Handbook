# PART XVI — Aerodynamics Knowledge Map

The complete dependency structure of the subject. Each arrow means: *you must own the upper concept before the lower one makes sense.*

![Knowledge map](diagrams/knowledge-map.svg)
*Figure 16.1 — The full chain from fluid mechanics to aerodynamic development.*

## 16.1 The chain, in text

```text
Fluid Mechanics (ρ, p, T, μ; continuity; momentum; energy)
        ↓
Aerodynamics (force = ∮ pressure + shear over the surface)
        ↓
Airfoils & Wings (Cp distributions; camber; α; circulation)
        ↓
Pressure / Shear distributions (where force actually comes from)
        ↓
Lift / Drag / Downforce (coefficients; C_L A, C_D A; the polar)
        ↓
Boundary Layers (laminar vs turbulent; transition; Cf)
        ↓
Separation & Vortices (adverse gradients; stall; Γ; induced drag)
        ↓
Race-Car Aerodynamics (ground proximity; attitude; tyres; balance)
        ↓
Ground Effect (venturi tunnels; diffuser recovery; force map)
        ↓
Wings / Floor / Diffuser SYSTEM (exit conditions = inlet conditions)
        ↓
Wake & Wheel-Wake Management (outwash; sealing; dirty air)
        ↓
Aero Balance (CoP vs CG; balance maps; vehicle dynamics)
        ↓
Wind Tunnel  ──┬──  Validation & Correlation
CFD  ──────────┘
        ↓
Aerodynamic Development (hypothesis-driven loop; decisions)
```

## 16.2 The micro connection maps (cause chains)

These are the chains to be able to draw from memory — they appear throughout the handbook and are the fastest self-test of understanding.

**Speed chain**
```text
Velocity ↑  →  q = ½ρV² ↑  →  aero forces ↑ (∝V²)  →  tyre loading ↑
→  ride heights ↓ (springs compress)  →  floor force-map position moves
→  balance migrates rearward  →  handling changes with speed
```

**Ride-height chain (the one that explains porpoising)**
```text
Ride height ↓  →  tunnel area ↓  →  throat velocity ↑ (continuity)
→  throat Cp ↓ (momentum)  →  downforce ↑  →  springs compress further
→  (steep dF/dh: positive feedback)  →  choke/separation
→  downforce collapses  →  rebound  →  LIMIT CYCLE = porpoising
```

**Front-wing chain (the one that explains system coupling)**
```text
FW geometry change  →  outwash vortex path shifts
→  front-tyre wake lands elsewhere  →  floor fence inlet total pressure changes
→  tunnel mass flow changes  →  rear load & balance change
→  "a front-wing upgrade is a whole-car experiment"
```

**Drag trade chain**
```text
More wing load  →  induced drag ↑ (∝C_L²)  +  profile drag ↑
→  top speed ↓ (P ∝ V³)  →  straight-line time ↑
BUT  corner speeds ↑ (grip ∝ load, sub-linearly via tyre load sensitivity)
→  optimum = circuit-dependent purchase, not a maximum
```

**CFD trust chain**
```text
Physical problem → equations (N–S + turbulence model assumption)
→ discretisation + mesh (error budget) → convergence (monitors, not residuals)
→ post-processing (integrals + mechanism, not pictures)
→ validation ladder (tunnel → track) → decision
```

## 16.3 Prerequisite cross-reference

If you struggle with… …revisit:

| Symptom | Prerequisite to revisit |
|---|---|
| porpoising / force-map logic | Part I §1.7 continuity + Part II §2.5 separation |
| why slots work | Part II §2.5 (momentum injection into boundary layers) |
| induced drag | Part VI §6.2 (edge leakage → trailing vortices) |
| diffuser stalls | Part II §2.5 + Part V §5.3 (adverse gradient over expansion) |
| y⁺ discipline | Part II §2.5 + Part XII §12.6 (boundary-layer scaling) |
| balance travel | Part V §5.4–5.5 (force map) + Part X |
| why tunnel ≠ track | Part XI §11.2 (Reynolds mismatch) |
| "CFD says X" skepticism | Parts XII–XIV (error budget + interpretation) |

---

## SOURCES (Part XVI)

- Composite of the whole handbook's structure; no external sources beyond those cited in the respective parts.
