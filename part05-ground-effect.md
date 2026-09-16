# PART V — Ground Effect

**Purpose:** the physics that makes an F1 car fast. Treated in depth: the underbody as a device, the diffuser as its pressure-recovery section, the ride-height force map, and porpoising as the instability where aerodynamics and suspension meet.

**Course connection:** anchors: Ranzenbach & Barlow (inverted airfoil in ground effect, 1990s); Zerihan & Zhang (wing in ground effect, *Journal of Aircraft*, 2000); Katz ch. 5; FIA 2022+ regulations (venturi tunnels). Module mapping: ____________

---

## 5.1 What "ground effect" actually is 🟡

Two distinct mechanisms share the name — you must keep them separate:

**Mechanism A — wing in ground effect (the "image" effect).** Any lifting surface near a solid boundary behaves as if a mirror-image vortex/airfoil existed below the wall (method of images). The image system increases the effective circulation for a given angle of attack and reduces the downwash-induced drag term. Net result at moderate proximity: **more load for the same geometry**, until very small clearances trigger losses (§5.4). Classic evidence: Ranzenbach & Barlow's inverted-airfoil studies and Zerihan & Zhang's single-element wing experiments — downforce rises as ride height falls, with a peak and a loss region at very low $h/c$.

**Mechanism B — underbody/venturi ground effect (the F1 floor).** The floor and reference plane form a **channel** (the 2022+ tunnels: floor, outer roof, ground). Mass conservation forces the flow to accelerate into the throat; the static pressure there falls well below ambient (strong suction over a large area); the diffuser then decelerates and recovers the pressure. This is a *designed* streamtube, and it is the main downforce generator of the modern car.

**Why proximity changes the flow at all:** the wall enforces the no-through-flow condition, so streamlines cannot escape downward; the effective flow area is geometry *and* clearance; and the wall kills vertical velocity — pressure fields become stronger and more two-dimensional than in free air.

![Underbody pressure distribution along the floor.](diagrams/p05-floor-cp.png)
*Figure 5.1 — The underbody Cp trace: suction concentrated at the throat, recovered through the diffuser. The dashed line is the same car with an over-driven expansion: the separation that "stalls" the diffuser destroys the recovery.*

**COMMON MISCONCEPTIONS (venturi & Bernoulli)**
> ❌ **"The air speeds up so the pressure drops"** (as a mechanism). Reversed/teleological again: geometry + mass conservation set the velocity; momentum conservation sets the pressure that accompanies it. Bernoulli is the bookkeeping identity between them.
>
> ❌ **"The venturi effect and Bernoulli are two different forces."** Neither is a force. "Venturi effect" is the *name* of the coupled behaviour in a constriction; Bernoulli is one valid relation inside it. The physics is continuity + momentum, with the boundary layer deciding whether the pattern can exist at all.
>
> ❌ **"The diffuser creates the downforce."** The *whole underbody* is the suction surface; the diffuser's job is pressure recovery — it raises the pressure at the exit so the low pressure upstream can exist and be maintained. A diffuser alone, without throat suction upstream, is a fairing.
>
> ❌ **"Sealing is about airtightness."** No seal exists; the edge vortex *fluid-dynamically* limits leakage. Skirts (banned hardware) were the mechanical version of the same idea.

---

## 5.2 The underbody as a streamtube (mass conservation first) 🟡

Model the tunnel as a 1-D streamtube: inlet area $A_1$ (set by fences, inlet geometry and ride height), throat area $A_t$ (minimum), exit at the diffuser.

$$\rho A_1 V_1 = \rho A_t V_t = \rho A_2 V_2$$

Everything follows: squeeze $A_t$ (lower ride height, tighter tunnel) ⇒ $V_t$ rises ⇒ (momentum balance) static pressure at the throat falls ⇒ more downforce. **But** two hard limits exist:

1. **Inlet supply:** the throat can only pass what the inlet and upstream flow deliver; a starved throat separates on its roof.
2. **Recovery:** whatever you accelerate, you must decelerate (§5.3) or pay it back in drag and lost mass flow.

