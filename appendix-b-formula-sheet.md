# Appendix B — Formula Sheet

One page, in dependency order. Assumptions stated compactly — an equation without its assumptions is a trap.

## Fluid mechanics

| # | Relation | Assumptions / notes |
|---|---|---|
| F1 | $\rho = m/V$; $p=\rho RT$ | ideal gas |
| F2 | $q = \tfrac12\rho V^2$ | definition — "the currency" |
| F3 | $p_0 = p + q$ | incompressible; along streamline, no loss |
| F4 | $A_1V_1 = A_2V_2$ | steady, incompressible streamtube |
| F5 | $p + \tfrac12\rho V^2 + \rho gz = $ const | steady, incompressible, inviscid, along streamline (z negligible in air) |
| F6 | $Re = VL/\nu$ | dynamic similarity |
| F7 | $Ma = V/a$, $a=\sqrt{\gamma RT}$ | incompressible OK for $Ma \lesssim 0.3$ |
| F8 | $\tau = \mu\,\partial u/\partial y$; no-slip at walls | Newtonian fluid |

## Force generation

| # | Relation | Assumptions / notes |
|---|---|---|
| F9 | $\vec F = \oint_S(-p\vec n + \vec\tau)\,dS$ | the only two mechanisms |
| F10 | $C_p=(p-p_\infty)/q_\infty$ | stagnation $=+1$ |
| F11 | $C_L = L/(qS)$; $C_D = D/(qS)$; F1 quotes $C_LA$, $C_DA$ [m²] | reference-area convention |
| F12 | $c_l = 2\pi(\alpha-\alpha_{L0})$ | thin-airfoil, incompressible, small α |
| F13 | $L' = \rho V_\infty\Gamma$ | Kutta–Joukowski, 2-D |
| F14 | $C_{D,i} = C_L^2/(\pi e\, AR)$ | lifting-line; low AR hurts (F1!) |
| F15 | $AR = b^2/S$ | — |

## Ground effect / underbody

| # | Relation | Assumptions / notes |
|---|---|---|
| G1 | $\dot m = \rho A V$ through inlet/throat/exit | 1-D streamtube model |
| G2 | suction $\Delta p \approx q_\infty\,|C_{p,min}|$ at throat | ideal; BL reduces it |
| G3 | force map: $F(h/c)$ rises → peaks (~0.08–0.1) → falls (choke) | measured (Z&Z 2000; R&B) |
| G4 | stability: flat/positive $dF/dh$ at operating point | porpoising criterion (Part V) |

## Vehicle / balance

| # | Relation | Assumptions / notes |
|---|---|---|
| V1 | $a_{y,max} \approx \mu(mg + qC_LA)/m$ | grip from load; μ sub-linear in reality (load sensitivity) |
| V2 | $\%front = F_{DF,front}/(F_{DF,front}+F_{DF,rear})$ | aero balance |
| V3 | $D = q\,C_DA$; $P = D\cdot V \propto V^3$ | the top-speed law |
| V4 | $\Delta V/V = (\Delta C_DA / C_DA)\cdot(-1/3)$ at fixed P | 2% drag cut ≈ +0.7% speed |

## Turbulence / CFD

| # | Relation | Assumptions / notes |
|---|---|---|
| C1 | N–S: $\rho\partial_t\vec V + \rho(\vec V\cdot\nabla)\vec V = -\nabla p + \mu\nabla^2\vec V + \vec f$ | incompressible, Newtonian, constant μ |
| C2 | $y^+ = y u_\tau/\nu$; $u_\tau=\sqrt{\tau_w/\rho}$ | targets: ~1 resolved; 30–300 wall-fn; **5–30 forbidden** |
| C3 | $C_f \approx 0.664/\sqrt{Re_x}$ (lam) / $\approx 0.059\,Re_x^{-1/5}$ (turb) | flat plate — for estimates |
| C4 | $\delta \approx 5x/\sqrt{Re_x}$ (lam) / $\approx 0.37x\,Re_x^{-1/5}$ (turb) | flat plate |
| C5 | GCI per Celik et al. (2008) | mesh-uncertainty reporting |
| C6 | convergence = flat force monitors (+ low residuals), at matched policy | Part XII |

## Numbers worth memorising

- $\rho = 1.225$ kg/m³ (ISA SL); $\nu = 1.46\times10^{-5}$ m²/s; $a ≈ 340$ m/s.
- $q$ at 300 km/h ≈ 4.25 kPa.
- $Re$ (0.25 m chord, 80 m/s) ≈ 1.4×10⁶.
- F1 car class: $C_LA ≈ 3.5$–5 m²; $C_DA ≈ 1.0$–1.7 m²; L/D ≈ 2.5–3.5 (public estimates).
- Downforce ≈ weight at ~180–210 km/h (setup-dependent).
- Wall-resolved first cell at F1 speeds: **~5 µm** (the reason wall functions exist).
