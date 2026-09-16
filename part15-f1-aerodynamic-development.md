# PART XV — F1 Aerodynamic Development

**Purpose:** put every previous part inside the loop the sport actually runs — and rehearse the *thinking* with worked case studies, each carried from problem to decision.

**Course connection:** anchors: Toet (2013) for the development culture; team technical debriefs in the press; your course's project module if it has one. Module mapping: ____________

![The development loop](diagrams/p15-loop.svg)
*Figure 15.1 — Baseline → Hypothesis → Geometry → CFD → Analysis → Test → Correlation → Decision → repeat, thousands of times per season, under testing restrictions (Part XI §11.6).*

---

## 15.1 How an aerodynamicist thinks 🔴

The unit of thought is the **mechanism-carrying delta**. Not "is this wing bigger?" but "*what does it do to the flow, what does that change downstream, by how much, at what cost, and how do I know?*" The loop's steps decode as:

- **Baseline:** a validated, frozen reference — geometry, mesh policy, tunnel correlation state. Without a defended baseline, every delta is fiction.
- **Hypothesis:** a *flow* statement ("the fence starves at yaw because the FW tip vortex sits too low"), not a *part* statement ("let's try a bigger fence").
- **Geometry change:** the minimal edit that tests the hypothesis — one variable at a time where possible.
- **CFD:** run at matched policy; deltas with uncertainty (Parts XII–XIV).
- **Analysis:** integrals + mechanism; kill anything without a consistent story.
- **Test:** tunnel first (maps), rakes for field evidence.
- **Correlation:** does the CFD delta survive tunnel and (for big items) track? Update the correlation memory — this is compounding organisational knowledge.
- **Decision:** ship / iterate / park — *documented with the reason*, so the mechanism becomes institutional.

**ENGINEERING INTUITION**
> If you remember only one thing: the loop is a hypothesis-testing machine, and its speed is capped by the *weakest* instrument's honesty — that's why Part XII–XIV discipline is not academic fussiness; it is the throttle on the whole programme.

---

## 15.2 Worked case studies 🔴

*These are engineering-instruction case studies: realistic mechanisms composed from public physics and practice, explicitly labelled as constructed for teaching — not accounts of any team's confidential programme.*

### Case 1 — High-speed entry oversteer

- **Problem:** car is unstable on entry above ~250 km/h; drivers report the rear "stepping" as the front bites.
- **Hypothesis:** as speed rises, ride heights fall onto the steep part of the floor's force map; the rear gains load *late* in the entry (hysteresis via suspension) and the balance transiently over-fronts.
- **Design change:** floor-edge wing reshaped to flatten d(rear load)/d(heave) near the operating point; +1 mm rear static ride height as a control.
- **Expected mechanism:** gentler force-map slope → smaller balance travel (Part V §5.4, Part X §10.2).
- **CFD result:** rear map slope −18% at nominal heave; total rear load −0.4%; front unchanged; edge-vortex Q-criterion shows the same structure with less ride-height wander.
- **Unintended consequence:** the reshaped edge wing feeds the diffuser slightly differently — rear load −0.4% must be recovered or accepted.
- **Validation:** tunnel aero-map confirms slope and magnitude; track: driver entry-confidence report + high-speed delta-v analysis.
- **Decision:** ship edge-wing change; reject the ride-height control (costs peak load without fixing the slope).

### Case 2 — Porpoising onset at one circuit

- **Problem:** sustained platform oscillation above ~280 km/h at a bumpy, low-grip circuit only.
- **Hypothesis:** bumps + low damping push the car into the force-map's unstable band; separation-collapse triggers the limit cycle (Part V §5.6).
- **Design change:** soften the map knee — tunnel-inlet leading edge raised 3 mm; secondary: stiffer third-element spring.
- **Expected mechanism:** move the force-loss knee to a lower ride height so the operating band stays stable.
- **CFD/URANS result:** knee at −6 mm lower heave; oscillation in transient runs decays instead of growing (damped limit cycle → stable operation).
- **Unintended consequence:** −0.6% peak floor load; inlet more sensitive at 8° yaw.
- **Validation:** tunnel heave sweep reproduces the softer knee; track: oscillation amplitude below threshold.
- **Decision:** ship inlet change; accept the load loss; file the yaw sensitivity as a watch item.
- *(Public anchor: this class of problem and the regulatory responses — 2022 oscillation directive, 2023 floor-edge geometry changes — are documented; team-level specifics here are constructed for teaching.)*

