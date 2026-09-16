# PART I — Fluid Mechanics Foundations

**Purpose:** build the physical vocabulary every later part depends on. Nothing here is optional: "ground effect" (Part V) is continuity plus a pressure field; "porpoising" (Part V) is an aerodynamic instability read through suspension; "y+" (Part XII) is boundary-layer scaling. Master this part and the rest of the handbook reads like application.

**Course connection:** this material corresponds to the opening modules of any aerodynamics course — canonical anchors are Anderson, *Fundamentals of Aerodynamics*, ch. 1–3, and any introductory fluid-mechanics text (continuity, Bernoulli, Reynolds number). Mark the module numbers here when you reach them: ____________

---

## 1.1 What is a fluid? 🟢

A **fluid** is any substance that flows — it deforms continuously under an applied shear stress, no matter how small. Liquids and gases are both fluids; air is a compressible fluid whose behaviour at F1 speeds is *almost* incompressible (§1.6).

**TERM — Fluid**
- **Simple:** anything that flows and takes the shape of its container.
- **Technical:** a continuum that deforms continuously under shear stress; characterised by density, pressure, temperature, viscosity.
- **F1 relevance:** the working "material" of the entire sport. Every component on the car is shaped to do something to this material.

**Why the continuum idea matters.** We treat air as a continuous medium even though it is molecules. That is valid when the object's length scale is much larger than the molecular mean free path (~70 nm at sea level) — trivially true for a race car. It is what allows us to define fields (velocity, pressure, density) at every point in space, which is exactly what CFD (Part XII) computes.

**ENGINEERING INTUITION**
> If you remember only one thing: aerodynamics is the management of a continuous fluid — everything an F1 car does is done *to air*, using geometry.

---

## 1.2 Density 🟢

**Definition:** mass per unit volume, $\rho = m/V$. **Units:** kg/m³.

| Condition | ρ (kg/m³) |
|---|---|
| ISA sea level, 15 °C, 101.325 kPa | **1.225** |
| Hot track day, ~35 °C sea level | ~1.15 |
| Mexico City (~2,200 m altitude) | ~0.98–1.00 |

Density enters every force: from $F = \tfrac12 \rho V^2 C A$, aerodynamic force scales *linearly* with density.

**F1 application:** Mexico City's altitude costs both engine power (less oxygen) and aerodynamic load (less dense air). Teams run maximum-downforce packages there and still corner slower than the wing levels suggest — the air itself is "thinner". Approximately 1% density change ≈ 1% downforce change at fixed speed (direct from the force equation).

**ENGINEERING INTUITION**
> Air is the working fluid AND the load-bearing structure. Half the reason setups differ between circuits is simply how much air there is per cubic metre that day.

---

## 1.3 Pressure 🟢

**Definition:** normal force per unit area, $p = F/A_\perp$. **Units:** Pa = N/m² (1 bar = 10⁵ Pa).

A fluid exerts pressure on every surface it touches, always *normal* to that surface. This single fact is the origin of **all** aerodynamic force: integrate the pressure over the car's surface and you have the pressure part of the aerodynamic force (Part II). The remaining part is skin friction, which is orders of magnitude smaller on most of the car — but decisive for how the pressure field develops (boundary layers, §1.5 and Part II).

**Static vs stagnation (total) vs dynamic pressure** — three names you must keep separate:

- **Static pressure $p$:** what a pressure gauge moving *with* the flow would feel; the random molecular "push" of the fluid.
- **Dynamic pressure $q$:** the kinetic energy per unit volume of the flow, $q = \tfrac12 \rho V^2$. It is the *currency* of aerodynamic force.
- **Stagnation (total) pressure $p_0$:** the static pressure the flow would reach if brought isentropically to rest: $p_0 = p + q$.

**F1 application:** pitot-static probes measure $p$ and $p_0$ to give airspeed. Surface pressure taps and pressure-sensitive paint map $p$ on wings. The whole of downforce generation is a *redistribution of static pressure* over the car's surfaces, paid for out of dynamic pressure.

---

## 1.4 Temperature 🟢

**Definition:** measure of molecular kinetic energy. **Units:** K (use Kelvin in every formula).

