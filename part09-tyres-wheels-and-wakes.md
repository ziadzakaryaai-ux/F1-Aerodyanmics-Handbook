# PART IX — Tyres, Wheels and Wakes

**Purpose:** understand the exposed rotating wheel — the F1 car's hardest aerodynamic problem — and why every downstream component's performance depends on how well the wheel wakes are handled.

**Course connection:** anchors: Mears/Dominy/Sims-Williams (SAE 2002-01-3290); Axerio-Cilies & Iaccarino (ASME JFE, 2012); Hucho wheel chapters; Katz ch. 4. Module mapping: ____________

---

## 9.1 Why wheels are aerodynamically hostile 🟡

An exposed racing wheel is three problems in one body:

1. **Bluff body:** a blunt disc/tyre with massive, unsteady separation at high Reynolds number.
2. **Rotating:** the wall velocity is *non-zero* (no-slip on a moving surface), reversing the classic "stationary body" intuition; the ground blocks the flow at the contact patch.
3. **Deforming:** tyre load deflects the carcass — contact-patch bulge and sidewall squash change the local geometry with speed and load (secondary but real, and regulated geometry changes with 18-inch wheels changed the flow too).

No aircraft deals with any of these; road cars hide two of them behind wheel arches. In F1 they sit in the open, on the most performance-critical flow paths of the car.

---

## 9.2 The flow field of an isolated rotating wheel (documented structure) 🟡

The literature (Mears et al.; Axerio-Cilies & Iaccarino; McManus & Zhang; Knowles et al.) gives a consistent picture, sketched in Figure 9.1:

![Rotating wheel flow features.](diagrams/p09-wheel-flow.svg)
*Figure 9.1 — Documented structure of the isolated rotating-wheel flow (schematic after the cited studies).*

- **Stagnation and "jetting":** the ground blocks the oncoming flow at the front of the contact patch; pressure rises there and the blocked flow squirts *forward and around* the tyre sides — the jet. Rotation energises this jet (the ground vortex pair).
- **Separation:** top separation and side separations are strong and *shift with rotation* — the rotating surface drags the boundary layer further around before it lets go. Documented effect of rotation vs stationary: top separation location moves earlier by tens of degrees; the wake becomes **taller and narrower**; the recirculating core grows.
- **The wake: a counter-rotating vortex pair (CVP)** filling the wake behind the wheel, with **upwash** behind the wheel (rotation pumps the wake upward around hub height) — a wheel wake is not a passive deficit; it is an organized, rising, swirling structure.
- **Force effects of rotation (isolated-wheel studies, order-of-magnitude):** rotating wheels show *lower* drag than stationary ones (of order 10%+), drastically less upward lift (rotation + jetting change the underbody/ground-vortex behaviour), and different side-force behaviour.

**Why the wake is so damaging downstream:** it combines a *large momentum deficit* (drag, Part VIII), *strong organised vorticity* (the CVP bends and scours whatever it touches), and *high unsteadiness* (broadband turbulence that decorrelates everything behind it). A downstream floor edge, fence, or wing element sees its inlet conditions change in both space and time.

---

## 9.3 Front-wheel wake and its management 🟡→🔴

The front-tyre wake lands directly on the floor, sidepods, and everything aft. Management tools, in regulation and in practice:

- **Front wing outwash** (Part IV): steer clean flow *around* the tyre to shield downstream devices.
- **Floor fences:** the first floor inlets are placed and shaped to digest what the tyre wake delivers, and to keep the tunnels fed at yaw.
- **Wheel covers / over-wheel geometry (2022+):** regulated bodywork to reduce the tyre's wake messiness.
- **Suspension shaping:** arms positioned/shaped to avoid feeding the wake further downstream.

**ENGINEERING INTUITION**
> If you remember only one thing: the front wheels own the inlet conditions of the whole car. "Making the front wing better" almost always means "making the front-tyre wake matter less".

---

## 9.4 Rear-wheel wake 🟡

The rear-tyre wake interacts with the diffuser's exit flow, the beam wing, and the rear wing's lower surface. The diffuser/beam-wing upwash (Parts IV–V) exists partly to *lift the floor jet over* the rear-tyre wakes. Get this wrong and the rear wing's lower surface eats turbulent wake: load fluctuates, stall margins shrink, and the car's rear becomes speed- and attitude-sensitive. Tyre *deformation* matters here too: a squatted rear tyre at speed changes the wake geometry the rear wing was designed around.

---

## 9.5 Wheel wake and the car behind 🟡

Wheel wakes are the main reason following an F1 car is hard: they are unsteady, wide, and contain the strongest vorticity in the whole flow field. The 2022 regulations attacked this directly (wheel covers, removed bargeboards, floor-centric load) — the FIA's stated goal was a following car losing much less downforce at close range (public figures of order ~46% loss for 2021 cars vs ~18% target for 2022 cars circulated in FIA materials; see Engineering Audit for verification status).

---

## COMMON MISCONCEPTIONS (Part IX)

