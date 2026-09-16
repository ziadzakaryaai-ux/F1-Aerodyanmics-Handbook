# PART XII — CFD Fundamentals

**Purpose:** build CFD from first principles so the F1 workflow (Part XIII) and result interpretation (Part XIV) rest on understanding rather than button-pushing. The chain to internalise: **physical problem → mathematical equations → numerical approximation → computational solution → engineering interpretation.**

**Course connection:** anchors: Versteeg & Malalasekera (the standard FVM text); Ferziger & Perić; Anderson, *CFD: The Basics with Applications*; Menter (1994) for turbulence models. Module mapping: ____________

---

## 12.1 What CFD actually does 🟢

CFD takes the conservation laws (Part I §1.7) and solves them numerically on a computer, replacing the continuous flow field with values stored at discrete points (cells). Nothing more, nothing less. Every CFD claim is only as good as the weakest link in: **equations → discretisation → mesh → boundary conditions → turbulence model → convergence → interpretation.**

![CFD domain, boundary conditions, mesh refinement.](diagrams/p12-mesh.svg)
*Figure 12.1 — The computational stage: a domain, its boundary conditions, and a mesh concentrated where the physics lives.*

---

## 12.2 The governing equations 🟢→🟡

For a Newtonian fluid, the **Navier–Stokes equations** are mass + momentum + energy conservation written locally. For F1 aerodynamics (incompressible, near-constant temperature in the external flow), the essential system is:

**Continuity:** $\nabla \cdot \vec{V} = 0$

**Momentum (incompressible N–S):**
$$\underbrace{\rho\frac{\partial \vec{V}}{\partial t}}_{\text{inertia}} + \underbrace{\rho (\vec{V}\cdot\nabla)\vec{V}}_{\text{convection (nonlinear!)}} = \underbrace{-\nabla p}_{\text{pressure}} + \underbrace{\mu \nabla^2 \vec{V}}_{\text{viscous}} + \vec{f}$$

| Term | Meaning | F1 relevance |
|---|---|---|
| $\rho \partial \vec V/\partial t$ | local (temporal) acceleration | matters in URANS/LES; zero in steady RANS |
| $\rho(\vec V \cdot \nabla)\vec V$ | convective acceleration | the nonlinearity that creates turbulence and makes CFD hard |
| $-\nabla p$ | pressure force | the force currency (Part II) |
| $\mu \nabla^2 \vec V$ | viscous diffusion | boundary layers, wakes, everything Part II built |

*Assumptions above:* incompressible Newtonian fluid, constant $\mu$. *The energy equation* matters when heat transfer (cooling flows, brake ducts) is part of the question.

**Why turbulence breaks direct solution.** At F1 Reynolds numbers, the N–S solutions are turbulent: a continuum of eddies from car-size (metres) down to Kolmogorov scales (fractions of a millimetre). Resolving *all* of them (Direct Numerical Simulation, DNS) costs scaling ~$Re^3$ in time-stepped grid points — utterly impossible for a race car. **Every practical CFD is therefore a turbulence-modelled approximation.** This single sentence is the most important thing in this part.

---

## 12.3 Discretisation and the Finite Volume Method 🟡

The dominant industrial method is the **Finite Volume Method (FVM)**: integrate the equations over each cell; fluxes in minus fluxes out = accumulation. Gives conservative, geometry-flexible schemes.

- **Spatial discretisation:** gradients and fluxes via interpolations of cell-centred (or node) values. Convective schemes trade accuracy against stability: upwind-family schemes are robust but **numerically diffusive** (§12.7); central schemes are sharper but less stable.
- **Temporal discretisation:** explicit (cheap, stability-limited time step) vs implicit (larger steps, per-step solve); for steady RANS the "time" is a relaxation device.
- **Pressure–velocity coupling:** incompressible N–S has no standalone pressure equation — solvers iterate (SIMPLE/PISO/PIMPLE families or fully coupled schemes) so that velocity and pressure simultaneously satisfy momentum and continuity.
- **Linear solvers:** each step reduces to huge sparse linear systems (multigrid, Krylov methods) — the reason F1 CFD is an HPC problem (Part XIII).

---

## 12.4 Domain, mesh, boundary conditions 🟡

**Domain (Fig. 12.1):** must let the physics breathe — several car lengths downstream for the wake, enough upstream for the inlet condition to relax, walls far enough that they don't squeeze the flow (the CFD twin of wind-tunnel blockage, Part XI §11.4).

