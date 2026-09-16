# PART VIII — Drag

**Purpose:** a proper taxonomy of drag, an honest account of where an F1 car's drag actually comes from, and why "make everything smaller" is not a drag-reduction strategy.

**Course connection:** anchors: Anderson ch. 1 (drag categories) + ch. on boundary layers (friction/form split); Hucho (vehicle drag decomposition); Katz ch. 4–5. Module mapping: ____________

---

## 8.1 The taxonomy 🟢→🟡

| Category | Mechanism | Scales with | F1 relevance |
|---|---|---|---|
| **Pressure (form) drag** | Boundary-layer separation leaves a low-pressure wake; integrated pressure imbalance | frontal area, separation extent | dominant on wheels, bodywork, any stalled component |
| **Skin-friction drag** | Wall shear $\int \tau \, dA$ | wetted area, $Re$, transition state | real but secondary at car scale; matters on clean surfaces |
| **Induced drag** | Trailing-vortex kinetic energy (finite-span lift tax) | $C_L^2/AR$ | heavy: low-AR wings, heavily loaded floor edges |
| **Interference drag** | Junctions, close-proximity components; merging boundary layers/wakes | local geometry | everywhere: wing-body junctions, suspension, endplate/floor intersections |
| **Wave/compressibility drag** | Shocks, compressibility losses | $Ma \to 1$ | essentially absent at F1 free-stream Mach (~0.3 max) |

Total drag splits *functionally* too — never forget the second axis:

$$D = D_{\text{wings}} + D_{\text{wheels}} + D_{\text{body}} + D_{\text{cooling}} + D_{\text{induced}} + \ldots$$

Because the car is a system, these terms are coupled: cooling flow exits into the floor feed; wing wake changes what the diffuser swallows; wheel wakes load the floor edge.

---

## 8.2 Where F1 drag actually comes from 🟡

**Wheels and their wakes.** Four exposed, rotating, open wheels — each a bluff body with massive separation. Open literature on isolated racing wheels shows drag coefficients of order 0.5–1 depending on configuration; wheels and their wakes are widely regarded as a leading share of total car drag (public technical consensus; exact team splits are confidential). Rotation changes the wake (Part IX).

**Wings (especially the rear wing).** Low-AR, heavily loaded — large induced drag plus the profile drag of elements working near their limits. The rear wing alone can be a double-digit percentage of total drag (order-of-magnitude, public estimates).

**Cooling.** The internal flow path pays three times: momentum lost at the inlet (ram capture), pressure loss through radiators/ducts, and exit momentum deficit/wake. Cooling drag is a genuine fraction of total drag, and its size is a design choice (inlet/exit sizing, Part IV).

**Bodywork & interference.** Separation on the engine cover, mirrors, halo, suspension legs, crash structure; junction flows at every intersection; the "coke-bottle" waist exists precisely to reduce these losses where the flow must accelerate and turn.

**The wake as drag.** The momentum deficit left behind the car (Fig. 8.1) *is* the drag, seen from the momentum viewpoint (Part II §2.1): the engine's thrust work is the kinetic energy and heat left in the air.

![Wake velocity deficit and turbulence.](diagrams/p08-wake-deficit.png)
*Figure 8.1 — Drag from downstream: the momentum deficit is the bill; the turbulence is the "dirty air" that punishes the car behind.*

**ENGINEERING INTUITION**
> If you remember only one thing: drag is the energy you leave in the air. Every watt the engine makes that doesn't push the car forward ends up as heat and turbulence in the wake — the drag audit is an energy audit.

---

## 8.3 Why "make everything smaller" fails 🟡

1. **Wheels are fixed** by regulation — the biggest bluff bodies can't shrink.
2. **Cooling must pass a budget** — starve it and you lose power or the race; the optimum is a designed compromise, not zero.
3. **Flow conditioning needs geometry** — bargeboards (historically), fences, and edge wings *added* area but *reduced* total drag by keeping downstream devices attached. Local area is not total drag.
4. **Downforce is purchased with drag** (Part VII) — the induced-drag term is the *product* working.
5. **Separation beats size** — a small separated component can drag more than a large attached one. Surface shaping (pressure recovery) is the tool, not shrinking.

---

## F1 ENGINEERING QUESTIONS (Part VIII)

**Conceptual**
- Explain why induced drag is largest exactly where downforce is largest.
- Why does a separated flap produce *more* drag and *less* load than an attached one at higher deflection?
- What is the momentum-view definition of drag, and how does an aero rake exploit it?

**Engineering**
- Monza trim: list three drag sources you'd attack first and what each risks.
- Your cooling exit flow merges with the rear-tyre wake. Quantify conceptually the three losses you're paying.
- Why can adding a component (e.g., a small strake) *reduce* total drag?