**Ground clearance** enters here: lowering the car reduces $A_t$ *and* changes the inlet's ability to swallow flow. That is why the force-vs-height map is non-monotonic (§5.4) — not because "suction gets stronger" indefinitely.

---

## 5.3 The diffuser: pressure recovery, and why it can separate 🟡→🔴

The diffuser is a **subsonic diffuser** — one of fluid mechanics' least forgiving components. Its boundary layer must survive a long adverse gradient. Governed concepts:

- **Area ratio** (exit/throat): too aggressive → separation, pressure recovery collapses (Figure 5.1 dashed line).
- **Pressure recovery coefficient** $C_p = (p_{exit} - p_{throat})/q_{throat}$: real automotive diffusers recover far less than the ideal (boundary layers + 3-D corner flows).
- **Strakes** control the corner-vortex system and delay spanwise stall; the beam wing and rear wing set the exit condition by "pulling" flow upward.
- **Stalled diffuser symptoms:** plateau in Cp, rising drag, sudden load loss with ride height — and, in the worst case, the oscillation loop of §5.6.

**ENGINEERING INTUITION**
> If you remember only one thing: the floor's tunnels write the cheque (suction), the diffuser cashes it (recovery). A diffuser that stalls bounces the cheque — you lose both the load *and* the exit condition that keeps the whole rear of the car working.

---

## 5.4 The force map: downforce vs ride height 🟡

![Downforce vs ride height with regimes.](diagrams/p05-df-vs-h.png)
*Figure 5.2 — The canonical ground-effect map. Region 1: load rises as height falls (Mechanisms A+B reinforcing). Region 2: peak/plateau — the design target. Region 3: force *loss* at very low height — underbody choke/separation. The red arrow marks the porpoising feedback zone.*

Documented experimentally for isolated wings: Zerihan & Zhang measured force enhancement for clearances below $h/c \approx 0.2$–0.3, peak load around $h/c \approx 0.08$, and force *loss* below $h/c \approx 0.1$ (trailing-edge separation); their double-element follow-up found an **abrupt downforce discontinuity** at $h/c \approx 0.17$–0.24 caused by tip-vortex breakdown. Ranzenbach & Barlow traced the low-clearance loss to under-wing flow throttling as the wing and ground boundary layers merge. Teams re-create these regimes daily in full-car aero maps. The three regimes and their mechanisms:

1. **Force enhancement:** smaller clearance → stronger image effect + higher tunnel velocity ratio → more suction.
2. **Peak band:** the design ride heights; maximum stable load.
3. **Force loss:** at very low height the underbody/inlet chokes — the boundary layer fills the shrinking channel (blockage), separation appears on the tunnel roof or diffuser, and load *falls* with height.

**This is why "lower is always better" is false**, and why the mechanical setup (springs, bump stops, ride heights) is an aerodynamic instrument (Part X).

---

## 5.5 Pitch, roll, yaw sensitivity 🟡

- **Pitch (rake):** raising the front *and* keeping the rear low changes the underbody's effective expansion — rake generally moves load distribution rearward and changes total load non-monotonically. Teams run a few degrees of rake; the "correct" rake is a floor-geometry question.
- **Roll:** the loaded side's edge seal tightens (more load) while the unloaded side's opens (less) — a *balance* effect first, a load effect second.
- **Yaw:** crossflow weakens the inlet vortex system and edge sealing; tunnels starve asymmetrically. Yawed aero maps are where "eats its tyres in fast corners" problems are diagnosed (Part X).

All three sensitivities are measured (tunnel/CFD maps) and targeted: **low sensitivity = robust car = usable everywhere**.

---

## 5.6 Porpoising — the aero-structural instability 🔴

The mechanism, step by step (this is the negative-damping story, not a slogan):

1. Car runs low on the suspension; ride height enters the steep region of the force map.
2. A perturbation lowers the front slightly → downforce *rises* strongly (slope $dF/dh$ large and negative w.r.t. height) → springs compress further (positive feedback, negative aerodynamic damping/stiffness).
3. The underbody finally chokes/separates → load collapses → suspension rebounds → flow re-attaches → cycle repeats: a limit-cycle oscillation of the whole platform, typically a few hertz.
4. Consequences: driver exposure (2022 was severe on some cars), energy loss, tyre loading oscillation, data loss.