**Mesh:** the error budget lives here.
- **Refinement where gradients live:** boundary layers, underbody, wakes (Fig. 12.1's boxes) — uniform meshes waste everything.
- **Inflation/prism layers** hugging surfaces resolve the boundary layer; their count/height set your **y⁺** (§12.6).
- **Quality metrics:** skewness, aspect ratio, size jump. Bad cells locally corrupt solutions globally (transport equations carry the damage downstream).
- **Mesh count:** F1 full-car meshes run in the tens-to-hundreds of millions of cells (public statements across teams); the *distribution* matters more than the count.

**Boundary conditions (BCs):**
- Inlet: velocity (or total pressure) + turbulence quantities ($k$, $\omega$ or $\epsilon$ — inlet turbulence is a *choice* with consequences for wakes).
- Outlet: static pressure (with non-reflecting/zero-gradient conventions).
- Ground: **moving wall** at car speed (the rolling road, Part XI).
- Wheels: rotating walls / multiple reference frames or sliding meshes.
- Car surfaces: no-slip walls (+ roughness/transition treatments if modelled).
- Symmetry (halved domain — at the cost of modelling yawed/unsteady asymmetries) vs full domain.

**COMMON MISCONCEPTIONS (setup)**
> ❌ **"A bigger domain is always safer."** True only up to resolution: domain growth steals cells from the boundary layer. The domain is an *optimisation*, not a comfort blanket.
>
> ❌ **"Inlet turbulence doesn't matter."** It feeds the wake's turbulence model and decay; two designs can rank differently under different inlet turbulence. Match it to tunnel/track conventions.
>
> ❌ **"Symmetry halves the cost for free."** It forbids asymmetry — wheels' wakes are not symmetric; steady-state symmetry is a modelling decision with physics consequences.

---

## 12.5 Turbulence modelling: RANS, URANS, LES, DES 🟡→🔴

**The closure problem.** Reynolds-averaging the N–S (splitting velocity into mean + fluctuation) generates unknown **Reynolds stresses**; the model must express them via known quantities. The workhorse assumption (Boussinesq) makes turbulence act like an extra viscosity — the **eddy viscosity** $\mu_t$ — computed from transport equations:

- **RANS (steady):** time-averaged equations; one steady solution. The F1 workhorse: cheap per design point, statistics-laden but *stable*, and adequate for attached/weakly-unsteady flows. Under-predicts unsteady loading and can mishandle massive separation.
- **k-ε:** robust, wall-function oriented; poor in adverse pressure gradients — historically superseded for wings.
- **k-ω SST (Menter, 1994):** blends k-ω's near-wall accuracy with k-ε's freestream robustness; strong adverse-pressure-gradient/separation behaviour. *The de-facto motorsport standard.* Know why it's chosen, not just that it's chosen.
- **Spalart–Allmaras:** one transport equation, excellent for attached aerodynamic flows; used for wing-focused studies.
- **URANS:** unsteady RANS — time-stepped RANS resolving the *large* forced/mean unsteadiness (e.g., porpoising-scale motion) while modelling the rest.
- **LES:** resolves the energy-containing large eddies, models only subgrid scales. Brutally expensive at full-car $Re$; used in research slices (wheel, mirror, local separation), not weekly development.
- **DES / hybrid (DDES, IDDES):** RANS near walls, LES-like behaviour in separated regions — the practical middle ground for unsteady separated flows.

*Model choice is a physics decision:* attached-load deltas (RANS/SST), unsteady separation physics (URANS minimum, DES better), turbulence-decay-sensitive wake studies (watch RANS's eddy-viscosity over-diffusion — §12.7).

---

## 12.6 Wall treatment and y⁺ 🟡

$y^+ = \frac{y \, u_\tau}{\nu}$ — the distance of the first cell centre from the wall in wall units ($u_\tau = \sqrt{\tau_w/\rho}$). It decides which near-wall treatment is valid:

| Approach | y⁺ target | What it assumes |
|---|---|---|
| Wall-resolved (low-Re models) | ~1 (up to ~4–5 acceptable) | resolves the viscous sublayer directly; needs many prism layers |
| Wall functions | 30–300 (~30 ideal) | bridging laws assume a log-layer exists at that location |
| **The forbidden zone** | **5–30** | neither formulation valid — results silently wrong |

(CFD-Online's near-wall treatment guidance is the standard citation: y+ ≈ 1 for low-Re; 30–300 for wall functions; the buffer band 5–30 is covered by neither.)

The trap: y⁺ varies over the car with speed and attitude. A mesh fine at one speed is in the forbidden zone at another — teams manage per-project y⁺ maps. High-quality separations/wake predictions are wall-treatment-sensitive: a boundary layer modelled with wall functions at y⁺=60 near a suction peak behaves differently from a resolved one.

---

## 12.7 Convergence, residuals, numerical diffusion 🟡→🔴

![Convergence: residuals and force monitors.](diagrams/p12-convergence.png)
*Figure 12.2 — Residuals falling is necessary; the integral monitors (forces) flattening is the actual convergence criterion.*

- **Residuals** measure how well the discrete equations are satisfied *this iteration*. Falling residuals = the solution is settling. But low residuals with drifting forces (or vice versa) both happen; **converge on monitors** (forces, moments, mass-flow balances) with residuals as backup.
- **Steady RANS on inherently unsteady flow** (massively separated wheels/wakes) converges to an *artificial steady state* — a time-average-like compromise. Forces can wobble at low level; teams average monitor windows and standardise stopping criteria (consistent practice matters more than any single number).
- **Initialisation:** uniform freestream vs potential-flow/partial-map initialisation — affects path (and sometimes the local minimum reached), not the converged truth.
- **Numerical diffusion:** discretisation error that *smears* gradients like an artificial viscosity. Upwind schemes on coarse cells diffuse wakes and vortices; it can kill a vortex that reality keeps — making downstream devices look worse than they are. Countermeasures: better schemes (bounded central/second-order), refinement zones, mesh-quality discipline.
- **Under-relaxation/CFL:** stability knobs; too-aggressive settings invent "convergence" that isn't physical.

---

## 12.8 Mesh independence, verification, validation 🔴

**Mesh independence (grid convergence).** Refine the mesh systematically (e.g., ×1.5 in each direction) and watch target quantities settle. Formalise with Richardson extrapolation / the **Grid Convergence Index (GCI)** per the ASME procedure (Celik et al., 2008): report the *uncertainty band* of your discretisation, not just "we refined it".

**Verification vs validation — keep them separate:**
- **Verification:** "are we solving the equations right?" — code/solution accuracy: convergence studies, benchmarks.
- **Validation:** "are we solving the right equations (model)?" — comparison with experiment: tunnel forces, pressure taps, rakes.
A perfectly verified simulation of the wrong turbulence model is precisely-validated-nothing.

**ENGINEERING INTUITION**
> If you remember only one thing: CFD is an instrument with an error bar, like a wind tunnel — except its errors are *systematic, invisible and cheap to ignore*. The discipline is quantifying them (mesh, model, convergence) before believing a delta.

---

## COMMON MISCONCEPTIONS (Part XII)

> ❌ **"CFD solves the real equations, so it's exact."** It solves modelled, discretised equations — every stage adds error (§12.2–12.8). DNS at car scale would need exascale-era resources no team has.
>
> ❌ **"More cells = better."** More *well-placed* cells; a bigger uniformly-meshed domain is a worse instrument than a smaller graded one.
>
> ❌ **"Residuals at 10⁻⁶ mean converged."** Residuals are per-equation satisfaction; the design quantities must also be flat (Fig. 12.2). Engineers converge on Δ forces, not on residual vanity.
>
> ❌ **"k-ε / k-ω / SST are interchangeable."** Each encodes assumptions; in adverse gradients and wakes they disagree — sometimes enough to flip a design ranking.
>
> ❌ **"y⁺ is a post-processing check."** It's a *design input* for the mesh; discovering bad y⁺ after the run means re-meshing, and results from the buffer zone are not "a bit off" — they're structurally unsupported.
>
> ❌ **"Steady RANS captures wheel wakes."** It produces a frozen average; load interactions dependent on unsteadiness are under-represented. That's a modelling choice with known limits, not a truth.

---

## F1 ENGINEERING QUESTIONS (Part XII)

**Conceptual**
- Why is DNS impossible at car scale — quantify the scaling argument.
- What physical assumption does the Boussinesq eddy-viscosity hypothesis make, and where does it fail on an F1 car?
- Why does the pressure need an iterative coupling scheme at all?

**Engineering**
- Your team must choose SST vs SA for a front-wing campaign. What flow features decide, and what would you benchmark first?
- A colleague reports "converged" with residuals 10⁻⁵ but forces still drifting ±0.3%. Diagnose.

**CFD**
- Design the mesh strategy for a yaw sweep from 0° to 10°: what changes and what must stay fixed for fair deltas?
- How would you *measure* numerical diffusion of the wake in your own setup?

**Design**
- Build a validation ladder for a new floor concept: which experiment (tunnel forces, taps, rakes, track) validates which CFD claim?
- Your manager asks for LES "because it's more accurate". Compose the engineering reply.

---

## MINI PROBLEM (Part XII)

**Problem — First-cell height for wall-resolved y⁺**
*Given:* car speed 80 m/s; characteristic length 0.3 m (wing chord); ν = 1.46×10⁻⁵ m²/s. *Required:* first-cell height for y⁺ ≈ 1.
*Solution:*
$Re = VL/\nu = 80 \times 0.3 / 1.46\times10^{-5} \approx 1.64\times10^6$.
Flat-plate estimate: $C_f \approx 0.026/Re^{1/7} \approx 0.026/11.4 \approx 0.0023$; $u_\tau = V\sqrt{C_f/2} \approx 80 \times 0.034 \approx 2.7$ m/s.
$y = y^+ \nu / u_\tau = 1 \times 1.46\times10^{-5}/2.7 \approx 5.4\ \mu m$ — first cell centre ~5 µm off the wall, with growth ratio ~1.2 to leave the sublayer properly.
*Engineering interpretation:* wall-resolved meshes are *expensive* (micron first cells over every surface) — the reason wall functions (y⁺ 30–300) remain attractive, and why y⁺ discipline per project is a real engineering decision, not hygiene.

---

## QUICK RECALL (Part XII)

1. Write the incompressible N–S momentum equation and name each term.
2. Why can't pressure be solved directly in incompressible CFD?
3. What is the closure problem, and what does Boussinesq assume?
4. Compare RANS, URANS, LES, DES in one line each (cost + what's resolved).
5. Why is SST the motorsport default? What does "SST" blend?
6. Give the y⁺ bands and the forbidden zone.
7. What is numerical diffusion, and which schemes/regions suffer most?
8. Define verification vs validation with one example each.
9. What does the GCI formalise?
10. Why is steady RANS on a car an "artificial steady state"?

### ANSWERS

1. $\rho\partial_t \vec V + \rho(\vec V\cdot\nabla)\vec V = -\nabla p + \mu\nabla^2\vec V + \vec f$: temporal inertia, convection, pressure, viscous, body forces.
2. Only the continuity constraint links p to V (no state equation for p); solvers iterate pressure–velocity coupling (SIMPLE/PISO/coupled).
3. Averaging generates unknown Reynolds stresses; Boussinesq models them as an isotropic eddy viscosity — fails where turbulence is strongly anisotropic/curved (vortices, massive separation, junctions).
4. RANS: steady, cheapest, all turbulence modelled. URANS: time-resolved large unsteadiness, rest modelled. LES: resolves large eddies, models subgrid — huge cost. DES: RANS near walls + LES in separated zones — practical hybrid.
5. k-ω accuracy near walls + k-ε robustness freestream; best-in-class adverse-gradient/separation behaviour (Menter 1994).
6. Resolved ≈1 (up to ~5); wall functions 30–300 (~30 ideal); 5–30 covered by neither.
7. Discretisation error acting like artificial viscosity; upwind schemes on coarse cells; kills gradients/wakes/vortices — worst exactly where F1 physics lives.
8. Verification: solving equations right (mesh convergence study); validation: solving right equations (compare to tunnel forces).
9. Discretisation-uncertainty reporting (Richardson extrapolation standardised by Celik et al. 2008).
10. Wheels/wakes are unsteady; steady RANS freezes a time-averaged compromise that no instant of the real flow resembles.

---

## SOURCES (Part XII)

- Versteeg, H. K. & Malalasekera, W., *An Introduction to Computational Fluid Dynamics: The Finite Volume Method*, Pearson (2nd ed., 2007) — FVM, discretisation, pressure–velocity coupling. [Tier 1]
- Ferziger, J. H. & Perić, M., *Computational Methods for Fluid Dynamics*, Springer (3rd rev. ed., 2002) — numerics, error analysis. [Tier 1]
- Menter, F. R., "Two-Equation Eddy-Viscosity Turbulence Models for Engineering Applications", *AIAA Journal* 32(8), 1994, pp. 1598–1605 — SST model. [Tier 1]
- Spalart, P. R. & Allmaras, S. R., "A One-Equation Turbulence Model for Aerodynamic Flows", AIAA 92-0439 (1992); *La Recherche Aérospatiale* (1), 1994 — SA model. [Tier 1]
- Celik, I. B., Ghia, U., Roache, P. J. & Freitas, C. J., "Procedure for Estimation and Reporting of Uncertainty Due to Discretization in CFD Applications", *ASME J. Fluids Engineering* 130(7), 2008 — GCI procedure. [Tier 1]
- CFD-Online Wiki: "Y plus wall distance estimation" and "Near wall treatment for k-omega models" — y⁺ bands. [Tier 2]
- Anderson, J. D., *Computational Fluid Dynamics: The Basics with Applications*, McGraw-Hill (1995) — accessible first-principles treatment. [Tier 1]
