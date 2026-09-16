# PART XVIII — Engineering Audit

The final audit required by the handbook's method: where the evidence is strong, where it is weak, where public information is incomplete, and what to verify yourself. Honesty here is the difference between a reference and a rumor-mill.

## 18.1 Verification status by claim class

**✅ VERIFIED (checked against primary/reputable sources during construction)**

- Ground-effect force behaviour vs ride height: enhancement regime, peak near $h/c \approx 0.08$–0.1, force loss below ~0.1, abrupt double-element discontinuity at $h/c \approx 0.17$–0.24 (Zerihan & Zhang 2000, *J. Aircraft* 37(6); Zhang & Zerihan 2003, *AIAA J.* 41(6); Ranzenbach & Barlow AIAA 95-1909 / SAE 942509) — DOIs in bibliography.
- The canonical review: Zhang, Toet & Zerihan, *Applied Mechanics Reviews* 59(1), 2006.
- Rotating-wheel flow structure (CVP, jetting, upwash, rotation effects incl. ~10%+ drag reduction vs stationary): Mears/Dominy/Sims-Williams SAE 2002-01-3290; Axerio-Cilies & Iaccarino *ASME JFE* 134(12), 2012; McManus & Zhang 2006.
- All textbook citations (editions/years/publishers): Katz 1995; McBeath 3rd ed. 2015; Hucho 4th ed. 1998; Barnard 2nd ed. 2001; Anderson 6th ed. 2017; Versteeg & Malalasekera 2007; Ferziger & Perić 2002; Barlow/Rae/Pope 3rd ed. 1999; Milliken & Milliken 1995.
- CFD canon: Menter 1994 (*AIAA J.* 32(8), pp. 1598–1605); Spalart–Allmaras (AIAA 92-0439; *La Recherche Aérospatiale* (1), 1994); Celik et al. 2008 (*ASME JFE* 130(7)) — the GCI procedure.
- y⁺ bands (≈1 wall-resolved; 30–300 wall functions; 5–30 uncovered): CFD-Online wiki pages, fetched directly.
- Toet (2013), *The Aeronautical Journal* 117(1187) — citation and scope verified.
- Porpoising mechanism literature: Gadola et al., *Energies* 15(18):6677, 2022; Kutz et al., arXiv:2211.11748 (heaving-wing normal-form analysis).
- DRS aerodynamic magnitudes at wing level (~50–80% wing-drag cut): Loução et al., *Fluids* 7(9):309, 2022; Monash DRS studies (partially verified).

**⚠️ PUBLICLY CIRCULATED, VERIFICATION PENDING (regulation specifics)**

*A dedicated regulation-verification pass was attempted but could not be completed within this build (source-check quota exhausted). The following figures are widely reported in reputable technical media and FIA communications, and are used in this handbook with explicit "verify" flags. Before relying on any of them in your own work, confirm against the current FIA documents:*

- DRS open-flap gap dimension (85 mm class) and current sporting-regulation usage detail (detection gap, zone rules).
- The FIA's 2022 wake figures ("~46% following-car downforce loss for the previous cars vs ~18% target/achieved at ~1 car length") — exact wording, distance and attribution vary between retellings; treat as order-of-magnitude until read in an FIA document.
- 2022 Technical Directive on aerodynamic oscillation (metric, measurement location, threshold) and the 2023 geometry changes (floor-edge raise ~15 mm class, diffuser/plank adjustments) — direction and intent are well documented; exact millimetres should be read from the regs.
- 2022 front-wing element count, floor-fence count, tunnel-count specifics.
- Aerodynamic Testing Restrictions current numbers (occupancy hours/runs, CFD tokens) — mechanism (sliding scale by championship position) is stable and documented; the numbers are revised periodically.
- Minimum weight (~800 kg class) and dimensions of the current cars.
- 2026 active-aero specifics (modes, actuation rules) — direction documented in FIA communications; detail still settling as of this handbook's construction.

**🏷️ ENGINEERING INFERENCE / TEACHING CONSTRUCTION (labelled as such in-text)**

