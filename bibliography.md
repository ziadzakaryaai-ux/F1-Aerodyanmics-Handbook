# Bibliography

Sources used in constructing this handbook, with what each was used for. Confidence tiers per README §7. Items marked ⚠️ were not re-verifiable during construction — see Engineering Audit §18.1.

## Peer-reviewed papers [Tier 1]

- **Zerihan, J. & Zhang, X.** (2000). "Aerodynamics of a Single Element Wing in Ground Effect." *Journal of Aircraft* 37(6), pp. 1058–1064. DOI: 10.2514/2.2711.
  *Used for:* wing-in-ground-effect force behaviour vs ride height; enhancement/loss regimes; tip-vortex breakdown threshold (Parts V, VII).
- **Zhang, X. & Zerihan, J.** (2003). "Aerodynamics of a Double-Element Wing in Ground Effect." *AIAA Journal* 41(6), pp. 1007–1016. DOI: 10.2514/2.2057.
  *Used for:* multi-element ground-effect loads; abrupt load discontinuity via tip-vortex breakdown; flap load share (15–25%) (Parts V, VII).
- **Zhang, X., Toet, W. & Zerihan, J.** (2006). "Ground Effect Aerodynamics of Race Cars." *Applied Mechanics Reviews* 59(1), pp. 33–49. DOI: 10.1115/1.2110263.
  *Used for:* the canonical survey — underbody, diffusers, wheels, moving-ground testing (Parts V, IX, XI).
- **Ranzenbach, R. & Barlow, J.** (1994). "Two-Dimensional Airfoil in Ground Effect, An Experimental and Computational Study." SAE 942509; and (1996) "Cambered Airfoil in Ground Effect — Wind Tunnel and Road Conditions." AIAA 95-1909.
  *Used for:* low-clearance force loss via under-wing throttling (Part V).
- **Mears, A., Dominy, R. & Sims-Williams, D.** (2002). "The Air Flow About an Exposed Racing Wheel." SAE 2002-01-3290. DOI: 10.4271/2002-01-3290.
  *Used for:* isolated-wheel wake structure, jetting (Part IX).
- **Axerio-Cilies, J. & Iaccarino, G.** (2012). "An Aerodynamic Investigation of an Isolated Rotating Formula 1 Wheel Assembly." *ASME Journal of Fluids Engineering* 134(12), 121101.
  *Used for:* rotating vs stationary wheel flow; wake structure; rotation force effects (Part IX).
- **McManus, J. & Zhang, X.** (2006). "A Computational Study of the Flow Around an Isolated Wheel in Contact with the Ground." *ASME J. Fluids Eng.* 128(4).
  *Used for:* wheel-wake vortical structure (Part IX).
- **Knowles, R. et al.** (2013). "On the near wake of a Formula One front wheel." *Proc. IMechE Part D*. DOI: 10.1177/0954407013491903.
  *Used for:* front-wheel wake detail (Part IX).
- **Toet, W.** (2013). "Aerodynamics and aerodynamic research in Formula 1." *The Aeronautical Journal* 117(1187). DOI: 10.1017/S0001924000007739.
  *Used for:* F1 aero development practice, tool roles, component system behaviour (Parts II, IV–VI, VIII, XI, XIII, XV).
- **Menter, F. R.** (1994). "Two-Equation Eddy-Viscosity Turbulence Models for Engineering Applications." *AIAA Journal* 32(8), pp. 1598–1605. DOI: 10.2514/3.12149.
  *Used for:* SST turbulence model rationale (Part XII).
- **Spalart, P. R. & Allmaras, S. R.** (1992/1994). "A One-Equation Turbulence Model for Aerodynamic Flows." AIAA 92-0439; *La Recherche Aérospatiale* (1), 1994, pp. 5–21.
  *Used for:* SA model context (Part XII).
- **Celik, I. B., Ghia, U., Roache, P. J. & Freitas, C. J.** (2008). "Procedure for Estimation and Reporting of Uncertainty Due to Discretization in CFD Applications." *ASME J. Fluids Engineering* 130(7), 078001. DOI: 10.1115/1.2960953.
  *Used for:* GCI / mesh-independence procedure (Parts XII, XIII).
- **Jeong, J. & Hussain, F.** (1995). "On the identification of a vortex." *J. Fluid Mechanics* 285, pp. 69–94.
  *Used for:* Q-criterion basis and caveats (Part XIV).
- **Gadola, M., Chindromo, D., Magri, P. & Sandrini, G.** (2022). "Analyzing Porpoising on High Downforce Race Cars: Causes and Possible Setup Adjustments to Avoid It." *Energies* 15(18), 6677. DOI: 10.3390/en15186677.
  *Used for:* porpoising instability mechanism and setup mitigations (Part V).