Countermeasures (all in public discussion/regulation in 2022–2023): raise the operating point (stiffer ride heights), increase suspension damping/stiffness so the aero slope is out-run, soften the force-map slope itself (floor edge geometry, tunnel inlet shaping), and the FIA's regulatory responses — the 2022 Technical Directive on oscillation limits (measured as a vertical-acceleration metric) and 2023 floor-edge/diffuser/plank geometry changes to move the map away from the unstable region.

**Why it is *not* "the car bouncing off bumps":** bumps force the car; porpoising is *self-excited* — the flow field is the spring-mass system's power source. That distinction is exactly why passive compliant suspensions can be unstable (a fixed body would never oscillate on a smooth road).

---

## 5.7 Aero platform stability & why the floor rules 🔴

A "stable platform" means: over the full attitude envelope, $dF/d(\text{attitude})$ has the *right signs* — load should decrease when the car goes lower past its design point, balance should not swing wildly with pitch/roll. Design levers: tunnel inlet shaping, throat position, diffuser area ratio, edge-wing geometry, and suspension tuning to sit in the stable band.

**Why the modern car relies on the floor:**
1. **Efficiency:** underbody suction acts over a large area with lower induced-drag cost than equivalent wing load (wings pay tip-vortex tax; tunnels are edge-sealed).
2. **Wake quality:** a floor-centric car sheds a more manageable wake than a wing-centric one — the 2022 regulations' racing-quality motive (public FIA rationale).
3. **Regulation:** the geometry is specified to make the floor the allowed big device; wings are deliberately constrained.

---

## F1 ENGINEERING QUESTIONS (Part V)

**Conceptual**
- Explain, in momentum terms, why underbody suction exerts downward force on the floor.
- Why does the same floor produce less load at the same height when the car yaws?
- What physically limits the pressure recovery a diffuser can achieve?

**Engineering**
- A car porpoises at one circuit only. List five candidate causes and a test to isolate each.
- You may spend 3 mm of ride height on either the front or the rear axle to fix understeer. Which force-map data decides?

**CFD**
- How would you detect underbody choke in a steady RANS solution? Which monitors?
- Why is steady RANS *questionable* for porpoising studies, and what would you run instead?

**Design**
- Redesign brief: move the force-loss knee to a lower ride height without losing peak load. Which geometry do you touch first, and what is the risk?
- The diffuser must grow for the floor upgrade. What must the beam wing and rear wing do to keep the exit condition?

---

## MINI PROBLEM (Part V)

**Problem — The throat cheque**
*Given:* tunnel throat area per side $A_t = 0.045\ \text{m}^2$; mean throat velocity $V_t = 55$ m/s at 250 km/h (69.4 m/s) car speed; throat static pressure corresponds to $C_p = -1.8$; floor planform area affected 1.6 m² total (both sides, plan-view). $\rho = 1.225$, $q = 2{,}951$ Pa (from Part II).
*Required:* (a) throat suction pressure; (b) rough downforce contribution of the tunnel region; (c) the mass flow through both tunnels.
*Solution:*
(a) $p_{suction} = C_p q = -1.8 \times 2{,}951 \approx -5.3\ \text{kPa}$ (gauge).
(b) With suction acting over the planform: $F \approx 5.3\ \text{kPa} \times 1.6\ \text{m}^2 \approx 8.5\ \text{kN}$ — *more than the car's weight*, from a strip of floor ~30 cm wide. (Order-of-magnitude demonstration, not a design claim; real distributions are 3-D and partly recovered.)
(c) $\dot m = \rho A_t V_t \times 2 = 1.225 \times 0.045 \times 55 \times 2 \approx 6.1\ \text{kg/s}$ through the tunnels.
*Engineering interpretation:* tiny geometries × large dynamic pressures = car-weight forces. This is why millimetres of ride height are worth tenths of seconds — and why the recovery section (diffuser) is treated as carefully as the suction section.

