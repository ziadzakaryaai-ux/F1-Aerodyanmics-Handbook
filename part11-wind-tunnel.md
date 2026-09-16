# PART XI — Wind Tunnel

**Purpose:** how a wind tunnel works, what it measures, where it lies, and how an F1 aerodynamic development programme actually uses it — including the FIA's restrictions on its use.

**Course connection:** anchors: Barlow, Rae & Pope, *Low-Speed Wind Tunnel Testing* (the canonical text); Katz ch. 8; Zhang/Toet/Zerihan review (moving-ground testing). Module mapping: ____________

![Wind tunnel with rolling road.](diagrams/p11-wind-tunnel.svg)
*Figure 11.1 — Elements of an F1-type tunnel. The rolling road and rotating wheels are not accessories; without them the underbody data is simply wrong (Part V).*

---

## 11.1 Why tunnel-test at all 🟢

A wind tunnel creates a controlled, repeatable, instrumented flow around a model, letting you: isolate variables (one geometry change at a time), measure forces precisely (balance), and see the flow (visualisation). Its purpose is *differential development* — quantifying deltas between designs far more accurately than absolute numbers.

F1 teams operate their own tunnels (team-specific sites, e.g., public knowledge: Toyota's former Cologne tunnel, Mercedes' Brackley facility, etc.) testing **scale models — commonly 50–60% scale** — on rolling roads with rotating wheels.

---

## 11.2 The similitude problem (scale effects) 🟡

Dynamic similarity requires matching $Re$ (and Mach, and Froude for free-surface effects — irrelevant here):

$$Re_{model} = \frac{\rho V_{model} L_{model}}{\mu} \stackrel{!}{=} Re_{full}$$

At 50% scale and equal velocity, $Re$ is only half of full scale; teams test at model speeds of tens of m/s (public: up to ~50 m/s class). You **cannot** close the gap fully (velocities are limited by model structural loads, drive power, and compressibility). Consequences and their standard handling:

- **Relatively thicker boundary layers** at lower $Re$ → margins differ; designers build correlation experience ("tunnel deltas vs track deltas").
- **Transition management:** without help, model boundary layers transition at different locations than full scale. Teams place **trip dots** to force transition where it would naturally occur on the full-scale car.
- **Stall/separation margins** shift — the tunnel is optimistic or pessimistic in known directions, per component, per team.

**ENGINEERING INTUITION**
> If you remember only one thing: the tunnel never gives you the track. It gives you *ranked deltas* — and the entire craft of testing is knowing how those deltas distort on the way to the car.

---

## 11.3 Making the ground real: rolling road & wheels 🟡

A fixed floor builds its own boundary layer, which the model would then fly through — physically wrong for a car whose ground is moving. The **moving belt (rolling road)**, matched to airspeed, plus **rotating wheels** (belt- or motor-driven, with regulated/vetted wheel rotation), reproduce the relative motion that dominates underbody and wheel-wake physics. Boundary-layer bleeding/suction ahead of the belt and careful belt-model gaps manage the seams. Every ground-effect concept in Part V was *born* in tunnels that got this right — and the historical moving-ground-facility literature (e.g., the Zhang/Toet/Zerihan review) documents how badly fixed-floor data distorts underbody forces.

---

## 11.4 Blockage and corrections 🟡

The tunnel walls constrain the flow (solid blockage) and the wake (wake blockage), inflating apparent dynamic pressure and forces relative to open air. Standard corrections (area-ratio based for solid blockage; wake-based for drag) are applied; F1 tunnels use large test sections relative to model size to keep corrections small. The same phenomenon — but infinitely worse — affects CFD domain sizing (Part XII); the physics is identical: boundaries that are too close flatter the design.

---

## 11.5 Instrumentation & flow diagnostics 🟡

- **Force & moment measurement:** a high-precision **internal six-component balance** (or under-floor external balance) gives the full force/moment vector; with model attitude actuators, teams sweep **aero maps** — heave, pitch, roll, yaw matrices (Part III §3.4).
- **Pressure taps:** hundreds of surface taps scan pressure distributions on wings/floor — the experimental Cp plots of Figure 2.1.
- **Flow visualisation:** tufts (surface flow direction), flow-vis paint (time-integrated surface streamlines), smoke wands (streaklines).
- **Particle image velocimetry (PIV):** laser-sheet imaging of seeded flow gives planar velocity fields — the experimental version of CFD slices; used for wake/vortex surveys (with restricted access windows and model-zone limitations).
- **Aero rakes:** pitot-tube combs traversed in the wake — direct CFD-correlation datasets (used on track too, publicly visible since ~2019).

---

## 11.6 The F1 development programme & its governor 🟡→🔴

A typical development use of the tunnel: validate the week's best CFD geometries → run aero maps (attitude sweeps) → compare deltas to baseline → flag robustness issues (map regions where the gain dies) → hand correlated upgrades to the track group.

