# PART XIV — Reading CFD Results

**Purpose:** teach engineering judgment over visualisation worship: for each standard output — what it *can* tell you, what it *cannot*, and what question it answers. The rule of the whole part: **a beautiful picture is a hypothesis generator; an integral is a decision-maker.**

**Course connection:** anchors: CFD post-processing chapters (Versteeg & Malalasekera ch. on solution interpretation is thin — pair with journal-figure reading); any Q-criterion/vertex-detection reference. Module mapping: ____________

---

## 14.1 Pressure coefficient (Cp) 🟡

**What it is:** the force currency made visible (Part II §2.2).

**Can tell you:**
- *Where* load is generated and where it is lost — suction peaks, recovery quality, separation signatures (a Cp plateau/flatline in the recovery region = stalled flow, Fig. 5.1 & 14.1).
- *Mechanism evidence*: did the new floor edge move the suction peak, or the recovery?
- Device-level integration sanity: $\int C_p \, dA$ ≈ the component force you measured.

![Attached vs separated pressure recovery.](diagrams/p14-cp-recovery.png)
*Figure 14.1 — The same expansion, two stories: recovery (green) vs stall (dashed). Cp traces diagnose separation before any picture does.*

**Cannot tell you:**
- Total merit without integration *over the real surface with real areas* — big local suction on a small patch ≠ big force.
- Anything about unsteadiness (steady RANS Cp is a frozen average).
- Comparison across plots with different colour scales — always normalise the legend range before comparing two designs.

---

## 14.2 Velocity contours 🟡

**Can tell you:** where the flow is fast/slow (mass-flow squandered or delivered), wake extents, jetting, throttle-like behaviour of ducts; good for *spatial bookkeeping* (is the tunnel fed?).

**Cannot tell you:** whether the design is better. Two designs can swap slow/fast regions while their integrals move oppositely. Colour maps also exaggerate: human eyes read saturated red/blue as "important". And a slice hides the third dimension — a beautiful slice can sit inside an ugly volume (always ask "what's out of plane?").

---

## 14.3 Streamlines and particle tracks 🟡

**Can tell you:** topology of transport — what feeds what (FW → fences; diffuser → beam wing), where flow *originating* somewhere ends up. Surface-restricted streamlines (limiting streamlines) are the *separation map*: converging lines mark separation, diverging mark attachment.

**Cannot tell you:** time history (in steady RANS they are solution-integral curves, not particle paths); vorticity content (a streamline can pass through a vortex without showing it); "the flow pattern" — seeding/cropping choices manufacture stories. In unsteady data, instantaneous streamlines are not paths at all (Part I §1.10).

---

## 14.4 Vorticity and Q-criterion 🟡→🔴

**Vorticity magnitude:** shows rotation rate density — wakes, shear layers, vortex cores. **Caveat:** vorticity is a *vector* — magnitude maps hide direction/structure, and shear layers (velocity gradients) light up too, not just real vortices.

**Q-criterion (iso-surfaces):** the standard vortex identifier — regions where rotation dominates strain. The workhorse for the Part VI inventory (edge vortices, wake CVPs, outwash).

**Can tell you:** structure *location/coherence*: did the floor-edge vortex survive? Did the wake pair merge? Where does the outwash land?

**Cannot tell you:** strength without additional measurement (circulation — integrate velocity around the core), and *importance*: threshold choice manufactures the picture (a lower iso-threshold "finds" more vortices). Compare two designs at the *same* threshold and with circulation numbers, or you are comparing art.

---

## 14.5 Turbulent kinetic energy (TKE) 🟡

**Can tell you:** where the model expects unsteadiness/mixing — wake cores, separation zones, the "dirty air" map (Part VIII Fig. 8.1). In RANS, TKE is *modelled*, not measured: it is the model's opinion of fluctuation energy.

**Cannot tell you:** actual spectra or frequencies (RANS has none), and validity in sensitive regions depends on the turbulence model's honesty (Part XII). Following-car studies live or die on TKE plausibility — which is exactly why the 2022 wake-robustness claims needed validation beyond pretty TKE blobs.

---

## 14.6 Wall shear stress / Cf 🟡

**Can tell you:** separation and reattachment *precisely* (Cf crossing zero — Part II §2.5); transition treatment effects; where the boundary layer is healthy (positive, finite Cf).

**Cannot tell you:** forces by itself (shear is a minor part of drag, Part VIII) — it is a *diagnostic* of flow state, not a scoreboard. Also mesh/y⁺-sensitive: a wall-function mesh makes near-wall shear semi-quantitative at best (Part XII §12.6).

---

## 14.7 Force coefficients and integrals 🔴

**Downforce, drag, moments, balance** — the decision quantities. Rules of professional use:

