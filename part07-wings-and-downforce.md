# PART VII — Wings and Downforce

**Purpose:** connect airfoil theory to the specific, regulated, low-aspect-ratio, multi-element wings of F1 — and to the drag/downforce trade that defines every setup sheet.

**Course connection:** anchors: Anderson ch. 4 (thin-airfoil theory), ch. 5 (finite wings, induced drag); Katz ch. 5; McBeath ch. on wings. Module mapping: ____________

---

## 7.1 Airfoil theory in one page 🟢→🟡

For a 2-D airfoil in incompressible flow:

- **Thin-airfoil result:** $c_l = 2\pi(\alpha - \alpha_{L0})$ ($\alpha$ in radians), where $\alpha_{L0}$ is the zero-lift angle — set by **camber**. Inverted camber ⇒ negative $\alpha_{L0}$ ⇒ downforce at zero geometric α.
- **The pressure side / suction side picture** (Part II, Fig. 2.1) — all of the load comes from the $C_p$ difference between the two surfaces; the suction side usually dominates.
- **Limits:** at high $\alpha$ (or high flap deflection) the suction peak's adverse gradient defeats the boundary layer → separation → stall (Part II §2.5).
- **Circulation view:** $l' = \rho V \Gamma$; the starting vortex and Kelvin's theorem explain where $\Gamma$ comes from. (You don't need the mathematics — you need the causal chain.)

**2-D vs 3-D — the tax of finite span.** A 2-D section achieves its ideal $c_l$; a real finite wing sheds a trailing vortex system (Part VI) that tilts the local flow downward (**downwash**) and adds **induced drag**:

$$C_{D,i} = \frac{C_L^2}{\pi e \, AR}, \qquad AR = \frac{b^2}{S}$$

| Variable | Meaning | Units |
|---|---|---|
| $b$ | span | m |
| $S$ | planform area | m² |
| $e$ | span-efficiency factor (≤ 1; elliptic loading = 1) | — |

*Assumptions:* linear theory, moderate $C_L$, no separation. *Meaning:* induced drag grows with the *square* of load and falls with aspect ratio. *F1 application:* regulations limit span severely, so F1 wings are **low-AR** devices with heavy induced-drag taxes — a primary reason the car's overall L/D is ~3 and why endplates and edge shaping matter so much.

**Endplates — what they do and don't do.** They do not eliminate induced drag; they modify tip flow, allow deliberately strong edge vortices to be placed usefully, and (historically) support outwash shaping. Modern endplate design is as much about the *vortex path* as the plate itself.

---

## 7.2 Multi-element wings: boundary-layer management 🟡→🔴

A single highly cambered element stalls long before useful F1 loads. The solution is **slotted multi-element geometry**:

![Multi-element wing with slot flow.](diagrams/p07-multielement.svg)
*Figure 7.1 — The slot: cove pressure drives a jet into the next element's boundary layer, delaying separation and letting each element carry more load.*

Mechanism, in physics order (this corrects the folk version):

1. The cove between elements is a **high-pressure stagnation region** (the flow decelerates into the slot's mouth).
2. That pressure drives air through the converging slot (continuity + momentum).
3. The **slot jet re-energises** the next element's boundary layer with momentum, delaying separation (Fig. 7.2 shows the velocity profiles).
4. Each element also *changes the effective flow direction* seen by the next (the cascade/interaction effect) — total circulation exceeds what any element could produce alone.
5. Result: element loads of 2–3× a single element's practical limit, at the cost of friction area, junction losses, and sensitivity (gap dimensions are critical — and heavily regulated).

![Slot re-energisation velocity profiles.](diagrams/p07-slot-profiles.png)
*Figure 7.2 — The slot's job in one picture: replace a starving boundary layer with one that has momentum to spend.*

**COMMON MISCONCEPTIONS (multi-element)**
> ❌ **"Slots work by restarting Bernoulli between elements."** Nothing "restarts"; the slot is a momentum *injection* device for a boundary layer (Part II §2.5). No slot, no high load — the flap separates.
>
> ❌ **"More elements = always more load."** Each element adds friction, junction and interference losses, and moves the stall mode to a new failure (flap stall, crossflow). Element count is regulated anyway.
>
> ❌ **"The flap only adds camber."** The flap also sets the slot jet, the cove pressure and the main-element loading — a change in flap angle reshuffles the *whole* pressure distribution.

---

## 7.3 F1 front and rear wings, concretely 🟡

**Front wing (current era, simplified by regulation — element count limited, neutral central section mandated).** Works close to the ground → wing-in-ground-effect physics (Part V Mechanism A) plus outwash duties (Part IV). Design tensions:
- Load vs. floor feeding: the strongest FW is not the best FW (Part IV §4.4).
- Ride-height sensitivity: FW load rises sharply as it nears the ground — a primary front-balance control (Part X).
- Kerb/attitude robustness: the wing must survive pitch/roll excursions without stalling.

**Rear wing.** Low aspect ratio (span regulated, ~limited to roughly 1 m class — check current dimensions), heavily loaded, the largest single drag item. The endplate is shaped to manage the tip vortex and interface with the beam-wing upwash. **DRS** rotates the flap open (gap regulated — 85 mm class; verify current figure in the regulations) to flatten the element and shed most of its load and drag: rear-wing drag reductions of order 50–80% are reported in open studies of DRS-type devices, with total-car drag cuts of tens of percent and lap-time gains of several tenths per lap (public/academic estimates — see sources). DRS also *changes the wake* — part of its racing effect beyond top speed.

**Gurney flaps.** A small right-angle strip at the trailing edge: increases trailing-edge loading (effectively higher circulation) cheaply, at a drag cost. A classic fine-trim tool for balance and load micro-adjustment.

---

## 7.4 The trade-off, quantitatively 🟡

The setup question — "how much wing for this circuit?" — is a lap-time integration problem. With total force coefficients dominated by the wing settings' contribution to $\Delta C_L A$ and $\Delta C_D A$:

- Fast circuits (long full-throttle fractions): drag costs top speed *every* straight; downforce helps only in a few corners ⇒ run low wing (Monza extreme).
- Slow/twisty circuits: downforce helps *every* corner, drag costs little ⇒ run maximum legal load (Monaco, Hungary).
- Everything else: optimise the power-limited/aero-limited balance per corner cluster; add tyre-degradation effects (more load = more lateral force = also more tyre energy).

**ENGINEERING INTUITION**
> If you remember only one thing: a wing setting is a *purchase*, and drag is the price tag. The aerodynamicist's job is not "maximum downforce" — it is buying each corner's grip at the cheapest possible straight-line price, under the regulations.

---

## F1 ENGINEERING QUESTIONS (Part VII)

**Conceptual**
- Why does induced drag scale with $C_L^2$? Explain with the trailing-vortex kinetic-energy picture.
- Why do F1 wings tolerate low aspect ratios that would be absurd on an aircraft?
- What physically limits how much load a multi-element wing can carry?

**Engineering**
- You need +2% rear load for one fast corner without losing top speed elsewhere. Candidates: main plane, flap angle, Gurney, beam wing. Rank them by drag-per-downforce and explain.
- DRS feels "lazier" on a high-downforce wing setting. Why?

**CFD**
- How would you verify the slot jet is working in your CFD post-processing? (Name two checks.)
- What does an induced-drag breakdown look like in CFD terms — which surface/region would you interrogate?

**Design**
- A rival's front wing generates equal load with visibly less span. What are three possible mechanisms?
- Design a rear wing "DRS-stratified" for a circuit with two DRS zones of different lengths — what geometry decisions follow?

---

## MINI PROBLEM (Part VII)

**Problem — The price of a wing trim**
*Given:* car at 300 km/h ($V = 83.3$ m/s, $q = 4{,}253$ Pa); a rear-wing trim adds $\Delta(C_L A) = 0.25\ \text{m}^2$ of downforce at a drag price $\Delta(C_D A) = 0.06\ \text{m}^2$. Car mass 800 kg, wing contributes to a corner where the lateral demand is $3.5g$.
*Required:* (a) extra downforce and drag force at 300 km/h; (b) is the trade "profitable" in the corner (does the added grip exceed the added drag penalty)? (c) At what speed does the extra drag equal 3% of the added downforce value?
*Solution:*
(a) $\Delta F_{DF} = q\,\Delta(C_L A) = 4{,}253 \times 0.25 \approx 1.06\ \text{kN}$; $\Delta D = 4{,}253 \times 0.06 \approx 255\ \text{N}$.
(b) In the 3.5g corner at some speed $V_c$, added grip $\approx \Delta F_{DF}$ (grows with $V_c^2$) vs added drag $\Delta D$ (also grows with $V_c^2$, but the *drag* only needs ~0.7 kN-scale to matter at top speed). At 250 km/h: $\Delta F_{DF} \approx 0.74$ kN of extra lateral capacity vs 178 N extra drag — the corner profits; on a straight the same trim costs ~178–255 N ≈ several km/h of top speed. The trade is circuit-dependent, exactly as §7.4 says.
(c) Engineering interpretation: trim decisions are made in this currency — kN of corner grip per 100 N of straight-line drag. The numbers above are illustrative orders of magnitude; real teams compute exactly this, per corner, per circuit.

---

## QUICK RECALL (Part VII)

1. Write the thin-airfoil lift relation; what sets $\alpha_{L0}$?
2. Write the induced-drag formula and explain each term's F1 implication.
3. What are the two effects that make multi-element wings work?
4. What does a Gurney flap do, mechanically?
5. Why is the front wing called the "thermostat" of the flow system?
6. What does DRS change, physically — list four effects.
7. Why is endplate design about vortex paths, not just blocking leakage?
8. Rank: which wing trim buys load cheapest in drag terms, and why?
9. Why does the optimum wing level differ between Monza and Hungary?
10. What limits a flap's load, and how does the slot postpone that limit?

### ANSWERS

1. $c_l = 2\pi(\alpha - \alpha_{L0})$; $\alpha_{L0}$ is set by camber (inverted camber → downforce at zero α).
2. $C_{D,i} = C_L^2/(\pi e AR)$: load² — F1 wings are heavily loaded; low regulated AR and low $e$ — big tax; hence floor-centric load generation.
3. Slot jet re-energises the next element's boundary layer (separation delay) + cascade interaction (each element sees modified effective flow).
4. A TE right-angle plate raising circulation/trailing-edge loading — cheap load, costs drag.
5. Its outwash and feed decide what every downstream device receives.
6. Flattens the flap: big rear drag cut; rear load drops; rear wake changes shape; rear axle unloads (handling + overtaking effects).
7. The edge vortex's *placement* does useful work (outwash, sealing); the plate just hosts it — designers shape where the vortex goes.
8. Generally beam wing / floor-adjacent devices (they add load with less direct free-stream drag and feed the rear wing) over main-plane/flap increases — hence "floor first" is the modern doctrine.
9. Corner-to-straight ratio: Hungary's corners reward load everywhere; Monza's straights punish drag everywhere.
10. Suction-peak adverse gradient defeating the boundary layer (stall); the slot injects momentum into that layer, postponing separation to higher loads.

---

## SOURCES (Part VII)

- Anderson, J. D., *Fundamentals of Aerodynamics*, McGraw-Hill (6th ed., 2017) — thin-airfoil theory, finite-wing/induced-drag theory. [Tier 1]
- Zhang, X. & Zerihan, J., "Aerodynamics of a Double-Element Wing in Ground Effect", *AIAA Journal* 41(6), 2003 — multi-element ground-effect loads; flap contributes 15–25% of total. [Tier 1]
- Katz, J., *Race Car Aerodynamics*, Bentley (1995) — race-car wing design, Gurney flaps, multi-element practice. [Tier 1]
- McBeath, S., *Competition Car Aerodynamics*, Veloce (3rd ed., 2015) — practical wing/trim development. [Tier 2]
- Loução, R. et al., "Aerodynamic Study of a Drag Reduction System…", *Fluids* (MDPI) 7(9):309, 2022; and Monash DRS studies — DRS drag/downforce magnitudes (wing-level ~50–80% drag cut; total-car estimates lower). [Tier 2]
- FIA Formula 1 Technical Regulations, Art. 3 — wing geometry, element counts, DRS aperture. [Tier 1]