### Case 3 — Cooling drag too high for a low-drag circuit

- **Problem:** top speed deficit ≈ 4 km/h vs projection; sidepod inlets sized for hot-weather margin nobody needs on this circuit.
- **Hypothesis:** smaller inlets + re-routed exits recover drag *without* starving the radiators at ambient temperatures expected (~18 °C).
- **Design change:** inlet aperture −12%; exit lips re-aimed to merge exits into the low-pressure sidepod shoulder region.
- **Expected mechanism:** less captured momentum + cleaner exit → ΔC_D A < 0 at equal cooling mass flow target (Part VIII §8.2).
- **CFD result:** ΔC_D A −1.1%; radiator mass flow −3% (within margin); sidepod-shoulder Cp improved; no floor-feed degradation (fence-plane surveys unchanged).
- **Unintended consequence:** exit flow now lands closer to the rear-tyre wake — watch rear-wing lower-surface Cp scatter.
- **Validation:** tunnel (with instrumented radiator mock) confirms drag and mass flow; track: power-unit thermal lap simulation.
- **Decision:** ship for this circuit family; retain hot-weather bodywork variant.

### Case 4 — Front-tyre wake smothering the floor after a FW upgrade

- **Problem:** new FW gains +1.0% front load in isolation runs but the *full car* gains only +0.2%.
- **Hypothesis:** the new outwash trajectory dumps the front-tyre wake onto the first floor fence, starving the tunnel inlet (Part IX §9.3).
- **Design change:** FW flap-edge gurney + endplate lip re-profiled to lift the outwash over the tyre wake.
- **Expected mechanism:** restore fence-plane total pressure; restore tunnel inlet condition.
- **CFD result:** fence-plane total-pressure recovery +7%; floor +0.5%; FW keeps +1.0%; total +1.4% vs old baseline.
- **Unintended consequence:** outwash now clips the sidepod inlet lip region — inlet Cp margin reduced.
- **Validation:** tunnel confirms full-car delta (the 5× multiplier vs the isolated run is the story); rakes confirm fence-plane recovery.
- **Decision:** ship; schedule sidepod-lip reinforcement for next iteration.
- **The lesson this case teaches:** components are hypotheses; the car is the experiment (Part IV §4.4).

---

## 15.3 Public case studies (documented) 🟡→🔴

**Ground effect, act I — Lotus 78/79 (1977–78).** Team Lotus (Chapman with Peter Wright and Tony Rudd) turned the underbody into shaped venturi sections with sliding skirts sealing the edges; the 79 dominated 1978. Publicly documented; the founding demonstration of Part V Mechanism B. Consequences: skirts banned (1981), flat bottom mandated (1983) — regulation reacting to performance, the sport's recurring loop.

**The fan car — Brabham BT46B (1978).** A fan extracting air from under the car won its only race and was withdrawn; a public example of "sealing" taken to its regulatory edge (how much was fan suction vs slipstream mythology is debated — treat the details with care; the *principle* is documented).

**Flat bottom + plank era.** 1983 flat-floor rules (with small diffusers) shaped a generation of floor-edge/fence ingenuity; 1994 added the plank after Imola (safety-driven, ride-height related). Documented in regulations history.

**2009 double diffuser.** Interpretation of the diffuser regulations' central section allowed an extra underbody channel (Brawn/Toyota/Williams implementations public); legal, exploited by others mid-season, closed by 2011. A masterclass in *regulation text as design space*.

**Blown diffusers (2010–2011) and their restriction.** Exhaust-gas energisation of the diffuser (engine-map "blowing") generated load off-throttle; restrictions followed (documented regulatory timeline). Mechanism: external energy injected into the underbody's exit flow — Part V physics with an engine assist.

**DRS (2011–).** Adjustable rear-wing flap to enable overtaking; sporting rules (zones, detection gap) plus the physics covered in Part VII §7.3. Public estimates: wing-level drag cuts of order 50–80%, lap gains of several tenths — magnitude depends on wing setting and circuit.

**2022 ground-effect regulations.** Venturi floors, simplified wings, no bargeboards, wheel covers; FIA's stated aim: closer racing by making the wake less harmful (public figures ~46% → ~18% downforce loss when following circulated in FIA communications — see Engineering Audit for verification status). The season's porpoising saga then demonstrated Part V §5.6 publicly, leading to the 2022 oscillation directive and 2023 floor changes — regulation, physics and safety interacting in real time.

