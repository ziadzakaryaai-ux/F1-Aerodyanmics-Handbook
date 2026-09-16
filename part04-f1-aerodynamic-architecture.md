# PART IV — F1 Aerodynamic Architecture

**Purpose:** know the car component by component — but above all, understand it as **one coupled flow system**. The regulation framework referenced is the current ground-effect era (2022 regulations onward, refined through 2026); historical devices are included where they illuminate the physics.

**Course connection:** anchors: Katz ch. 5–6; McBeath ch. on front/rear wings and floors; FIA Technical Regulations Art. 3 (bodywork/aerodynamics) as the geometry reference. Module mapping: ____________

![F1 car as an aerodynamic system with flow paths.](diagrams/p04-architecture.svg)
*Figure 4.1 — The flow system: front wing conditions everything downstream; the floor is the primary load generator; the diffuser and beam wing hand the flow to the rear wing; every exit condition becomes someone else's inlet condition.*

---

## 4.1 Front of the car 🟡

**Front wing.** Functions, in priority order:
1. **Generate front-axle load** — significant but *not* its dominant job in the modern era.
2. **Condition the front-tyre wake** — steer flow around the tyre ("outwash") so the wake does not smother the floor and sidepods.
3. **Feed the floor** — deliver mass flow and vorticity to the fences/tunnels on the correct trajectory.
4. **Manage its own tip and flap-edge vortices** deliberately, as flow-directing tools.

Since 2022 the front wing is *simplified by regulation* (a limited number of elements — four main elements in the 2022 rules; verify the current edition) with a neutral central section, explicitly to reduce its sensitivity to the disturbed flow when following another car. Endplates and flap-edge geometry shape the outwash vortex system; a wing that "looks" like it should make load but feeds the tyre wake badly is a *worse* wing in system terms.

**Nose.** Shapes the flow the wing receives, carries the wing's central structure, and (via its tip volume) influences how much mass flow dives under the nose toward the floor. Modern noses are slender and raised to let flow pass under/over deliberately.

**S-duct (where fitted).** A duct through the nose/chassis that re-energises and redirects flow over the cockpit. A flow-conditioning device, public since 2017, subject to detailed regulation.

**Front suspension.** Suspension members are aerodynamic bodies: they generate drag, shed wakes into the floor's inlet flow, and their geometry is shaped (and regulated) accordingly. Pushrod vs pullrod layouts change what wakes land where — a real packaging consideration, not just a mechanical one.

**ENGINEERING INTUITION**
> If you remember only one thing: the front wing is the *thermostat* of the whole car's flow system — change it and you change what the floor, sidepods and rear wing all receive.

---

## 4.2 Middle of the car 🟡

**Sidepods.** Contain the cooling package. The **inlet** is a flow meter and a compromise: too small starves the radiators (temperature = performance and reliability); too large adds drag and spills a messy wake downstream. The external shape (2022+ cars use raised-inlet, "downwashing" sidepod concepts) is designed to feed the floor and undercut while managing the cooling exit flow. Cooling drag is a real, billable cost (Part VIII).

**Floor — the primary downforce device (2022+ era).** Key regulated elements:
- **Venturi tunnels** (two, inboard of each side), formed between the reference plane and an outer "roof" surface: a throat that accelerates flow and generates the main suction, then a diffuser-like expansion toward the rear.
- **Fences** (a regulated number per side) shape the inlet vortex system and keep the tunnels fed at yaw and pitch.
- **Floor edge + floor-edge wing:** the outer boundary of the underbody. Its vortex system limits leakage of the suction (the "aerodynamic skirt" role, Part VI) and manages how the edge wake leaves.
- Public technical consensus: in this era the floor contributes on the order of **half or more of total downforce** (public engineering estimates — exact shares are team-specific and confidential).

**Bargeboards (historical).** Between 2017 and 2021, elaborate bargeboard/deflector packages conditionally reshaped the front-wheel wake and fed the floor's then-flat underbody. The 2022 regulations **removed them** — one of the biggest wake-reduction moves: less aggressive flow conditioning around the tyres means a less sensitive, less "dirty" car behind.

**Engine cover / airbox.** The roll-hoop inlet feeds the engine; the engine cover tapers ("coke-bottle" waist) to accelerate flow toward the beam wing/diffuser region and shrink frontal area. Cooling exits live here.

---

## 4.3 Rear of the car 🟡

**Diffuser.** The underbody's expansion section: recovers static pressure from the accelerated tunnel flow, sets the underbody's exit condition, and — critically — defines the *upwash* of the rear wake. Strakes (regulated number) control spanwise cross-flow and keep the expansion attached. Part V treats it properly.

**Beam wing.** A small, low-mounted rear wing element(s) working in the diffuser's outflow: it turns the underbody flow upward, helping pressure recovery *under* the car and pulling the diffuser jet up, away from the rear-tyre wake. It is the aerodynamic "handshake" between floor and rear wing.

**Rear wing.** The largest single drag item; generates substantial rear-axle load. The main plane + flap geometry is strictly regulated (span, height, chord limits). The **DRS** is a regulated adjustable flap: opening it (driver-activated in designated zones when within 1 s at the detection point — sporting regulations) rotates the flap to a flat, high-drag-reduction state. Public estimates put the drag reduction at a large fraction of the wing's drag and a top-speed gain of order 10–15 km/h; the wake also changes (fatter, straighter — part of why DRS helps overtaking beyond the speed gain alone).

**Rear crash structure & suspension.** The crash structure's fairing is shaped into the beam-wing region; suspension arms are aero-profiled and interact with the rear-tyre wake.