---

## QUICK RECALL (Part V)

1. State the two mechanisms called "ground effect" and where each applies on the car.
2. What sets throat velocity? What sets throat pressure?
3. Why does the diffuser exist, and what happens when it stalls?
4. Sketch (describe) the downforce-vs-ride-height map and its three regimes.
5. What is the porpoising feedback loop, in terms of $dF/dh$ and suspension?
6. Why is "lower is always better" false — give the two physical limits.
7. How do pitch, roll and yaw each alter floor performance?
8. What makes floor-generated load more "efficient" than wing-generated load?
9. What did the 2022 Technical Directive and 2023 floor changes target?
10. In a Cp plot under the car, where is the strongest suction and why?

### ANSWERS

1. Wing-in-ground effect (image effect — wings/elements near ground) and underbody/venturi effect (floor tunnels) — modern cars use both, tunnels dominate.
2. Mass conservation through the inlet/geometry (and upstream supply); momentum balance converts that velocity into the local static pressure.
3. Recovers static pressure so throat suction can exist and the exit condition is healthy; stalled → recovery collapses, drag rises, load falls, instability risk.
4. Rise (enhancement), peak/plateau (design band), loss (choke/separation) as height decreases — Figure 5.2.
5. Steep negative slope of load vs height + spring compressibility → positive feedback → separation-triggered limit cycle.
6. Underbody choke (boundary-layer blockage) and inlet starvation/separation — plus suspension/mechanical limits (the map turns over).
7. Pitch changes expansion geometry and shifts load; roll unbalances edge sealing; yaw starves tunnels asymmetrically and weakens edge vortices.
8. Large actuation area, edge-sealed (low leakage), less induced-drag penalty than a low-AR free wing.
9. Limiting aerodynamic oscillations (driver exposure) and moving the force map away from instability via floor-edge/diffuser/plank geometry.
10. At the tunnel throat — minimum flow area, maximum velocity, hence minimum static pressure (with boundary-layer effects deciding how low it actually gets).

---

## SOURCES (Part V)

- Zerihan, J. & Zhang, X., "Aerodynamics of a Single Element Wing in Ground Effect", *Journal of Aircraft* 37(6), 2000, pp. 1058–1064 (DOI: 10.2514/2.2711) — force enhancement/loss regimes vs $h/c$; tip-vortex breakdown. [Tier 1]
- Zhang, X. & Zerihan, J., "Aerodynamics of a Double-Element Wing in Ground Effect", *AIAA Journal* 41(6), 2003, pp. 1007–1016 (DOI: 10.2514/2.2057) — abrupt force discontinuity at low clearance from tip-vortex breakdown. [Tier 1]
- Ranzenbach, R. & Barlow, J., "Cambered Airfoil in Ground Effect — Wind Tunnel and Road Conditions", AIAA 95-1909 (1996; also SAE 942509, 1994) — under-wing throttling/force loss at low clearance. [Tier 1]
- Zhang, X., Toet, W. & Zerihan, J., "Ground Effect Aerodynamics of Race Cars", *Applied Mechanics Reviews* 59(1), 2006, pp. 33–49 (DOI: 10.1115/1.2110263) — the canonical review of downforce devices. [Tier 1]
- Gadola, M. et al., "Analyzing Porpoising on High Downforce Race Cars…", *Energies* 15(18):6677, 2022 (DOI: 10.3390/en15186677) — porpoising as aerodynamic instability; setup mitigations. [Tier 1]
- Katz, J., *Race Car Aerodynamics*, Bentley (1995) — underbody and diffuser fundamentals. [Tier 1]
- FIA Formula 1 Technical Regulations (2022+) and FIA technical communications 2022–2023 — venturi tunnels, oscillation directive, floor geometry changes. [Tier 1]
- Toet, W., "Aerodynamics and aerodynamic research in Formula 1", *The Aeronautical Journal* 117(1187), 2013 (DOI: 10.1017/S0001924000007739) — underbody/diffuser practice from F1 experience. [Tier 2]