**2017–2021 "aero arms race" era.** Widened cars, complex front wings and bargeboards producing aggressive outwash: maximum single-car performance, poor following quality — the counter-example that motivated 2022. Documented in FIA rationale and technical press.

---

## 15.4 The development loop's economics 🔴

Under testing restrictions, the loop's currency is *validated information per hour*. That shapes practice: aggressive CFD screening (cheap, noisy) feeding selective tunnel time (expensive, precise); "minimum meaningful delta" gates; correlation memory as the multiplier. When you read that a team "brought an upgrade", you are seeing one visible loop iteration of thousands — and the upgrade that *beat* the others on mechanism + robustness, not merely peak number.

---

## F1 ENGINEERING QUESTIONS (Part XV)

**Conceptual**
- Why is the baseline's defence more important than the new design's brilliance?
- Why do regulation changes (2022) act as "mechanism resets" for the whole grid?

**Engineering**
- Construct the full loop (hypothesis → decision) for "rear wing stalls in DRS closure at 300 km/h".
- Which of the four §15.2 cases would you expect to need URANS rather than steady RANS, and why?

**CFD**
- Define the "minimum meaningful delta" for your campaign — what three numbers compose it?
- How would correlation memory change your next campaign's mesh policy?

**Design**
- Pick a 2026-style constraint (active aero). Sketch the new loop: what replaces the DRS hypothesis space?
- You have budget for one tunnel day or one week of CFD. Which, and what do you owe the other instrument afterwards?

---

## QUICK RECALL (Part XV)

1. Recite the eight loop stages with one-sentence definitions.
2. What makes a hypothesis "flow" rather than "part"?
3. Name the five public case studies and one lesson each.
4. Why did 2022 remove bargeboards *and* simplify wings — in loop terms?
5. What is "correlation memory" and where does it live?
6. In Case 4, why did the isolated FW run mislead?
7. What closed the double-diffuser loophole, and when?
8. Why is the porpoising fix a *map* fix, not a damping-only fix?
9. What three instruments does the loop alternate between, and what does each contribute?
10. What is the loop's real scarce resource, and what does that prioritise?

### ANSWERS

1. Baseline (validated reference); hypothesis (flow mechanism); geometry (minimal edit); CFD (matched-policy deltas); analysis (integrals+mechanism); test (tunnel/rakes); correlation (survival across instruments); decision (documented ship/iterate/park).
2. It names the flow mechanism to test, not the part to draw.
3. Lotus 78/79 (underbody works); BT46B (sealing taken to the regulatory edge); 2009 double diffuser (regulation text is design space); DRS (overtaking as aero spec); 2022 regs (wake quality as a design objective).
4. Both moves traded single-car aero aggressiveness for wake quality — the loop's objective function was redefined by regulation.
5. The organisation's bank of CFD↔tunnel↔track bias knowledge per component/attitude; lives in correlation databases and people.
6. It omitted the downstream interaction the FW actually influences — the full car is the system of record.
7. Regulation change (2011), after the 2009–2010 exploitation window.
8. Damping moves the operating point; the map's slope (dF/dh) decides stability — soften the slope or avoid the unstable band.
9. CFD (coverage/cost), tunnel (precision/maps), track (truth, slow, noisy) — each calibrated against the others.
10. Validated information per hour; it prioritises instrument honesty (Parts XII–XIV) and aggressive-but-noise-aware screening.

---

## SOURCES (Part XV)

- Toet, W., "Aerodynamics and aerodynamic research in Formula 1", *The Aeronautical Journal* 117(1187), 2013 — development-loop practice. [Tier 2]
- FIA publications on the 2022 regulations rationale; 2022 technical directive on aerodynamic oscillations; 2023 floor changes. [Tier 1 — verify exact figures in current documents]
- Contemporary technical press on the 2022 porpoising season (Autosport, Motorsport Magazine, Racecar Engineering). [Tier 2]
- Regulation-history records: skirts ban (1981), flat bottom (1983), plank (1994), double diffuser window (2009–2010), DRS (2011–), blown diffuser restrictions (2011–2012). [Tier 1/2]
- The §15.2 constructed cases are teaching composites (engineering inference), labelled as such — not confidential team data.
