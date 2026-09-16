# PART III — From Aircraft Aerodynamics to Race-Car Aerodynamics

**Purpose:** rebuild your mental model from "wing in clean air" to "bluff, lifting, wheeled body flying one tyre-width off a moving wall in its own turbulence". Almost every F1-specific concept — ride height, rake, aero balance, dirty air — exists because of the differences catalogued here.

**Course connection:** anchors: Katz ch. 1, 4–5; Hucho ch. on vehicle aerodynamics fundamentals; Barnard ch. on road-vehicle/racing aerodynamics. Module mapping: ____________

---

## 3.1 Negative lift: the inverted objective 🟢

An aircraft *minimises* weight at fixed lift. A race car wants the opposite: **maximum normal load on the tyres without paying mass**. Aerodynamic downforce is "free mass" that scales with $V^2$, so it arrives exactly where it's needed — in fast corners — and disappears on straights (where it would cost acceleration).

$$F_{downforce} = \tfrac12 \rho V^2 \, (C_L A)$$

With $C_L A \approx 4\ \text{m}^2$ (public-order estimate), downforce equals the car's own weight (~7.85 kN) at roughly:

$$V = \sqrt{\frac{2mg}{\rho C_L A}} = \sqrt{\frac{2 \times 7.85\times10^3}{1.225 \times 4}} \approx 57\ \text{m/s} \approx 205\ \text{km/h}$$

(approximate; setup- and regulation-dependent). Beyond that speed, the tyres carry multiple times the car's static weight — which is why high-speed cornering in F1 is an *aerodynamic* activity and low-speed cornering a *mechanical* one.

---

## 3.2 The drag/downforce trade-off 🟡

Downforce and drag are not independent products; both are integrals over the same pressure and shear fields, driven by the same momentum exchange. Pushing more mass flow faster (floor) or loading wings more inherently increases the energy left in the air (wake/vortex kinetic energy = drag).

The governing engineering object is the **drag polar** — downforce area versus drag area over the setup range:

![Illustrative drag polar of an F1 car.](diagrams/p07-polar.png)
*Figure 3.1 — Each point is a wing/floor setting. Lap time, not downforce, is the objective: the right point depends on the circuit's straights and corners (Part VII).*

The trade-off is *why* aerodynamic development is an optimisation under constraints (regulations, cooling, stability) rather than a maximisation.

---

## 3.3 Ground proximity — the defining difference 🟡