The FIA **Aerodynamic Testing Regulations (ATR)** cap this activity: wind-tunnel *occupancy* and *runs*, and CFD *usage*, are allocated on a **sliding scale tied to championship position** (worse finish → more testing allowance), with further adjustments under cost-cap-era rules. The precise unit system (runs, hours, "tokens") is revised periodically; the *mechanism* — testing capped inversely to success, to slow the rich-get-richer spiral — is the durable fact. Check the current ATR edition for exact numbers.

**COMMON MISCONCEPTIONS (wind tunnel)**
> ❌ **"The tunnel is the ground truth that CFD is judged against."** The tunnel is a *measurement of a model* — with scale effects, support interference, belt seams and its own uncertainty bands. Tunnel↔track correlation is its own hard problem; the tunnel is one instrument among three (tunnel, CFD, track), none of which is "truth" alone.
>
> ❌ **"Model-scale numbers convert by scale factor."** Forces don't scale by $L^2$ naively across mismatched $Re$; coefficients transfer only with transition management and correlation experience.
>
> ❌ **"A fixed floor is fine for force testing."** For road cars with sealed underbodies, marginally; for ground-effect race cars, catastrophically wrong — the underbody is the engine of the car.
>
> ❌ **"Tunnels are unlimited resources."** ATR caps occupancy and CFD — the *allocation* of tunnel hours is a strategic team resource, planned like a budget.

---

## F1 ENGINEERING QUESTIONS (Part XI)

**Conceptual**
- Why does a rolling road change underbody *force*, not just flow pictures?
- What exactly does a trip dot replace, and why is it needed at model scale?
- Why is blockage worse for a wake-heavy body than a clean one?

**Engineering**
- Your tunnel says +1.5% $C_L A$, the track says −0.5%. List four candidate causes and one diagnostic each.
- How would you plan a tunnel session to *also* validate CFD, not just rank geometries?

**CFD**
- Which tunnel-related corrections have CFD analogues, and why does CFD still need its own discipline (Part XII)?
- What model-scale phenomena would you *deliberately* recreate in CFD to build correlation?

**Design**
- You have 8 hours of tunnel time and 20 candidate geometries from CFD. Design the screening strategy.
- Where would you place instrumentation to catch the floor-edge vortex failing (Part VI) on a 55% model?

---

## QUICK RECALL (Part XI)

1. State the dynamic-similarity condition for tunnel testing and why F1 tunnels can't fully match it.
2. What is a rolling road for, physically?
3. Name four instrumentation systems and what each measures.
4. What is blockage, and how do tunnels and CFD each handle it?
5. What does the ATR sliding scale do, and why?
6. Why are trip dots used on models?
7. What is an aero map, and which variables does it sweep?
8. Why is "tunnel = truth" wrong? Give two reasons.
9. What does flow-vis show that tufts don't?
10. What is the tunnel's real product — absolute numbers or something else?

### ANSWERS

1. Match $Re$ ($\rho V L/\mu$); at 50% scale, $V$ would need to double (limited by loads/power) — an order-of-magnitude gap remains in practice.
2. Reproduces relative ground motion; removes the fixed-floor boundary layer that falsifies underbody physics.
3. Six-component balance (forces/moments), pressure taps (surface Cp), PIV (planar velocity fields), aero rakes (wake surveys); plus tufts/flow-vis/smoke.
4. Walls constrain flow/wake, inflating forces; corrected in tunnels by formulas/large sections; in CFD by domain sizing — the same boundary-interference physics.
5. Caps tunnel occupancy/runs and CFD usage inversely to championship position — to limit the resource advantage of successful (rich) teams.
6. They force transition to the full-scale location, compensating the model's lower $Re$.
7. The force/moment response sampled over heave/pitch/roll/yaw — the car's aerodynamic personality.
8. It measures a scaled model (Re mismatch, transition, support/belt interference) and has its own uncertainty; it is one leg of a three-legged correlation stool.
9. Flow-vis gives time-integrated surface streamlines (where flow *went*); tufts show local direction behaviour live.
10. Ranked, repeatable *deltas* between designs — plus correlation currency for CFD and track.

---

## SOURCES (Part XI)

- Barlow, J. B., Rae, W. H. & Pope, A., *Low-Speed Wind Tunnel Testing*, Wiley (3rd ed., 1999) — blockage corrections, balance, testing practice. [Tier 1]
- Zhang, X., Toet, W. & Zerihan, J., "Ground Effect Aerodynamics of Race Cars", *Applied Mechanics Reviews* 59(1), 2006 — moving-ground testing and its importance. [Tier 1]
- Katz, J., *Race Car Aerodynamics*, Bentley (1995) — tunnel testing of race cars. [Tier 1]
- FIA Aerodynamic Testing Regulations (current edition) — testing restrictions mechanism. [Tier 1 — numbers periodically revised; see Engineering Audit]
- Toet, W. (2013), *The Aeronautical Journal* — tunnel/CFD/track roles from F1 practice. [Tier 2]