Through the ideal gas law $p = \rho R T$ (with $R_{air} = 287$ J/(kg·K)), temperature sets density at a given pressure: hot air is less dense, cold air denser. Temperature also raises viscosity (Sutherland's law: $\mu \propto T^{1.5}/(T+110.4)$), which slightly changes Reynolds numbers (§1.9).

**F1 application:** a hot afternoon moves $\rho$, $\mu$, and the boundary-layer behaviour simultaneously. This is one reason "track temperature" correlates with setup and why identical wing levels produce different speeds at the same circuit across a weekend. Approximately: 10 K of air-temperature rise at constant pressure costs ~3% density (engineering inference from the ideal gas law).

---

## 1.5 Viscosity 🟢

**TERM — Viscosity**
- **Simple:** the fluid's internal "stickiness" — its resistance to shearing.
- **Technical:** dynamic viscosity $\mu$ [Pa·s] relates shear stress to velocity gradient: $\tau = \mu \, du/dy$. Kinematic viscosity $\nu = \mu/\rho$ [m²/s].
- **F1 relevance:** without viscosity there is no boundary layer (Part II), no separation, no wheel wake, no vortex roll-up with well-defined cores — and also no lift-generating pressure fields as we know them. Viscosity is tiny in its magnitude and enormous in its consequences.

For air at 15 °C: $\mu \approx 1.79\times10^{-5}$ Pa·s, $\nu \approx 1.46\times10^{-5}$ m²/s.

**The no-slip condition:** at a solid surface the fluid sticks — velocity equals the wall's velocity (zero for a static wall). Every velocity profile you will ever see in a boundary layer starts from this condition. On a rotating wheel (Part IX) the *wall itself moves*, which is why wheel aerodynamics is its own discipline.

**ENGINEERING INTUITION**
> Viscosity is the tax collector of aerodynamics: it takes momentum away from the flow near surfaces and converts orderly kinetic energy into heat and turbulence. Almost every "bad" thing that happens to an F1 car (separation, stall, dirty air) is a downstream consequence of the tax.

---

## 1.6 Compressibility and the Mach number 🟢

**Mach number** $Ma = V/a$, where $a = \sqrt{\gamma R T}$ is the speed of sound (≈ 340 m/s at 15 °C, $\gamma = 1.4$).

Below roughly $Ma \approx 0.3$, density changes in the flow are small (order $Ma^2/2$: about 4.5% at Ma = 0.3) and the incompressible assumption is acceptable.

**F1 application:** a car at 330 km/h has $Ma_\infty \approx 0.27$ — F1 is a low-Mach problem in the free stream. Local accelerations (wing suction peaks, venturi throats) push local Mach somewhat higher, but Formula 1 aerodynamics is fundamentally an **incompressible** subject. Contrast this with propellers, or with the 2026-era power units' compressor side, where compressibility dominates. Keep the term "compressibility effects" out of your F1 explanations unless you are talking about local flow detail — it is almost never the mechanism you think it is.

---

## 1.7 Conservation laws: mass, momentum, energy 🟢→🟡

All of fluid mechanics, and all of CFD, is three conservation statements applied to a control volume:

**Mass (continuity).** Mass is neither created nor destroyed. For incompressible flow:

$$\nabla \cdot \vec{V} = 0 \qquad \text{(3-D form)}, \qquad A_1 V_1 = A_2 V_2 \qquad \text{(1-D streamtube form)}$$

| Variable | Meaning | Units |
|---|---|---|
| $A$ | cross-sectional area of the streamtube | m² |
| $V$ | mean velocity through that area | m/s |

*Meaning:* if the tube narrows, the flow must speed up — velocity is not a free parameter, it is a *consequence* of geometry and mass conservation.
*Assumptions:* incompressible, steady, single inlet/outlet for the 1-D form.
*F1 application:* the 2022+ floor **venturi tunnels** (Part V) are a designed streamtube: ramp and roof geometry squeeze the area, the flow accelerates, the static pressure drops, the floor is pushed down. Sidepod inlets, cooling ducts and brake ducts obey the same law.

**Momentum.** Newton's second law for a control volume: the sum of forces (pressure + viscous + body) equals the net flux of momentum out of the volume. Two uses you must internalise:

1. *Integral form* — you can compute the force on a body by surrounding it with a control volume and measuring momentum change at the boundaries. This is how wake surveys and aero rakes (Parts IX, XI) measure drag without touching the car.
2. *Differential form* — the **Navier–Stokes equations** (written out and dissected in Part XII) are the momentum statement made local. CFD solves exactly this.

**Energy.** Energy is conserved; for flowing air it trades between kinetic energy, pressure work, and heat (via viscosity and turbulence). No moving surface does work on the air except through moving walls (rotating wheels, the ground belt) — the car's engine pays for every joule the air carries away.

---

## 1.8 The Bernoulli equation 🟢 (and how not to misuse it)

For steady, incompressible, inviscid flow **along a single streamline** (or across a boundary layer where viscous effects are negligible):

$$p + \tfrac12 \rho V^2 + \rho g z = \text{constant}$$

| Variable | Meaning | Units |
|---|---|---|
| $p$ | static pressure | Pa |
| $\tfrac12\rho V^2$ | dynamic pressure $q$ | Pa |
| $\rho g z$ | hydrostatic head (negligible for air at car scale) | Pa |

**Physical meaning:** it is an energy statement. Along the streamline, pressure energy and kinetic energy convert into each other with no losses. Where the flow accelerates, static pressure *must* fall; where it decelerates, static pressure *must* rise.

**Assumptions — and they are strict:** steady, incompressible, **inviscid along that streamline**, no shaft work, no heat addition. Cross a wake, a separation region, or a shock, and Bernoulli's constant changes. This is why the total pressure in a tyre's wake (Part IX) is *lower* than the free stream: viscosity destroyed mechanical energy into heat.

![Venturi duct: area change drives velocity change and the pressure field.](diagrams/p01-venturi.png)
*Figure 1.1 — A venturi is mass conservation (top) and the energy/pressure relationship (bottom) working together. The F1 floor tunnel is this device, inverted and run under a moving car.*

**COMMON MISCONCEPTIONS**
> ❌ **"Bernoulli explains lift."** Incomplete. Bernoulli is a *bookkeeping relation* between velocity and pressure along a streamline — it says nothing about *why* the velocity field has the shape it does. The causal chain is: body geometry + flow constraints → streamline curvature and momentum change → pressure field → (and only then) you may use Bernoulli to relate that pressure to local speed. Lift is caused by the fluid being *deflected* — a momentum change — and the pressure field that goes with it (Part II).
>
> ❌ **"Fast air has low pressure because of Bernoulli."** Reversed logic. The pressure gradient is set by the flow's momentum balance (curvature, deflection); the speed change accompanies it. Bernoulli is the accounting identity, not the mechanism.
>
> ✅ **Correct use in F1:** quantitative bookkeeping between known states — e.g., estimating the static pressure drop along the floor throat from the velocity ratio.

**ENGINEERING INTUITION**
> If you remember only one thing: Bernoulli tells you what pressure goes with a velocity; it does not tell you why the velocity is there. The *why* is always geometry + conservation of momentum.

---

## 1.9 Reynolds number 🟢→🟡 (the master parameter)

$$Re = \frac{\rho V L}{\mu} = \frac{V L}{\nu}$$

| Variable | Meaning | Units |
|---|---|---|
| $V$ | characteristic velocity | m/s |
| $L$ | characteristic length (chord, car length…) | m |
| $\nu$ | kinematic viscosity | m²/s |

**Meaning:** the ratio of inertial to viscous forces. Two flows with the same $Re$ (and the same geometry and Mach) are dynamically similar — this is the entire theoretical basis of scale-model testing (Part XI) and of mesh/y⁺ reasoning in CFD (Part XII).

**F1 numbers (order of magnitude, engineering inference from public geometry):**
- Front-wing element, chord ~0.2–0.3 m at 80 m/s: $Re \approx 1.1$–$1.6\times10^6$.
- Full car at 80 m/s, length ~5.5 m: $Re \approx 3\times10^7$.
- A 50%-scale wind-tunnel model at ~40 m/s: $Re$ roughly an order of magnitude lower than full scale — small enough to matter for laminar/turbulent behaviour, handled with transition trips and experience (Part XI).

**Why it matters:** $Re$ sets where boundary layers transition from laminar to turbulent, how thick they are, where they separate, and hence lift, drag, stall behaviour and wake structure. A wing at $Re = 10^5$ is a *different aero device* from the same wing at $10^6$.

---

## 1.10 Streamlines and flow fields 🟢

- A **flow field** is the vector field $\vec{V}(x,y,z,t)$ of fluid velocity — the complete state of the air.
- A **streamline** is the instantaneous line everywhere tangent to $\vec{V}$. In steady flow, streamlines are the paths fluid particles follow. In unsteady flow they are not — a distinction CFD post-processing constantly abuses (Part XIV).
- A **streamtube** is a bundle of streamlines; the 1-D continuity law applies to it.
- **Pathlines / streaklines:** actual particle trajectories / smoke trails. Smoke wand tests visualise streaklines.

**F1 application:** "flow field" is the mental object every aerodynamicist carries: pressure maps, velocity slices, streamlines and vortices are all views of the same underlying $\vec{V}(x,y,z)$ and $p(x,y,z)$. Getting fluent at mentally switching between these views is most of "learning to read CFD" (Part XIV).

---

## 1.11 Laminar vs turbulent flow 🟢→🟡

At low $Re$ flows are **laminar**: fluid moves in smooth sheets, mixing only by molecular diffusion. Above a critical $Re$ (with disturbance amplitude, surface roughness and free-stream turbulence all involved) flow becomes **turbulent**: superimposed chaotic, three-dimensional fluctuations that transport momentum violently.

![Boundary-layer growth and transition.](diagrams/p01-boundary-layer.png)
*Figure 1.2 — Laminar layers are thin and orderly; turbulent layers are thicker, fuller, and mix far more. Both properties matter: skin friction is higher in turbulent flow, but resistance to separation is also higher.*

Key consequences to hold simultaneously in mind:

| Property | Laminar | Turbulent |
|---|---|---|
| Skin friction (same $Re$) | lower | **higher** |
| Mixing / momentum transport | weak | **strong** |
| Resistance to adverse pressure gradients | poor | **better** |
| Separation behaviour | separates earlier | separates later |
| Predictability in CFD | exact equations suffice | requires turbulence modelling (Part XII) |

**F1 application:** teams would love laminar flow over much of the car (less drag) but must accept turbulent boundary layers wherever separation looms (wings at high load, the diffuser). Wind-tunnel models use **trip dots** to force realistic transition at model $Re$. "Laminar vs turbulent" is not a good-vs-bad choice; it is a local trade you place deliberately (Part II, §boundary layers).

**ENGINEERING INTUITION**
> Laminar flow is a friction-cheap but separation-fragile business partner; turbulent flow is expensive but robust. Engineering is deciding, location by location, which one you hire.

---

## COMMON MISCONCEPTIONS (Part I)

> ❌ **"Air accelerates because pressure drops." / "Pressure drops because air accelerates."** Neither is a cause; both accompany each other through the momentum balance. The cause is geometry constraining the flow, plus Newton's second law.
>
> ❌ **"The flow in a venturi speeds up so the pressure can drop."** Teleology — flows have no intentions. The throat *forces* acceleration via continuity; the pressure field follows from momentum conservation.
>
> ❌ **"Compressibility matters at F1 speeds."** Free-stream Mach at 330 km/h ≈ 0.27. Density effects are second-order. (Wave drag, Mach cones etc. belong to other vehicles.)
>
> ❌ **"Reynolds number matching is optional in model tests."** Without managing $Re$ (and transition), model data does not scale — this is the first thing that breaks wind-tunnel-to-track correlation.
>
> ❌ **"Turbulence = bad, laminar = good."** Turbulence costs skin friction but buys separation resistance. Wheels and wakes are turbulent whether you like it or not; the design question is where you want the *transition line* and what you do with the turbulent momentum.

---

## F1 ENGINEERING QUESTIONS (Part I)

**Conceptual**
- Why does the same car produce less downforce in Mexico City than at Monza at the same speed — and why is the *drag* also lower?
- What physically happens to the Bernoulli constant of fluid passing through a tyre wake?
- Why is the free-stream Mach number a nearly irrelevant parameter for F1 but the Reynolds number a nearly decisive one?

**Engineering**
- The air is 5 °C cooler on Sunday than Friday. Which parts of the aero map move, and in which direction?
- A rule change mandates a 15 mm higher floor edge. Where does the mass flow under the car go?

**CFD**
- Your CFD domain inlet is set to 45 m/s at sea-level ISA conditions. What three derived quantities does this fix before the solver runs?
- Why do CFD practitioners care about matching Reynolds *number*, not just velocity?

**Design**
- You are told a new floor increases underbody mass flow by 8% at fixed speed. What do you expect to happen to throat velocity and static pressure, assuming no separation?
- Where on the car would you deliberately *want* a turbulent boundary layer, and why?

---

## MINI PROBLEMS (Part I)

**Problem 1 — The currency of aerodynamics**
*Given:* car speed 300 km/h, ISA sea level ($\rho = 1.225$ kg/m³). *Required:* dynamic pressure $q$.
*Solution:*
$V = 300/3.6 = 83.3$ m/s. $q = \tfrac12 \rho V^2 = 0.5 \times 1.225 \times 83.3^2 \approx 4{,}253\ \text{Pa} \approx 4.25\ \text{kPa}$.
*Engineering interpretation:* the entire downforce budget of the car is this ~4.3 kPa times surface areas times coefficients. A floor area of ~1.5 m² working at an average $C_p$ of −1 would already see ~6 kN — the magnitudes in Part V are not exotic; they are this number multiplied by good design.

**Problem 2 — Scale-model similarity**
*Given:* full-scale wing chord 0.25 m at 80 m/s; 50% model at 40 m/s; $\nu = 1.46\times10^{-5}$ m²/s. *Required:* both Reynolds numbers, and the mismatch.
*Solution:*
Full scale: $Re = 80 \times 0.25 / 1.46\times10^{-5} \approx 1.37\times10^6$.
Model: $Re = 40 \times 0.125 / 1.46\times10^{-5} \approx 3.4\times10^5$ — a factor ~4 lower.
*Engineering interpretation:* the model runs at much lower $Re$, so its boundary layers are relatively thicker and its transition points different. Teams respond with trips, higher model speeds, and correlation experience. When someone tells you "wind tunnel says +2% downforce", the correct question is: "and how does that survive the Reynolds gap?"

---

## QUICK RECALL (Part I)

1. Write down the incompressible continuity equation and state what it says about velocity in a narrowing duct.
2. State the three forms of pressure and their relationship at a stagnation point.
3. What four assumptions sit behind the Bernoulli equation, and which one breaks inside a tyre wake?
4. Why does viscosity matter for lift even though lift is mostly a pressure force?
5. Compute (mentally) the order of $Re$ for a 0.25 m chord at 80 m/s in air.
6. What is the no-slip condition, and why does a rotating wheel make it interesting?
7. Why is F1 aerodynamics an incompressible problem, quantitatively?
8. What is the difference between a streamline and a pathline, and when does the difference matter?
9. Hot day at the track: what happens to $\rho$, $\mu$, and downforce at fixed speed?
10. Name two places on an F1 car where the 1-D continuity equation is the central design driver.

### ANSWERS

1. $\nabla \cdot \vec V = 0$; narrowing area ⇒ velocity must rise ($A_1V_1 = A_2V_2$) — velocity is set by geometry and mass conservation.
2. Static $p$, dynamic $q=\tfrac12\rho V^2$, stagnation $p_0$; at a stagnation point $p_0 = p + q$ (all of $q$ converted to $p$).
3. Steady, incompressible, inviscid (along the streamline), no work/heat. Inside a wake viscosity destroys mechanical energy — $p_0$ is no longer conserved.
4. Viscosity builds the boundary layer; boundary-layer state controls separation and where the pressure field can be maintained — without it the pressure field (hence lift) cannot be sustained.
5. $Re = VL/\nu \approx 80 \times 0.25 / 1.46\times10^{-5} \approx 1.4\times10^6$.
6. Fluid velocity equals wall velocity at the surface. A wheel's surface moves — the wall itself drags the air, creating jetting and an upward-pumped wake (Part IX).
7. $Ma = 83.3/340 \approx 0.25$–0.27 at 300+ km/h; density change ~$Ma^2/2 \lesssim 4\%$ — small enough to ignore for force estimation.
8. Streamline = tangent to instantaneous velocity; pathline = actual trajectory. They differ in unsteady flow — e.g., behind any oscillating/pulsed wake, or in URANS/LES post-processing (Part XIV).
9. $\rho$ falls (ideal gas law), $\mu$ rises slightly (Sutherland), so downforce falls roughly in proportion to $\rho$ and $Re$ shifts slightly.
10. Floor venturi tunnels and sidepod/cooling inlets (also brake ducts; any internal duct).

---

## SOURCES (Part I)

- Anderson, J. D., *Fundamentals of Aerodynamics*, McGraw-Hill (6th ed., 2017) — fluid properties, control-volume laws, Bernoulli, Reynolds number. [Tier 1]
- White, F. M., *Fluid Mechanics*, McGraw-Hill (8th ed., 2015) — continuum assumption, viscosity, laminar/turbulent distinction. [Tier 1]
- Katz, J., *Race Car Aerodynamics: Designing for Speed*, Bentley Publishers (1995) — race-car application of dynamic pressure, density effects. [Tier 1]
- FIA Formula 1 Technical Regulations (current edition) — geometry context for tunnels/inlets; see bibliography for the edition consulted. [Tier 1]
