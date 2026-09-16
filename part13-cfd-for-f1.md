# PART XIII — CFD for F1

**Purpose:** walk through a realistic aerodynamic CFD workflow end-to-end, then catalogue the failure modes that produce confident nonsense. This is the operational companion to Part XII's theory.

**Course connection:** anchors: a CFD-project lab course; Versteeg & Malalasekera ch. on implementation; Ferziger & Perić ch. on practical accuracy. Module mapping: ____________

![CFD workflow loop](diagrams/p15-loop.svg)
*Figure 13.1 — The loop each geometry travels (Part XV expands the engineering decisions inside it).*

---

## 13.1 The workflow, stage by stage 🔴

**1–2. CAD preparation & geometry cleanup.** Design surfaces arrive as CAD; regulations-derived envelopes, negative-volume gaps, tiny slivers and leak artifacts are cleaned. Cleanup is where real-world CFD dies quietly: an unresolved 0.1 mm gap can leak mass flow and corrupt an entire underbody. The virtual model must represent the *regulated, real* geometry — including regulation-mandated items (plank, skids, wheel covers).

**3. Domain creation.** Sized so boundaries don't influence the solution: several car lengths downstream (wake development), enough upstream/sideways for inlet relaxation; ground as a moving wall; symmetry only if the campaign can afford its assumptions (Part XII §12.4).

**4. Meshing.** The error budget: surface mesh resolves curvature; inflation layers hit the project's y⁺ policy; wake/underbody refinement boxes follow the gradients (Fig. 12.1). Mesh *policy* is frozen across a campaign so deltas are geometry-driven, not mesh-driven.

**5. Boundary conditions.** Freestream velocity/pressure, ground and wheel motions, inlet turbulence matched to the project's tunnel/track conventions (Part XII). At yaw, the domain or the reference frame is rotated — the choice must be consistent across the campaign.

**6–7. Solver setup & turbulence model.** Steady, pressure-based RANS with k-ω SST is the motorsport default (Part XII §12.5); discretisation schemes second-order in the far field, more robust near separation; project-standard relaxation/CFL. Unsteady campaigns (URANS/DES) declare their time-step/CFL policy and averaging windows up front.

**8. Initialisation.** Uniform freestream or a previous solution ("warm start"). Warm-starting saves cost but can *bias toward the previous design's flow structures* — dangerous when the question is "does the new geometry change the topology?"

**9. Convergence.** Monitors: forces/moments per component (front/rear wing, floor...), mass-flow through tunnels/inlets, residuals as backup (Part XII §12.7, Fig. 12.2). Stopping criteria are standardised *per campaign*; unsteady runs standardise averaging windows. Everything measurable is written down: mesh version, BCs, model, iteration count.

**10–12. Extraction: forces, pressures, flow visualisation.** Component force breakdown; Cp maps along elements/floor; survey planes (velocity, vorticity, Q-criterion, TKE) at the stations the hypothesis cares about (Part XIV teaches the reading).

**13. Design comparison.** The currency is the **delta**: ΔC_L A (total and per axle), ΔC_D A, Δ balance, plus *mechanism evidence* (which surface pressure changed, which vortex moved). Deltas are evaluated at matched attitude and, ideally, across a small map (heave/yaw) for robustness.

**14. Validation against experiment.** Laddered: tunnel forces (same scale model conventions) → pressure taps (distribution-level) → wake/aero rakes (field-level) → track (lap-time/correlation level). A delta that survives the ladder is a design; one that dies is a lesson.

**15. Engineering decision.** Ship / iterate / park — with the *reason* documented (Part XV).

**ENGINEERING INTUITION**
> If you remember only one thing: an F1 CFD campaign is an *instrument calibration* problem wearing a design competition's clothes — freeze everything that isn't the geometry, and freeze the geometry's evaluation recipe too.

---

## 13.2 Failure modes: how good engineers produce wrong numbers 🔴

| Failure | Mechanism | Symptom / defence |
|---|---|---|
| **Bad mesh** | poor quality cells, insufficient prism layers, coarse wakes | results flip between mesh versions; defence: quality gates + GCI (Part XII) |
| **Wrong BCs** | fixed ground, static wheels, mismatched inlet turbulence | underbody deltas that die in the tunnel; defence: BC checklist per project |
| **Poor convergence** | forces still drifting when "stopped" | deltas smaller than monitor noise; defence: monitor-window protocol |
| **Wrong turbulence model** | SST on massively separated transient flow, or model switched mid-campaign | mechanism "explanations" that don't replicate; defence: model frozen + validated per campaign |
| **Numerical diffusion** | coarse cells + upwind smearing wakes/vortices | downstream devices underperform vs tunnel; defence: scheme policy + refinement zones |
| **Insufficient resolution** | features (slot jets, edge vortices) unresolved | designs ranked by mesh artifact; defence: resolution studies on the *feature*, not just forces |
| **Unrealistic geometry** | leaks, simplified wheels, missing regulation details | magnitudes right, deltas wrong; defence: geometry audits |
| **Plot worship** | judging "colourful = better" | Part XIV's whole subject; defence: integrals + mechanism evidence |
| **Optimising numerical noise** | chasing deltas smaller than run-to-run repeatability | "gains" vanish on re-run; defence: repeatability quantified, minimum meaningful delta defined |