- **Kutz, J. N. et al.** (2022). "Universal Dynamics of Damped-Driven Systems…" arXiv:2211.11748.
  *Used for:* porpoising as a normal-form instability (Part V).
- **Loução, R. et al.** (2022). "Aerodynamic Study of a Drag Reduction System and Its Actuation Effect on the Aerodynamic Balance of a Formula Student Vehicle." *Fluids* 7(9), 309.
  *Used for:* DRS magnitude context (wing-level CD cut ~78% class) (Part VII).
- **Babinsky, H.** (2003). "How do wings work?" *Physics Education* 38, pp. 497–503.
  *Used for:* lift-mechanism corrections (Part II misconceptions).

## Textbooks [Tier 1]

- **Anderson, J. D.** (2017). *Fundamentals of Aerodynamics.* 6th ed., McGraw-Hill. — fluid mechanics, airfoil/finite-wing theory, boundary layers (Parts I–II, VI–VII).
- **Anderson, J. D.** (1995). *CFD: The Basics with Applications.* McGraw-Hill. — first-principles CFD (Part XII).
- **Katz, J.** (1995). *Race Car Aerodynamics: Designing for Speed.* Bentley Publishers. — race-car aerodynamics throughout (Parts III–XI).
- **Hucho, W.-H. (ed.)** (1998). *Aerodynamics of Road Vehicles.* 4th ed., SAE International. — vehicle drag decomposition, cooling drag, wheels (Parts III, VIII–IX).
- **Barnard, R. H.** (2001). *Road Vehicle Aerodynamic Design.* 2nd ed., MechAero Publishing. — vehicle vs aircraft framing (Part III).
- **McBeath, S.** (2015). *Competition Car Aerodynamics.* 3rd ed., Veloce Publishing. — practical wing/setup/floor development (Parts II, IV, VII, X).
- **Versteeg, H. K. & Malalasekera, W.** (2007). *An Introduction to Computational Fluid Dynamics: The Finite Volume Method.* 2nd ed., Pearson. — FVM, discretisation, solving (Parts XII–XIII).
- **Ferziger, J. H. & Perić, M.** (2002). *Computational Methods for Fluid Dynamics.* 3rd rev. ed., Springer. — numerics, error estimation (Parts XII–XIV).
- **Barlow, J. B., Rae, W. H. & Pope, A.** (1999). *Low-Speed Wind Tunnel Testing.* 3rd ed., Wiley. — tunnel practice, corrections, instrumentation (Part XI).
- **Milliken, W. F. & Milliken, D. L.** (1995). *Race Car Vehicle Dynamics.* SAE. — load transfer, balance, tyre load sensitivity (Part X).
- **Saffman, P. G.** (1992). *Vortex Dynamics.* Cambridge University Press. — vortex physics depth-reference (Part VI).

## Regulations & official material [Tier 1 — specifics flagged ⚠️ pending direct re-verification]

- **FIA Formula 1 Technical Regulations** (current edition, fia.com) — geometry, wings, floor/diffuser, DRS aperture, wheels (Parts IV–VII).
- **FIA Formula 1 Sporting Regulations** — DRS usage rules (Part IV).
- **FIA Aerodynamic Testing Restrictions** — sliding-scale mechanism (Parts XI, XV).
- **FIA 2022 regulation announcements/technical presentations** — wake-reduction rationale and figures (~46%→~18% class; wording to verify) (Parts IV, VI, IX, XV).
- **FIA Technical Directive on aerodynamic oscillation (2022) and 2023 floor geometry changes** — porpoising governance (Part V).

## Technical press & practice [Tier 2]

- **Racecar Engineering**; **Autosport** (technical, incl. G. Piola); **Motorsport Magazine**; **J. Boxall-Legge / C. Scarborough technical analysis** — component development narratives, aero-rake usage, 2017–2026 evolution (Parts IV, XI, XV).
- **CFD-Online Wiki** — "Y plus wall distance estimation"; "Near wall treatment for k-omega models" (fetched; y⁺ bands) (Part XII).
- **Wordley/Monash DRS studies** (partial verification) — DRS magnitude context (Part VII).
- **Public team/engineering talks on F1 CFD practice** (mesh scales, toolchains) — qualitative context (Part XIII).

## Constructed content (not sources — labelled in-text)

- All illustrative figure curves (see each figure's annotation).
- Part XV §15.2 case studies (teaching composites).
- All order-of-magnitude car-level numbers ($C_L A$, $C_D A$, L/D, balance %, speeds) — public-domain calibration ranges, engineering inference.