> ❌ **"Wheel drag is mostly skin friction on the tyre."** It is overwhelmingly pressure/form drag from separation and the wake. The tread's friction is a rounding error.
>
> ❌ **"A stationary-wheel CFD model is good enough."** Rotation changes separation positions, wake structure (taller, rising) and even the sign of some loads. The early literature's main lesson is exactly this difference.
>
> ❌ **"The wheel wake just blows backwards."** It rises (upwash around hub height) and contains an organised CVP — it bends *around and over* downstream components, which is what makes it so invasive.
>
> ❌ **"Slipstreaming an F1 car is like following a truck."** The wakes are narrower, vortical, and high-energy in different places; the benefit is real but the spatial structure is completely different — hence tow behaviour varies corner-by-corner.
>
> ❌ **"Tyre deformation is a mechanical footnote."** The deforming tyre *is* an aerodynamic body whose shape varies with load and speed — one reason aero maps at fixed geometry cannot fully represent reality.

---

## F1 ENGINEERING QUESTIONS (Part IX)

**Conceptual**
- Explain jetting in continuity terms: what is blocked, and where does the flow go?
- Why does rotation make the wheel wake *taller*? (Follow the surface velocities.)
- Why is the wheel wake's unsteadiness a bigger problem for a downstream wing than its mean deficit?

**Engineering**
- Your floor loses load when following. How would you decide whether front-tyre wake management or floor-robustness is the better investment?
- What would you change first to reduce front-tyre wake into the sidepods: FW outwash, fences, or wheel cover? Why?

**CFD**
- Why must the wheels rotate in your CFD (and the ground move) to trust underbody data?
- How would you compare two wheel-wake "treatments" — which metrics, which survey planes?

**Design**
- Brief: reduce the front-tyre wake's impact on the floor's first fence by 20% without adding drag. Sketch two mechanisms and their risk.
- How would you design the diffuser/beam-wing system to be more robust to rear-tyre wake wandering?

---

## QUICK RECALL (Part IX)

1. Name the three simultaneous problems an exposed F1 wheel presents.
2. What is jetting, and what structure does it leave near the ground?
3. Describe the isolated rotating wheel's wake in three features.
4. What changes (documented, order-of-magnitude) between rotating and stationary wheel flows?
5. Why do front wheels "own the inlet conditions" of the car?
6. Name three regulation/practice tools for front-tyre-wake management.
7. Why does the diffuser/beam-wing system care about the rear-tyre wake?
8. What made wheel wakes central to the 2022 rule changes?
9. Why is the wheel wake's CVP more damaging than its momentum deficit?
10. How does tyre deformation couple into the aero problem?

### ANSWERS

1. Bluff-body separation; rotation (moving wall); deformation under load.
2. Ground-blocked flow squirting forward/around at the contact patch, leaving a ground-vortex pair energised by rotation.
3. Counter-rotating vortex pair; upwash (rising wake); large unsteady recirculating core.
4. Top separation moves earlier (tens of degrees), wake taller/narrower, drag lower by ~10%+, upward lift drastically reduced (order-of-magnitude from isolated-wheel studies).
5. Their wakes set the flow quality delivered to floor, sidepods and everything downstream.
6. FW outwash shaping, floor fences, wheel covers/over-wheel bodywork (plus suspension shaping).
7. The rear-tyre wake sits where the diffuser jet and beam wing work; wake wandering changes the rear wing's inlet quality and stall margin.
8. They are the biggest unsteady vortical contaminant for following cars — the regs targeted wheel covers, bargeboard removal and floor-centric load to reduce sensitivity.
9. The CVP actively bends/organises the disturbance and scours surfaces — a structured intruder, not just a slow region.
10. Load and speed change the tyre's shape, hence the flow geometry the whole downstream system was tuned to.

---

## SOURCES (Part IX)

- Mears, A., Dominy, R. & Sims-Williams, D., "The Air Flow About an Exposed Racing Wheel", SAE 2002-01-3290, 2002 — isolated-wheel flow structure, jetting, wake. [Tier 1]
- Axerio-Cilies, J. & Iaccarino, G., "An Aerodynamic Investigation of an Isolated Rotating Formula 1 Wheel Assembly", *ASME J. Fluids Engineering* 134(12), 2012 — rotating vs stationary wheel flow and forces. [Tier 1]
- McManus, J. & Zhang, X., "A Computational Study of the Flow Around an Isolated Wheel in Contact with the Ground", *ASME J. Fluids Eng.* 128(4), 2006 — wake vortical structure. [Tier 1]
- Knowles, R. et al., "On the near wake of a Formula One front wheel", *Proc. IMechE Part D*, 2013 — front-wheel wake detail. [Tier 1]
- Hucho, W.-H. (ed.), *Aerodynamics of Road Vehicles*, SAE (4th ed., 1998) — wheel/tyre aerodynamics background. [Tier 1]
- Zhang, X., Toet, W. & Zerihan, J., "Ground Effect Aerodynamics of Race Cars", *Applied Mechanics Reviews* 59(1), 2006 — wheels in the ground-effect context. [Tier 1]