The last row deserves emphasis: repeatability (same input, re-run) sets the floor of meaningful delta. A 0.1% gain on an instrument with 0.3% noise is not a gain — it is a decision to be fooled.

---

## COMMON MISCONCEPTIONS (Part XIII)

> ❌ **"CFD setup is engineering; meshing is IT work."** The mesh *is* the physics budget; most silent failures are mesh failures.
>
> ❌ **"Warm-starting is free speed."** It can anchor the flow topology to the old design — the one thing you're testing.
>
> ❌ **"If CFD and tunnel disagree, one is broken."** They disagree *systematically*; the disagreement map (which component, which attitude) is itself engineering data.
>
> ❌ **"Unsteady always beats steady."** URANS/DES costs order-of-magnitude more; for attached-flow deltas, steady RANS answers the question. Match the tool to the hypothesis.
>
> ❌ **"The simulation validated the design because the forces went up."** Force deltas validate nothing by themselves; only the tunnel/track ladder does (Part XV).

---

## F1 ENGINEERING QUESTIONS (Part XIII)

**Conceptual**
- Why must mesh policy be frozen across a campaign, and what breaks if it isn't?
- What is the difference between "converged" and "repeatable", and why do you need both?

**Engineering**
- You inherit a campaign where every design was meshed individually. What can you still trust, and how do you find out?
- A new floor shows +0.8% total load in CFD but the rear-wing component shows −0.3%. What do you investigate first?

**CFD**
- Write the checklist you would run before believing a new geometry's first result.
- How would you design the repeatability experiment (same input twice) for a steady-RANS campaign?

**Design**
- Budget: 48 h wall-clock on the cluster for one design point. Steady RANS ×8 attitudes, or URANS ×1 attitude? Justify by the hypothesis you'd write.
- A component looks excellent in CFD but the tunnel can't see it. Compose the investigation plan.

---

## QUICK RECALL (Part XIII)

1. List the 15 workflow stages in order (compressed to their key verbs).
2. Name five failure modes and one defence for each.
3. Why is geometry cleanup safety-critical for underbody simulations?
4. What does "deltas at matched policy" mean, and why does it matter?
5. What is the validation ladder, in order?
6. Why can warm-starting bias a topology question?
7. What sets the minimum meaningful delta in a campaign?
8. Why are per-component force monitors more informative than total only?
9. What must an unsteady campaign declare before running?
10. Why is "colourful plot" not an acceptance criterion?

### ANSWERS

1. Clean CAD → domain → mesh (policy frozen) → BCs → solver/model → initialise → converge (monitors) → extract forces/pressure/flow → compare deltas → validate → decide.
2. Bad mesh→quality gates/GCI; wrong BCs→checklist; poor convergence→monitor protocol; wrong model→freeze+validate; plot worship→integrals+mechanism (any five).
3. A sub-mm leak or sliver corrupts mass flow/pressure integration — the floor's whole signal.
4. Same mesh policy, BCs, model, stopping rule for baseline and variant → the delta is attributable to geometry alone.
5. Tunnel forces → pressure taps → wake/rake surveys → track correlation.
6. The initial flow field carries the old design's structures; a genuinely new topology may be masked.
7. Run-to-run repeatability (numerical noise floor) of the whole pipeline.
8. Total gain can hide redistribution (e.g., front gains, rear losses = balance change).
9. Time step/CFL, averaging window, model (URANS/DES), stopping criteria — so deltas are comparable.
10. Plots are post-processing views; acceptance is integrated deltas + mechanism + validation (Part XIV).

---

## SOURCES (Part XIII)

- Versteeg, H. K. & Malalasekera, W., *An Introduction to Computational Fluid Dynamics* (2nd ed., Pearson, 2007) — implementation practice. [Tier 1]
- Ferziger, J. H. & Perić, M., *Computational Methods for Fluid Dynamics* (3rd rev. ed., Springer, 2002) — accuracy/convergence practice. [Tier 1]
- Celik, I. B. et al., *ASME J. Fluids Engineering* 130(7), 2008 — discretisation-uncertainty reporting. [Tier 1]
- Toet, W. (2013), *The Aeronautical Journal* 117(1187) — F1 CFD/tunnel/track workflow from practice. [Tier 2]
- Public team/engineering talks on F1 CFD practice (mesh scales, OpenFOAM-based toolchains) — Tier 2/3, used qualitatively; see Engineering Audit for verification status.