An aircraft wing operates against the atmosphere "at infinity". An F1 car operates a few centimetres above a solid wall moving relative to it (in the car's frame, the road is a moving wall). Consequences:

1. **Underbody flow is forced through a converging–diverging channel** (floor tunnels, diffuser) — ground effect (Part V).
2. **Leakage paths are limited**, so underbody suction can be maintained — modern cars re-seal the edges with vortices where 1970s cars used physical skirts.
3. **The whole force map becomes a function of ride height, pitch, roll and yaw** — the car's *attitude* is an input to the aerodynamics, not just a result of them.

This is the deepest structural difference from aircraft aerodynamics: **the F1 car's aerodynamics is a closed loop with its suspension.**

---

## 3.4 Vehicle attitude: heave, pitch, roll, yaw 🟡

| Attitude | Definition | Primary aerodynamic consequence |
|---|---|---|
| Heave | uniform vertical motion/ride-height change | underbody volume changes → total load changes (strongest sensitivity) |
| Pitch | front vs rear ride-height difference (rake) | redistributes underbody expansion; shifts load front↔rear |
| Roll | lateral ride-height difference | one floor-edge seal opens, other tightens → balance shift |
| Yaw | car axis vs velocity vector | crossflow under/around the car; asymmetric wakes; edge-vortex weakening |

**F1 application:** teams measure full **aero maps** — force and moment coefficients over a matrix of heave/pitch/roll/yaw — in the tunnel and in CFD. A component that only works at one attitude is a liability; **robustness across the map** is a core design currency (Parts XI, XV).

---

## 3.5 Tyre loading: why downforce buys cornering speed 🟡

Tyre lateral force $F_y \approx \mu \, N$: grip scales with normal load $N$. Downforce raises $N$, so cornering speed for a given lateral limit rises:

$$a_{y,max} \approx \frac{\mu (mg + \tfrac12\rho V^2 C_L A)}{m}$$

The loop closes: $V \uparrow \Rightarrow$ downforce $\uparrow$ (with $V^2$) $\Rightarrow$ grip $\uparrow$ — fast corners are "aero-dominated" (lateral accelerations publicly quoted at 4–5 g in the fastest corners, vs ~1.5–2 g purely mechanical).

Two subtleties that make this engineering rather than arithmetic:

- **Tyre load sensitivity:** $\mu$ *falls* as load rises — grip grows sub-linearly with downforce. This shapes everything from weight distribution to aero balance (Part X).
- **Load transfer:** longitudinal/lateral acceleration shifts load between tyres; the aero pitch moment (drag acting above the ground, downforce distribution fore/aft) modifies that transfer at speed.

---

## 3.6 Centre of pressure, centre of mass, aero balance 🟡

![Force system on an F1 car.](diagrams/p03-force-diagram.svg)
*Figure 3.2 — Weight acts at the CG; downforce acts at the centre of pressure (CoP); drag acts at an effective height. Their relative positions create moments that re-distribute tyre load with speed.*

- **Centre of mass (CG):** fixed by mass distribution (regulated minimum weight ~800 kg, current era — approximately, FIA figures; see Part IV sources).
- **Centre of pressure (CoP):** where the *total* aero force effectively acts. Its fore/aft position defines the **aero balance** (% of downforce on the front axle).
- The lever arm between CoP and CG, plus drag height, sets the aero pitch moment: at speed, braking stability, traction and steering feel all carry an aerodynamic contribution.

**Why the car is not simply "an upside-down airplane" — the compact list:**

1. The lifting surface that matters most (floor) is a *channel between two walls*, not a free wing; its performance is ride-height physics, not airfoil physics alone.
2. Wings operate at low aspect ratio, in **wakes from wheels and other components** — the inlet flow quality of every downstream device is a design variable.
3. Four exposed, rotating wheels create the dominant wakes and a large drag share; no aircraft has this problem.
4. The force map is **coupled to suspension state** (attitude), creating stability problems (porpoising) with no aircraft equivalent.
5. The optimisation target is lap time under strict geometric regulation — the designer shapes a *system*, not a wing.
6. Downstream devices must also *condition the wake* for the car behind (overtaking), a constraint no aircraft ever had.

---

## COMMON MISCONCEPTIONS (Part III)

> ❌ **"An F1 car is an upside-down airplane."** As a slogan, misleading: the load path (tyres), the ground plane, the wheels, the wakes and the suspension coupling make it a different discipline that merely shares equations.
>
> ❌ **"Downforce is always good."** It costs drag, tyre energy and mechanical stress; and above the underbody's stable range more load can trigger instability (Part V).
>
> ❌ **"Aero balance is fixed by the wing sizes."** It moves with speed (ride heights change), attitude (pitch/roll/yaw), and every upstream component's wake. Balance is a *map*, not a number (Part X).
>
> ❌ **"More downforce means more grip, linearly."** Tyre load sensitivity makes grip sub-linear in load — part of why the sport obsesses over *efficiency* of load generation, not just quantity.
>
> ❌ **"Drag only slows the car on straights."** Drag also unloads the car (high-speed traction), heats tyres, and its wake degrades following cars — part of the racing problem, not just the lap-time one.

---

## F1 ENGINEERING QUESTIONS (Part III)

**Conceptual**
- Why does a car that is "aero-limited" in fast corners still accelerate slower if you add drag-heavy downforce?
- Physically, why does yaw degrade floor performance more than it degrades a free wing's performance?

**Engineering**
- Given a fixed power, how would you decide between +2% $C_L A$ and −2% $C_D A$ for Monza? For Hungary? (Quantify with a lap-time argument.)
- What suspension properties would you choose to stabilise a car whose downforce curve steepens as ride height falls?

**CFD**
- Why must CFD of an F1 car be run over a matrix of attitudes rather than one "nominal" position?
- Which attitude variable would you sweep to understand roll behaviour of the floor-edge vortices?

**Design**
- A new floor adds downforce only below 150 km/h. Is that useful? Design a test to find where the load is going.
- If drag is acting too high (excessive pitch moment under braking), which components would you examine first?

---

## QUICK RECALL (Part III)

1. At approximately what speed does a modern F1 car's downforce equal its weight? What does that imply for fast corners?
2. Name four attitude variables and their dominant aerodynamic effects.
3. Why is the drag polar the "price list" of the sport?
4. Define aero balance; why is it speed-dependent?
5. How does tyre load sensitivity modify the naive "downforce = grip × μ" reasoning?
6. List three reasons "upside-down airplane" fails as a mental model.
7. What is an aero map and why is robustness across it valuable?
8. How does ground proximity change the underbody flow topology vs a free wing?
9. Why do fast corners produce 4–5 g but slow corners cannot?
10. Where does the drag force act relative to the ground, and why does that height matter?

### ANSWERS

1. Roughly 180–210 km/h depending on setup ($C_L A$ ≈ 3.5–5 m², public estimates). Fast corners are aero-dominated: grip available grows with $V^2$.
2. Heave — underbody volume/load; pitch (rake) — load shift + expansion geometry; roll — edge-seal asymmetry; yaw — crossflow, asymmetric wakes, weakened edge vortices.
3. Every downforce gain must be bought with drag (and tyre/cooling costs); the polar is the menu of legal trades.
4. Fraction of downforce on the front axle; moves with speed because ride heights/pitch change with aero load, shifting floor vs wing contributions.
5. μ decreases with load ⇒ grip rises sub-linearly ⇒ efficient (not just large) load generation matters; also sets balance targets.
6. Floor is a channel in ground proximity; wings work in wheel/component wakes; suspension-coupled force map (+ low AR wings, wake conditioning for racing, regulated shape).
7. Coefficients sampled over heave/pitch/roll/yaw; a component robust across the map survives real cornering, kerbs and fuel-load changes.
8. It creates a converging–diverging underbody channel with mass-flow/pressure coupling; leakage and edge sealing become first-order.
9. Fast corners have large $V$, so aero downforce multiplies tyre normal load far beyond the car's weight; slow corners have little aero load (μmg only).
10. At an effective height above the ground (roughly the aero force centroid); its moment about the contact patches redistributes wheel loads under acceleration/braking.

---

## SOURCES (Part III)

- Katz, J., *Race Car Aerodynamics*, Bentley (1995) — downforce/trade-off fundamentals, load sensitivity, attitude effects. [Tier 1]
- Hucho, W.-H. (ed.), *Aerodynamics of Road Vehicles*, SAE — bluff-body aerodynamics, ground proximity, attitude sensitivity. [Tier 1]
- Barnard, R. H., *Road Vehicle Aerodynamic Design*, MechAero — accessible treatment of vehicle vs aircraft differences. [Tier 2]
- FIA Formula 1 Technical Regulations (current) — mass and dimension limits cited as approximate. [Tier 1]
- Public team/press estimates of $C_L A$, $C_D A$, lateral g — used as ranges only (Tier 3, marked as estimates).
