# PART XVII — Final Engineering Checklist

## "Can I Actually Understand F1 Aerodynamics Yet?"

Work through this list honestly. For each item: ✅ (explain it aloud, in your own words, with the mechanism), ⚠️ (partially — review needed), ❌ (not yet). For any ❌/⚠️, the right column names the prerequisite to revisit. Rule of thumb: you are ready for LEVEL 3 work (development reasoning, Part XV) when nothing is ❌ and fewer than five are ⚠️.

| # | Can I… | Prerequisite if not |
|---|---|---|
| 1 | Explain where aerodynamic forces come from (both mechanisms, and how they relate)? | Part II §2.1 |
| 2 | Explain a pressure distribution and integrate it (mentally) into force? | Part II §2.2 |
| 3 | Explain the boundary layer, its two states, and what depletes its momentum? | Part I §1.11, Part II §2.5 |
| 4 | Explain separation, its signature in Cf and Cp, and reattachment? | Part II §2.5, Part XIV §14.1–14.6 |
| 5 | Explain lift correctly — and refute "equal transit time" and "fast air = low pressure" as causes? | Part II §2.1 misconceptions |
| 6 | Explain drag's full taxonomy with an F1 example of each? | Part VIII §8.1 |
| 7 | Explain downforce as a purchase (the polar) and why maximum ≠ optimal? | Part III §3.2, Part VII §7.4 |
| 8 | Explain ground effect's two mechanisms and keep them separate? | Part V §5.1 |
| 9 | Explain the diffuser's job as pressure recovery, and what "stalled diffuser" means? | Part V §5.3 |
| 10 | Explain vortex generation (four mechanisms), sealing, and breakdown? | Part VI §6.2–6.3 |
| 11 | Explain the wheel wake's documented structure and why it dominates the car's flow? | Part IX §9.2 |
| 12 | Explain aero balance, why it travels with speed, and its handling consequences? | Part X §10.1–10.2 |
| 13 | Explain ride-height sensitivity using the force map's three regimes? | Part V §5.4 |
| 14 | Explain porpoising as a feedback loop (dF/dh + suspension)? | Part V §5.6 |
| 15 | Explain the CFD workflow end-to-end (15 stages) and why each exists? | Part XIII §13.1 |
| 16 | Read Cp plots, Q-criterion, TKE and streamlines — with their "cannot tell you" limits? | Part XIV |
| 17 | Explain convergence properly (monitors vs residuals) and numerical diffusion? | Part XII §12.7 |
| 18 | Explain mesh quality, refinement strategy and y⁺ bands (incl. the forbidden zone)? | Part XII §12.4, §12.6 |
| 19 | Explain RANS/URANS/LES/DES at a conceptual level — cost vs what's resolved? | Part XII §12.5 |
| 20 | Distinguish simulation, verification, validation and correlation? | Part XII §12.8, Part XI |
| 21 | Reason about a drag/downforce trade-off for a named circuit, quantitatively? | Part VII §7.4, Part VIII mini-problem |
| 22 | Form an aerodynamic hypothesis that is a *flow* statement, not a part statement? | Part XV §15.1 |
| 23 | Design a basic CFD investigation (policy, monitors, deltas, validation ladder)? | Part XIII, Part XV §15.2 |
| 24 | Explain why the tunnel measures a model, and how Reynolds mismatch is handled? | Part XI §11.2 |
| 25 | Explain the 2022 regulation philosophy (wake quality) and what it changed mechanically? | Part IV, Part VI §6.4, Part XV §15.3 |

---

## Scoring guide

- **All ✅ / few ⚠️:** you have the conceptual backbone the course will now fill with detail and practice. Move to working the mini-problems *without* looking at solutions, and start reading real Cp/Q-criterion figures (Part XIV checklist in hand).
- **⚠️ cluster in 1–14 (physics):** the fix is Parts I–II, slowly, with the misconception boxes — everything downstream is downstream for a reason.
- **⚠️ cluster in 15–23 (CFD/development):** the fix is Parts XII–XIV discipline; re-derive the y⁺ mini-problem and the convergence criteria until they're reflexes.
- **❌ anywhere:** revisit the named prerequisite *before* the part that depends on it (dependency table in Part XVI §16.3) — sequence matters more than speed.

## The one-paragraph final exam

If you can write this paragraph, with every clause defensible, you have what this handbook was built to give you:

> "An F1 car generates force by redistributing pressure over its surfaces (and paying skin friction), in a flow field constrained by a moving ground and contaminated by four rotating wheels' wakes. Its dominant device is a venturi underbody whose load depends on ride height through a non-monotonic force map, recovered by a diffuser, sealed by vortices, and coupled through suspension to vehicle dynamics — which is why balance travels with speed and why porpoising exists. Wings add load at induced-drag cost, so every setup is a circuit-specific purchase on the drag polar. Development is a hypothesis loop run across CFD, tunnel and track — three instruments, none of which is truth alone, ranked by how honestly their errors are known."

---

## SOURCES (Part XVII)

- Composite self-assessment; maps directly onto Parts I–XV.