**CFD**
- How would you decompose CFD drag by component and by mechanism (pressure vs friction vs induced)?
- What does an interference-drag audit look like in CFD? (Two bodies run separately vs together — what's the bookkeeping?)

**Design**
- The rear wing is 15% of total drag. Design two mechanisms to cut it without losing the corner it was bought for.
- A new mirror design saves 0.4% total drag but dirties the sidepod inlet flow. What data decides "keep or kill"?

---

## MINI PROBLEM (Part VIII)

**Problem — Power to overcome drag**
*Given:* $C_D A = 1.4\ \text{m}^2$ (mid-trim, public-order estimate), $\rho = 1.225$, speed 320 km/h (88.9 m/s). Ignore rolling resistance.
*Required:* (a) drag force; (b) power to overcome it; (c) top-speed sensitivity: how much extra speed does −2% $C_D A$ buy at fixed power?
*Solution:*
(a) $D = q\,C_D A = 0.5\times1.225\times88.9^2\times1.4 \approx 6.8\ \text{kN}$.
(b) $P = D \cdot V = 6.8\times10^3 \times 88.9 \approx 605\ \text{kW}$ — of order the total deployed power of a current power unit, which tells you the estimate class is right (rolling resistance and drivetrain losses add more).
(c) At fixed power $P = \tfrac12\rho C_DA\, V^3$: $V_{new}/V = (0.98)^{-1/3} \approx 1.0068$ ⇒ ~0.7% ≈ +2.3 km/h at 320. One to two car lengths per straight.
*Engineering interpretation:* cubic velocity scaling makes drag the currency of top speed; a 2% drag cut is worth more than most single-corner downforce gains at Monza-class circuits — and *less* at Hungary-class circuits. That asymmetry is the entire wing-level debate, quantified.

---

## QUICK RECALL (Part VIII)

1. Name the five drag categories and one F1 example of each (or note absence).
2. What is the momentum definition of drag, and how is it measured without touching the car?
3. Rank the F1 drag sources by likely share and justify the top item.
4. Why is cooling drag a "three-time payment"?
5. Why can added geometry reduce total drag?
6. What does the $V^3$ power law imply about trim choices for Monza?
7. Where does the engine's drag work end up, thermodynamically?
8. Why are wheels' wakes both a drag and a racing problem?
9. What is interference drag, physically?
10. Why is "smaller = less drag" a non-strategy in F1?

### ANSWERS

1. Pressure/form (wheels, stalled parts), skin friction (clean surfaces), induced (loaded low-AR wings/floor edges), interference (junctions, suspension), wave (essentially absent at Ma ≈ 0.3).
2. Net momentum flux deficit behind the body; measured by wake surveys/rakes integrating $\rho u (u_\infty - u)$.
3. Wheels/wakes and wings at the top (public consensus, order-of-magnitude); exact splits confidential.
4. Ram capture at the inlet, duct/radiator pressure loss, exit momentum deficit/wake.
5. Because flow conditioning keeps downstream devices attached and clean — total drag is a system outcome.
6. Drag costs scale with $V^3$ in power terms; long straights make every $C_D A$ point expensive ⇒ low wing.
7. As heat and turbulence in the wake (plus some as acoustic/unsteady energy) — the entropy bill of going fast.
8. They cost drag directly *and* degrade following cars' performance — the double role that shaped the 2022 rules.
9. Merging boundary layers and mutual flow disruption at junctions/proximities producing more drag than the sum of parts.
10. Wheels fixed; cooling required; conditioning devices pay for themselves; separation dominates size; downforce purchase is legitimate drag.

---

## SOURCES (Part VIII)

- Hucho, W.-H. (ed.), *Aerodynamics of Road Vehicles*, SAE International (4th ed., 1998) — vehicle drag decomposition, cooling drag. [Tier 1]
- Anderson, J. D., *Fundamentals of Aerodynamics*, McGraw-Hill (6th ed., 2017) — drag categories, friction/form split. [Tier 1]
- Katz, J., *Race Car Aerodynamics*, Bentley (1995) — race-car drag accounting. [Tier 1]
- Mears, A., Dominy, R. & Sims-Williams, D., "The Air Flow About an Exposed Racing Wheel", SAE 2002-01-3290 — isolated-wheel drag magnitude. [Tier 1]
- Axerio-Cilies, J. & Iaccarino, G., *ASME J. Fluids Eng.* 134(12), 2012 — rotating-wheel flow/drag. [Tier 1]
- Toet, W. (2013), *The Aeronautical Journal* — where F1 drag comes from, from practice. [Tier 2]