- All numeric "orders of magnitude" for car-level $C_L A$ (3.5–5 m²), $C_D A$ (1.0–1.7 m²), L/D ≈ 2.5–3.5, component drag shares, aero-balance ranges (mid-40s % front), downforce-equals-weight speed (~180–210 km/h): consistent with public technical discussion, but *no team publishes these*. Use as calibration for scale, never as data.
- The four Part XV §15.2 case studies: constructed composites demonstrating the method; not accounts of any team's actual programme.
- All figure curves (venturi, Cp shapes, force map, polar, balance-vs-speed, convergence): illustrative shapes drawn to depict correct physics, annotated as such on each figure.
- The "typical" mesh sizes (tens–hundreds of millions of cells) and OpenFOAM-derived toolchain claims: public statements by engineers over the years; qualitative only.

## 18.2 Known simplifications (and why they're acceptable here)

1. **Bernoulli used pedagogically, not causally** — the handbook repeatedly separates bookkeeping from mechanism; some course material will blur this (flag it when you meet it).
2. **1-D streamtube model of the floor** (Part V): the real tunnel is strongly 3-D with edge leakage; the model is for mechanism, not prediction.
3. **Flat-plate boundary-layer estimates** (y⁺ mini-problem): real wings have pressure gradients; treat the 5 µm answer as an order-of-magnitude design input.
4. **Steady-RANS framing dominates Parts XII–XIV** because it dominates industry practice; LES/DES get conceptual treatment only. A dedicated turbulence-modeling course is the next step if that's your direction.
5. **Tyre modelling**: tyre load sensitivity is introduced as a fact of tyre mechanics without its physical derivation (rubber friction physics) — a whole subject of its own (Pacejka).
6. **Cooling-flow thermodynamics** simplified to momentum bookkeeping; real cooling design couples heat exchangers, pumps and power-unit efficiency.
7. **Vehicle dynamics** reduced to load transfer and balance; full treatment is Milliken & Milliken's book.

## 18.3 Where sources disagree (and what this handbook did)

- **"Ground effect = the air speeds up"** vs the momentum/continuity account: resolved in favour of the causal account throughout (Part I §1.8, Part V §5.1) — this is the academic consensus position.
- **Vortex "sealing" language**: between the paddock's confident shorthand and the literature's careful "leakage limitation", the handbook keeps the shorthand but defines it precisely (Part VI §6.3).
- **Porpoising attributions** (2022 season): press narratives variously blamed stiff suspensions, floor concepts or tyres; the peer-reviewed mechanism (aerodynamic negative damping via the force map) is what Part V teaches — suspension choices modulate, the map decides.
- **L/D and force-multiple figures** vary across public sources by setup and era; ranges, never point values, are quoted.

## 18.4 Recommended next steps (study plan)

1. **Verify the pending regulation items** directly in the FIA documents (fia.com → regulations; change logs per season). One focused evening closes the whole ⚠️ list above.
2. **Pair this handbook with your course**, annotating each part's *Course connection* line as you reach the matching module.
3. **Work a real geometry**: a simplified open-wheel body in OpenFOAM (or similar) at 3 attitudes × 2 yaw angles, applying Parts XII–XIV discipline end-to-end — the single highest-value exercise in this guide.
4. **Read one paper properly**: Zerihan & Zhang (2000) start-to-finish with the handbook open at Part V. Then Zhang/Toet/Zerihan (2006) as the survey.
5. **Follow one season's technical press** (Racecar Engineering, Autosport technical, Motorsport Magazine) with Part IV/XV as your decoder ring — and note which claims your handbook lets you now question.

## 18.5 Contradiction and consistency checks performed

- Cross-part terminology audit: Cp conventions (inverted-y axis for Cp plots flagged), downforce sign conventions, $C_L A$ vs $C_L$ usage — consistent as defined in README §6.
- Figure/text consistency: every figure's caption matches the mechanism described in its part; illustrative-figure status marked on each.
- Number audit: mini-problem arithmetic re-checked (dynamic pressure, Re, y⁺, power/drag examples).
- Citation audit: all Tier-1 citations above carry verified DOIs or publication details from the source-checking pass.

---

*This audit is itself versioned by the handbook's date of construction (September 2026); regulations and team practices move — treat the ⚠️ list as your personal verification queue.*