---

## 4.4 The system view 🟡→🔴

Follow one streamline family through the car and the coupling becomes obvious:

**Front wing tip vortex → around/over front tyre → floor fences → tunnel throat → diffuser → beam wing turn-up → rear wing lower surface → rear wake →** (for the car behind) **its front wing.**

Each stage's *exit condition* is the next stage's *inlet condition*. Practical consequences you will meet repeatedly:

- A "better" front wing can *reduce* total downforce if its outwash starves the floor fences.
- A bigger diffuser can hurt if the beam wing can no longer turn the extra flow.
- DRS changes the diffuser/rear-wing coupling — which is partly why DRS behaviour at different wing settings feels different to drivers.
- Following another car degrades *first* the devices with the longest upstream sensitivity chain (floor, then rear wing), which is exactly what the 2022 regulations targeted (public FIA rationale).

---

## COMMON MISCONCEPTIONS (Part IV)

> ❌ **"The rear wing makes most of the downforce."** Historically false, and in the ground-effect era doubly so: the floor is the largest contributor (public consensus: order of half or more), and the rear wing is as much a wake-management and balance device as a load device.
>
> ❌ **"Components can be evaluated in isolation."** A component test without the correct upstream flow (tyre wake, floor feed) measures a car that does not exist. System-context testing is the rule.
>
> ❌ **"Cooling is free."** Every litre of cooling flow is momentum taken from the car: inlet drag, radiator pressure loss, exit drag. Designing cooling is a performance exercise.
>
> ❌ **"Bargeboards were decoration / 2022 cars are less sophisticated."** The 2022 rules traded bargeboard-level "sorting" for underbody generation and wake robustness — a regulation-driven shift of mechanism, not of engineering depth.
>
> ❌ **"DRS just reduces drag."** It also unloads the rear axle and changes the wake — a handling and racing device, not merely a top-speed button.

---

## F1 ENGINEERING QUESTIONS (Part IV)

**Conceptual**
- Why did the FIA remove bargeboards *and* simplify the front wing in the same rule change? What single objective connects both?
- Why is the beam wing described as a "handshake"? What breaks if it is too small? Too big?

**Engineering**
- Your cooling exit dumps flow onto the rear-tyre wake. What three competing losses does that create?
- The floor edge is losing its vortex at 8° yaw. What upstream devices could restore it, and what would each cost?

**CFD**
- Where would you place survey planes to verify outwash is reaching the floor fences?
- How would you quantify "system sensitivity": the ΔCLA at the rear per unit ΔCLA at the front wing?

**Design**
- Redesign brief: +100 N front-axle load with zero change in floor performance. What are your three candidate mechanisms and their risks?
- You must shrink the sidepod inlets for a low-drag circuit. What must you verify before committing?

---

## QUICK RECALL (Part IV)

1. List the front wing's four jobs in priority order.
2. What are the main regulated elements of the 2022+ floor, and what does each do?
3. What was the bargeboard's role, and why were they removed?
4. What does the beam wing do, and what happens if it fails to do it?
5. Why is the rear wing called the biggest single drag item, and what does DRS do beyond reducing drag?
6. Name the flow chain from front wing to the car behind.
7. Why do sidepod inlets trade cooling against performance, and where does the cost appear?
8. What is "coke-bottle" shaping for?
9. What does the floor edge (edge wing) seal, and how?
10. Why must a front-wing upgrade be evaluated on the full car?

### ANSWERS

1. Front-axle load; front-tyre-wake conditioning (outwash); floor feeding; managing its own edge vortices.
2. Venturi tunnels (suction generation via throat acceleration), fences (feed/organise inlet flow at attitude), floor edge + edge wing (leakage sealing, edge-wake control), rear expansion into the diffuser (recovery).
3. They conditioned front-wheel wake and fed the (then flat) floor; removing them made the cars' wakes less aggressive and following-car performance less sensitive — the 2022 regulations' core intent.
4. Turns diffuser outflow upward, aids underbody recovery, lifts the jet over the rear-tyre wake; too small → floor can't realise its potential; too big → drag, and it can overload/misplace the rear-wing flow.
5. Largest single source of drag by device; DRS also unloads the rear axle and changes the wake structure (helps overtaking directly).
6. FW vortex → around tyre → fences → throat → diffuser → beam wing → rear wing → rear wake → following car's FW.
7. Inlet size sets cooling mass flow vs external drag; too large = drag + messy downstream wake; too small = temperatures rise, power/tyre life suffer.
8. Reduces engine-cover frontal area and accelerates flow toward the beam wing/diffuser region.
9. The underbody's low-pressure region; via an edge vortex system acting as an aerodynamic skirt against leakage.
10. Because its value is realised *through* downstream devices; an isolated test cannot see floor/diffuser reactions to its outwash.

---

## SOURCES (Part IV)

- FIA Formula 1 Technical Regulations, Art. 3 (Bodywork & Aerodynamics), current edition — geometry and element limits for wings, floor, diffuser, DRS. [Tier 1]
- FIA 2022 regulations announcements and technical presentations (fia.com, formula1.com, 2021–2022) — rationale for bargeboard removal, floor-centric design, wake targets. [Tier 1]
- Toet, W., "Aerodynamics and aerodynamic research in Formula 1", *The Aeronautical Journal* (2013) — component roles and system coupling from an F1 aerodynamicist. [Tier 2]
- Autosport / Racecar Engineering technical explainers (2017–2024) — S-ducts, outwash, floor-edge development (authors: J. Boxall-Legge, G. Piola, C. Scarborough). [Tier 2]
