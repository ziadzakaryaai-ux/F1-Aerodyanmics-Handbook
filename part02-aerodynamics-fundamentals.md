# PART II — Aerodynamics Fundamentals

**Purpose:** answer the deepest question in the syllabus — *where does aerodynamic force actually come from* — and build the boundary-layer machinery that explains separation, stall, vortices and most F1 failures.

**Course connection:** canonical anchors are Anderson ch. 1.7–1.8 (force origins), ch. 4 (incompressible flow over airfoils), ch. 15–17 depending on edition (boundary layers, transition); Katz ch. 2 (race-car force coefficients). Module mapping: ____________

---

## 2.1 What actually generates aerodynamic force? 🟢

Two, and only two, mechanisms act on any body in a flow:

1. **Pressure** — the normal stress $p$ acting perpendicular to every wetted surface.
2. **Shear stress** — the tangential friction $\tau$ acting along every wetted surface.

$$\vec{F}_{aero} = \oint_{S} (-p\,\vec{n} + \vec{\tau}) \, dS$$

| Variable | Meaning | Units |
|---|---|---|
| $p$ | local static pressure | Pa |
| $\vec{n}$ | outward surface normal | — |
| $\vec{\tau}$ | wall shear stress vector | Pa |

Everything else — lift, drag, downforce, pitching moment, "ground effect", "vortex sealing" — is bookkeeping on this integral. If a design change doesn't alter the pressure distribution or the shear distribution, it changes nothing.

**The two equivalent explanations of lift.** The same physics can be viewed two ways, and a competent aerodynamicist switches between them freely:

- **Pressure-field view:** the body curves the streamlines; curved streamlines require a centripetal pressure gradient (Newton's 2nd law applied to fluid elements); integrating the resulting pressure difference over the body gives the force.
- **Momentum view:** the body deflects the airflow — turning it down (for lift) or up (for downforce). The rate of change of momentum of the air equals the force on the body (Newton's 3rd law). Measure the momentum deficit/deflection in the wake and you have measured the force without touching the body.

Both are exact descriptions of the same phenomenon. **Circulation** ($\Gamma$, §2.6) is the mathematical bridge: the Kutta–Joukowski theorem $L' = \rho V_\infty \Gamma$ ties the lift per unit span to the circulation, which exists *because* the pressure field and the boundary-layer behaviour allow flow to leave the trailing edge smoothly (the Kutta condition).

**COMMON MISCONCEPTIONS (lift — read this twice)**
> ❌ **"Air must travel faster over the top to meet the same parcel at the trailing edge (equal transit time)."** Experimentally false — the upper-surface air arrives *early*. There is no transit-time requirement anywhere in physics.
>
> ❌ **"Fast air has lower pressure, and that's why there's lift."** Backwards as causality (Part I). The pressure field is set by momentum/curvature; Bernoulli then relates the speeds to that field.
>
> ❌ **"Lift comes only from the bottom surface pushing air down."** False — on a conventional wing the *upper* surface contributes most of the lift through suction. On an F1 wing, the *lower* surface suction dominates. The integrand in §2.1, not folklore, decides.
>
> ❌ **"Downforce wings 'push' air down off their underside like a wedge."** The force is a distributed pressure/suction field plus the associated momentum change of a large volume of air — the deflection region extends many chord lengths around the wing, not just "under it".
>
> ✅ **The correct compact statement:** geometry + flow constraints create a curved, deflected flow; momentum conservation demands a pressure field to deliver that curvature; integrating that field over the surfaces gives the force; circulation is its quantitative signature.

---

## 2.2 Pressure distribution and the pressure coefficient 🟢

The workhorse of all aerodynamic analysis:

$$C_p = \frac{p - p_\infty}{q_\infty}, \qquad q_\infty = \tfrac12 \rho V_\infty^2$$

| Variable | Meaning | Units |
|---|---|---|
| $p$ | local static pressure | Pa |
| $p_\infty, V_\infty$ | free-stream static pressure / velocity | Pa, m/s |
| $C_p$ | pressure coefficient | dimensionless |

Reference values: stagnation point $C_p = +1$; free stream $C_p = 0$; suction peaks go strongly negative (values beyond −2 are common on F1 wing elements near the ground — engineering inference from underbody pressure levels).

![Pressure distribution around an inverted (downforce) wing.](diagrams/p02-cp-inverted-wing.png)
*Figure 2.1 — An inverted wing lives on its lower-surface suction peak. The shaded area is the net load. Reading and manipulating this picture is 70% of wing-development work (Part XV).*

**F1 application:** every wing element, the floor throat, the diffuser — each is a *pressure distribution shaping problem*. Designers push suction peaks where load is needed while managing the pressure *recovery* behind them (which is where separation lives).

---

## 2.3 Lift, drag, pitching moment — and their coefficients 🟢

With reference area $S$ (or "area" $A$) and dynamic pressure $q$:

| Quantity | Definition | Coefficient |
|---|---|---|
| Lift (up) | $L$ | $C_L = L/(qS)$ |
| Drag (rearward) | $D$ | $C_D = D/(qS)$ |
| Pitching moment | $M$ | $C_M = M/(qSc)$ |

For an F1 car the lift is *negative* — teams speak of **downforce** $= -L$, and quote **downforce area $C_L A$** and **drag area $C_D A$** [m²] because reference-area conventions differ. Useful orders of magnitude (public-domain estimates, mid-2020s cars, mid-wing settings — treat as approximate):

- $C_L A \approx 3.5$–$5\ \text{m}^2$ (high downforce ~5+, Monza ~2.5–3)
- $C_D A \approx 1.0$–$1.7\ \text{m}^2$
- Effective lift-to-drag ratio of the whole car: roughly 2.5–3.5 — *terrible* by aircraft standards (gliders exceed 40), and that trade-off is the central economic problem of the sport (Parts VII–VIII).

**Pitching moment** matters because the car is a lever: the distribution of lift between front and rear axles, and the drag height, create moments that load and unload the tires (Part X).

---

## 2.4 Airfoil geometry, angle of attack, camber 🟢

- **Chord $c$:** reference length, leading edge to trailing edge.
- **Angle of attack $\alpha$:** angle between the chord line and the free stream. For a downforce wing the flow approaches the *pressure* (upper) side, i.e., negative $\alpha$ in the aviation convention, or you flip the wing upside down and keep $\alpha$ positive in the F1 convention — sign conventions are team/regulation artifacts; the physics is symmetric.
- **Camber:** the curvature of the mean line. Camber is the primary lever for generating circulation at zero α. Inverted camber → downforce.
- **Thickness & leading-edge radius:** set the suction-peak sharpness, and therefore how much adverse gradient (§2.5) the boundary layer must survive. F1 wing elements are thin with small leading-edge radii — high load, but fragile to stall.

---

## 2.5 The boundary layer 🟢→🟡 (the most important concept in this handbook)

**TERM — Boundary Layer**
- **Simple:** the thin region near a surface where the air is slowed down by friction.
- **Technical:** the region in which velocity rises from the no-slip wall value to the external velocity $u_e$; thickness $\delta_{99}$; governed by viscous diffusion of momentum. $\delta \sim 5x/\sqrt{Re_x}$ (laminar), $\sim 0.37x/Re_x^{-1/5}$ (turbulent); flat-plate skin friction $C_f = 0.664/\sqrt{Re_x}$ (laminar), $\approx 0.059 Re_x^{-1/5}$ (turbulent).
- **F1 relevance:** its state decides separation, stall, wing load limits, diffuser stability and wake character. Most F1 "packages" are, at bottom, boundary-layer management devices.

Inside the layer, the flow's momentum budget is: friction and pressure gradients spend it; the free stream and any slots/jets replenish it. Two outcomes matter:

**Adverse pressure gradient ($dp/dx > 0$).** Where the flow must decelerate (rear of a wing element, diffuser expansion), the slow near-wall fluid is the first to run out of momentum.

**Flow separation.** When the near-wall flow stops moving forward (wall shear $C_f \to 0$) and then reverses, the boundary layer separates: the flow leaves the surface, a low-energy recirculating region forms, and the *intended pressure distribution collapses*. Separation is the mechanism behind stall, stalled diffusers, and dead wing elements.

![Boundary-layer velocity profiles in an adverse pressure gradient.](diagrams/p02-separation.png)
*Figure 2.2 — Separation is a momentum bankruptcy: friction + pressure rise consume the near-wall momentum budget.*

**Stall** is the large-scale loss of load when separation eats the suction surface. On thin, highly loaded F1 elements it can be abrupt and is often **three-dimensional** (vortex-induced, tip-driven, or flap stall) — 2-D intuition under-predicts its violence.

**Transition** (laminar → turbulent) is managed, not avoided: turbulent layers resist separation better. Devices: natural transition, pressure-field design, or **vortex generators / trips**. In the tunnel, trip dots force realistic transition at model Re (Part XI).

**ENGINEERING INTUITION**
> If you remember only one thing: an F1 car is a system for keeping boundary layers attached where they pay rent (wing elements, floor throat, diffuser) and paying them off where they don't. Every "the car lost the rear" story of the last decade — including porpoising — is partly a boundary-layer story.

---

## 2.6 Vortices and circulation (appetiser) 🟢

A **vortex** is fluid rotating about an axis; its strength is the **circulation** $\Gamma = \oint \vec{V}\cdot d\vec{l}$. Vortices matter to F1 for three distinct jobs: (1) they are the *price* of finite-span lifting wings (tip vortices → induced drag, Part VII); (2) they are *tools* (floor-edge vortices seal the underbody, Part VI); (3) they are *contaminants* (wheel wakes, Part IX). Full treatment in Part VI.

---

## 2.7 From aircraft coefficients to race-car coefficients 🟡

The coefficient definitions are identical for aircraft and race cars. What changes is everything else:

| | Aircraft wing | F1 car |
|---|---|---|
| Flow quality | clean free stream | wings operate in other components' wakes |
| Ground | absent | defines the whole underbody problem (Part V) |
| Aspect ratio | high (efficient) | low, span-limited by regulations |
| Objective | maximize L/D | maximize **Δ(lap time)**: downforce-dominated, drag tolerated |
| Re configuration | cruise-fixed | continuously varying with speed & attitude |

This is why "F1 car = upside-down airplane" fails as a design mental model — expanded in Part III.

---

## COMMON MISCONCEPTIONS (Part II)

> ❌ **"More downforce coefficient is always better."** Downforce costs drag, tyre energy, and can destabilise the underbody; the optimum is lap-time-optimal per circuit (Parts VII, X, XV).
>
> ❌ **"Separation = the flow stops."** The *near-wall* flow reverses; above it there is still fast-moving fluid. A separated shear layer can even reattach (separation bubbles) — which is why "there's a bubble" vs "it's fully stalled" are different engineering conversations.
>
> ❌ **"Cp plots directly show force by colour."** Only the *integral* of Cp over area, projected correctly, is force. A big red patch on a small surface can matter less than a modest suction over a large one (Part XIV).
>
> ❌ **"Skin friction is what makes F1 drag big."** Pressure (form) drag, induced drag and the wheels' wakes dominate. Friction is real but secondary at car scale (Part VIII).
>
> ❌ **"Turbulent flow separates less, so make everything turbulent."** It resists adverse gradients better but costs friction and thickens the layer (losing more pressure recovery). It's a local design choice, not a global blessing.

---

## F1 ENGINEERING QUESTIONS (Part II)

**Conceptual**
- Explain downforce twice: once with momentum, once with the pressure field. Where do the two accounts disagree quantitatively, if at all?
- Why does a suction peak at the leading edge make an element stall-prone?
- What does "the floor is working harder than the wing" mean in Cp terms?

**Engineering**
- You add a Gurney flap to a rear wing: what happens to the pressure distribution, total load, and drag? What is the boundary-layer mechanism?
- A rival runs a thinner main plane with sharper LE radius. What load/stall trade are they making?

**CFD**
- Where would you place Cp monitor points to catch early separation on a flap?
- Which surface quantity — Cp or wall shear — tells you *first* that a diffuser is stalling? Why?

**Design**
- Hypothesis: the flap stalls in fast corners because of the wakes from the element ahead. What two design directions could fix it, and what does each cost?
- If you were given "more front-axle load without more front-wing drag", which pressure-region would you attack first?

---

## MINI PROBLEMS (Part II)

**Problem 1 — Downforce from a floor region**
*Given:* a floor region of 1.2 m² working at an area-averaged $C_p = -1.1$; car at 250 km/h ($V = 69.4$ m/s), $\rho = 1.225$ kg/m³. *Required:* downforce from that region.
*Solution:*
$q = 0.5 \times 1.225 \times 69.4^2 = 2{,}951$ Pa.
$F = |C_p| \, q \, A = 1.1 \times 2{,}951 \times 1.2 \approx 3.9\ \text{kN}$ — about half the car's weight (800 kg ≈ 7.85 kN).
*Engineering interpretation:* single surfaces routinely carry weight-scale loads. This is why floor-ride-height changes of millimetres move lap time by tenths, and why underbody separation is catastrophic rather than merely inconvenient.

**Problem 2 — Reading a wake to get drag (momentum view)**
*Given:* behind a body, the wake has a mean velocity 30% below free stream across a band of area 0.4 m² (normal to flow), other regions undisturbed; $V_\infty = 80$ m/s, $\rho = 1.225$. *Required:* estimate drag.
*Solution:*
Momentum flux deficit $\approx \rho \, \Delta u \cdot A \cdot u_{wake}$; take deficit $\Delta u = 0.3 V_\infty = 24$ m/s at mean wake speed $\approx 0.85 V_\infty = 68$ m/s:
$D \approx 1.225 \times 24 \times 0.4 \times 68 \approx 800\ \text{N}$.
*Engineering interpretation:* this is exactly what a wake/aero-rake survey does (Parts IX, XI): you never need to touch the body to weigh its drag — momentum bookkeeping in the wake is the measurement.

---

## QUICK RECALL (Part II)

1. State the two surface-stress mechanisms that produce aerodynamic force.
2. Give the correct "why does a wing generate lift" in two sentences, then name two classic wrong versions.
3. Define Cp and give its value at a stagnation point, in the free stream, and in a strong suction peak.
4. What is the boundary layer, and what two budget items deplete its near-wall momentum?
5. What single wall quantity flags incipient separation?
6. Why do F1 teams quote $C_L A$ and $C_D A$ instead of $C_L$ and $C_D$?
7. Order-of-magnitude: $C_L A$ and $C_D A$ of a current car, and what ratio do they imply?
8. Why is a turbulent boundary layer *preferred* in some F1 locations?
9. What is the Kutta condition, and what does it prevent?
10. Why can't you integrate a Cp *colour plot* by eye and call it force?

### ANSWERS

1. Pressure (normal stress) and wall shear stress; nothing else.
2. Geometry deflects and curves the flow; momentum conservation requires the associated pressure field; integrating it gives the force (circulation $L'=\rho V \Gamma$ quantifies it). Wrong versions: equal-transit-time; "fast air ⇒ low pressure" as a cause.
3. $C_p = (p-p_\infty)/q_\infty$; stagnation +1; free stream 0; suction peaks −1 to −3+ on highly loaded F1 elements (order-of-magnitude, engineering inference).
4. The near-wall region of retarded flow created by no-slip + viscosity; depleted by friction and adverse pressure gradients.
5. Wall shear stress → zero ($C_f \to 0$), then reversed.
6. Reference-area conventions vary between teams/eras; multiplying out the reference area removes the ambiguity and gives directly scalable force-per-dynamic-pressure.
7. Roughly $C_L A$ 3.5–5 m², $C_D A$ 1.0–1.7 m² (public estimates, setup-dependent) ⇒ car L/D ≈ 2.5–3.5.
8. Where adverse gradients threaten separation (rear of elements, diffuser): turbulent mixing re-energises the layer and delays stall, at the cost of friction drag.
9. Flow leaves a sharp trailing edge smoothly along one side; prevents the unphysical infinite-velocity wrap-around solution and fixes the circulation magnitude.
10. Force needs $\int C_p\,dA$ over real surface area with correct normals; colour patches ignore area weighting, surface orientation, and integration limits.

---

## SOURCES (Part II)

- Anderson, J. D., *Fundamentals of Aerodynamics*, McGraw-Hill — airfoil pressure distributions, circulation, boundary layers, separation fundamentals. [Tier 1]
- Katz, J., *Race Car Aerodynamics*, Bentley (1995) — race-car coefficients, downforce conventions. [Tier 1]
- McBeath, S., *Competition Car Aerodynamics*, Veloce — practical pressure-distribution reading for race cars. [Tier 2]
- Toet, W., "Aerodynamics and aerodynamic research in Formula 1", *The Aeronautical Journal* (2013) — how F1 actually uses these concepts. [Tier 2]
- Anderson, J. D., *Introduction to Flight* / NACA Report 460 (Abbott & von Doenhoff) for equal-transit-time debunking context; also Holger Babinsky's "How do wings work?" *Physics Education* 38 (2003). [Tier 2]