1. **Deltas, not absolutes:** ΔC_L A vs a validated baseline, per component and total.
2. **With uncertainty:** mesh/GCI band + convergence window + repeatability noise (Parts XII–XIII) — a delta below its own error bar is a rumour.
3. **Across the map:** a delta that exists only at nominal attitude is a mirage (Parts III, V, X).
4. **With mechanism:** what changed in the pressure/vortex story explains the integral — otherwise you may be optimising noise or a mesh artifact.

**ENGINEERING INTUITION**
> If you remember only one thing: every plot is a *claim*, and every claim needs its error bar and its mechanism. The professional question is never "which picture looks better?" but "which delta survives uncertainty, and what physics explains it?"

---

## 14.8 The interpretation checklist (use it on every result) 🔴

1. What was the hypothesis? (If there wasn't one, stop.)
2. Are the deltas above the noise floor? (repeatability, GCI, convergence window)
3. Did anything change upstream that shouldn't have? (mesh policy, BCs, iteration count)
4. What is the mechanism? (Cp moves, vortex path, wake change — one consistent story)
5. Does it survive attitude? (2–3 map points minimum)
6. What does the tunnel/track ladder need to confirm it? (Part XIII §14)

---

## COMMON MISCONCEPTIONS (Part XIV)

> ❌ **"A cleaner-looking wake means a better car."** Not necessarily — the wake's *content* (momentum, vorticity, where it lands) matters more than its appearance.
>
> ❌ **"Q-criterion pictures show downforce."** They show coherent rotation. A car can gain load with fewer visible structures or lose it with more.
>
> ❌ **"Velocity contours prove flow is faster = better."** Faster where, fed by what, at what pressure cost? Local speed is not merit.
>
> ❌ **"The colour scale is neutral."** Legend range, slicing plane and seeding are editorial choices. The same solution can be made to look brilliant or broken.
>
> ❌ **"RANS TKE map = measured turbulence."** It is the turbulence model's estimate — an opinion with assumptions (Part XII §12.5).
>
> ❌ **"Surface streamlines show particle paths."** In steady solutions they are integral curves of the surface shear field; separation lines yes, trajectories no.

---

## F1 ENGINEERING QUESTIONS (Part XIV)

**Conceptual**
- Why is Q-criterion threshold choice an editorial act, and how do you make it defensible?
- Why can a Cp plot reveal stall that a force monitor misses until later?

**Engineering**
- Two floors: A gains 1.2% load with a messier wake; B gains 0.9% with a cleaner wake. Define the data that picks the winner for (a) single-car pace, (b) race pace in traffic.
- Your new FW shows equal load, lower drag, and a shifted outwash. What downstream checks before you celebrate?

**CFD**
- Build the minimal post-processing set (5 outputs) that supports or kills the hypothesis "the edge vortex seals better at low ride height".
- How would you quantify circulation of the floor-edge vortex from your solution?

**Design**
- A sponsor asks for "a picture that shows the upgrade is better". What do you send instead, and why?
- You suspect a beautiful new wing result is mesh-driven. Design the two-run experiment that settles it.

---

## QUICK RECALL (Part XIV)

1. Which plot diagnoses separation *earliest*, and what signature do you look for?
2. What three pieces of data turn a Q-criterion image into engineering evidence?
3. Why are steady-RANS streamlines not particle paths?
4. What does a Cp plateau in a recovery region mean?
5. Why must legend ranges match before comparing Cp plots?
6. What is RANS TKE, epistemically?
7. Why is wall shear a diagnostic rather than a scoreboard?
8. Define the four properties of a decision-grade delta.
9. What does a slice hide, and what do you always ask?
10. Which output would you *never* use alone to approve a design, and why?

### ANSWERS

1. Wall shear / surface limiting streamlines: Cf→0, converging separation line — earlier and more local than force monitors.
2. Same threshold between designs; a strength measure (circulation); the associated force/pressure change.
3. They are integral curves of an instantaneous (frozen) field; unsteady reality has no such fixed paths.
4. The expansion has separated — recovery stalled (Figs. 5.1, 14.1).
5. Otherwise you compare colour scales, not physics; renormalise to common Cp limits.
6. The turbulence model's estimate of fluctuation energy — modelled opinion, not measurement.
7. Shear's contribution to force is small; its value is flow-state diagnosis (separation/attachment).
8. Above noise floor; at matched policy; across attitudes; with an explained mechanism.
9. The third dimension/out-of-plane gradients — ask "what does the volume integral say?"
10. Any single picture (Q-criterion, contours, streamlines) — pictures are claims; only integrals + mechanism + validation approve designs.

---

## SOURCES (Part XIV)

- Versteeg, H. K. & Malalasekera, W. (2007) — solution interpretation practice. [Tier 1]
- Ferziger, J. H. & Perić, M. (2002) — error-aware post-processing. [Tier 1]
- Jeong, J. & Hussain, F., "On the identification of a vortex", *J. Fluid Mech.* 285 (1995) — the Q-criterion's origin and caveats. [Tier 1]
- Toet, W. (2013), *The Aeronautical Journal* — how F1 consumes flow-field diagnostics. [Tier 2]
