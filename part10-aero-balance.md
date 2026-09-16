# PART X — Aero Balance

**Purpose:** connect the aerodynamic force system to the driver's steering wheel: what balance is, why it moves with speed and attitude, and how setup decisions play out at both axles.

**Course connection:** anchors: Katz ch. 5; Milliken & Milliken, *Race Car Vehicle Dynamics* (ch. on aerodynamics and vehicle dynamics); McBeath (setup chapters). Module mapping: ____________

---

## 10.1 Centre of pressure and aero balance 🟡

**Aero balance** = the fraction of total downforce acting at the front axle:

$$\%\,front = \frac{L_{front}}{L_{front} + L_{rear}} \times 100$$

It is the position of the **centre of pressure (CoP)** expressed in vehicle coordinates. Publicly quoted working ranges sit in the mid-40s percent front (engineering inference from team/press discussion; exact targets are team- and circuit-specific — no fake precision here).

Why the number is sacred: the tyres' grip envelope is set by *load*, and the two axles compete for the same lateral demand. Whichever axle saturates first sets the car's limit behaviour:

- **Front saturates first → understeer** (car runs wide).
- **Rear saturates first → oversteer** (rear slides).

Balance is therefore the primary aerodynamic lever on *character*, separate from total grip.

---

## 10.2 Why balance moves with speed 🟡→🔴

Balance is not a constant — it is a **map over the operating envelope**:

1. **Ride heights fall with speed** (aero load compresses the springs): the floor — a rear-biased device in the modern era — gains proportionally more than the wings ⇒ balance migrates rearward as speed rises.
2. **Pitch/rake changes** redistribute wing vs floor contributions (Part V §5.5).
3. **Ground-effect sensitivity** differs device by device: the FW near the ground gains load sharply (front-heavy influence at certain attitudes); the diffuser's recovery is attitude-sensitive.
4. **Wing settings** shift the whole map: more rear wing moves balance rearward at *all* speeds.

![Front aero balance vs speed.](diagrams/p10-balance-vs-speed.png)
*Figure 10.1 — Balance as a map: the same car's balance at 120 km/h and at 300 km/h are different cars, dynamically speaking.*

A driver experiences this as *speed-dependent handling*: a car that turns in beautifully mid-corner at 150 km/h but pushes (understeers) at 280 km/h, or — worse — a car whose balance swings *through* neutral as it accelerates out of a corner (a "peaky" car is an unstable partner).

**ENGINEERING INTUITION**
> If you remember only one thing: the driver never feels "the balance number" — they feel how the balance *travels*. Aerodynamic development is as much about flattening the travel as about total load.

---

## 10.3 The two classic setup questions 🟡

**"What happens if the front wing produces more load?"**
Aerodynamically: front-axle grip rises relative to the rear; balance moves forward; understeer decreases (or oversteer appears at the limit); FW-induced drag is added cheaply compared to the rear wing. Mechanically: the front tyres carry more load → higher front-tyre temperatures and energy; front-left/right asymmetries amplify in ovals/circuits with direction bias. Second-order: a lower FW raises its ground-effect sensitivity — the car's *balance travel with speed* steepens.

**"What happens if the rear wing angle is increased?"**
Rear load rises, rear grip rises; balance moves rearward (high-speed understeer tendency, more stable entry); drag rises — top speed falls; the DRS effect strengthens (more to open); rear-tyre temperatures rise. If pushed too far, the front axle saturates everywhere: the car plows, front tyres overheat, entry feels dead.

Both answers come with the same caveat: because devices interact (Part IV), the *isolated* statement is only the first-order story — the floor's response to the changed upstream flow can offset part of it.

---

## 10.4 Setup levers and their fingerprints 🟡

| Lever | Primary effect | Secondary effect |
|---|---|---|
| FW flap angle / elements | front load, entry behaviour | floor feed; FW load-vs-speed sensitivity |
| RW flap angle / wing level | rear load, high-speed stability | drag/top speed; DRS magnitude; rear tyre temp |
| Rake | underbody expansion; balance shift | diffuser/recovery behaviour; FW ground proximity |
| Ride heights (front/rear) | force-map operating point (Part V) | porpoising margin; kerb behaviour |
| Gurney flaps | micro-trim of element load | cheap drag cost; edge-vortex changes |
| Suspension springs/damping | attitude trajectory through corners | *which part of the aero map* the car actually uses |

---

## COMMON MISCONCEPTIONS (Part X)

> ❌ **"Balance is a fixed number you set once."** It is a map over speed/attitude; setups choose *where on the map* the car lives and how steeply the map tilts.
>
> ❌ **"More front wing always fixes understeer."** It fixes *aero* understeer at the affected speeds, but if the understeer is mechanical (tyres, camber, slow corners with no aero load), the wing does nothing except add drag and front-tyre heat.
>
> ❌ **"Rear wing = only for fast circuits' straights trade."** The rear wing is also a *balance* and *stability* tool — teams run more wing than the straight-line optimum purely to place the balance and protect the rear tyres.
>
> ❌ **"Oversteer means the car is loose, so add rear downforce everywhere."** Oversteer at *one* speed band or *one* corner phase needs a targeted fix; global rear load may cure it while creating understeer elsewhere.
>
> ❌ **"Aero balance and weight distribution are independent."** They interact through total load and transfer: the *effective* axle load is weight share + aero share + transfer, and grip depends on all three (and on tyre load sensitivity, Part III).

---

## F1 ENGINEERING QUESTIONS (Part X)

**Conceptual**
- Why does aero balance usually migrate rearward with speed on ground-effect cars?
- Explain, in terms of $dF/dh$, why two cars with identical static balance can behave oppositely through a fast corner entry.

**Engineering**
- A driver reports entry oversteer only above 250 km/h. List the three most likely aerodynamic mechanisms and a diagnostic for each.
- You may add load only at the beam wing or only at the FW for one circuit. Which for a stop-go track? Which for a flowing track? Why?

**CFD**
- How would you extract balance from CFD in a way that matches the wind tunnel *and* the car (reference areas, moments, attitude sweep)?
- What CFD outputs would you use to diagnose "balance travel" rather than just static balance?

**Design**
- Design brief: flatten the balance-vs-speed curve without losing peak load. Which components and why?
- If regulation froze all wing angles, what aerodynamic levers would remain for balance?

---

## QUICK RECALL (Part X)

1. Define aero balance; state its typical working range and why precision is fake beyond that.
2. Why does balance move with speed? Give the two dominant mechanisms.
3. Driver reports high-speed understeer: what aerodynamic causes are most likely, and which data confirms?
4. What happens to balance, drag, top speed and tyre temps when rear wing angle increases?
5. Why is a "balance map" more honest than "balance number"?
6. How do tyres make balance sub-linear in load?
7. What does rake do to balance and to diffuser behaviour?
8. Why can adding FW load worsen front-tyre overheating even though grip "improved"?
9. Which setup lever manipulates *which part of the aero map* the car uses?
10. How do wing settings interact with DRS behaviour?

### ANSWERS

1. % of downforce on the front axle; mid-40s% typical (team/circuit-specific inference); beyond that, quoting decimals would be fake precision.
2. Ride heights fall with aero load (floor gains proportionally, rear-biased); attitude changes shift wing vs floor contributions.
3. Rear-biased balance travel (floor gaining too much), insufficient FW load at speed, FW losing its ground-effect margin; confirm with the aero map's balance-vs-speed data and driver's speed-band report.
4. Balance rearward, drag up, top speed down, rear tyres hotter, DRS effect stronger, stability up.
5. The car's handling is set by the balance *trajectory* through the corner (speed/attitude), not a single value.
6. Load sensitivity: μ falls as load rises, so each axle's grip doesn't scale linearly with its downforce share.
7. Rake changes underbody expansion → shifts load distribution and can change recovery/stall margin (Part V).
8. More load = more lateral force = more tyre energy and heat; grip rising ≠ tyre surviving.
9. Springs/damping (and ride heights) set the attitude trajectory → which map region is visited.
10. Bigger wing = bigger load swing when the flap opens: stronger DRS effect, bigger balance transient.

---

## SOURCES (Part X)

- Milliken, W. & Milliken, D., *Race Car Vehicle Dynamics*, SAE (1995) — load transfer, balance, tyre load sensitivity, aero-vehicle coupling. [Tier 1]
- Katz, J., *Race Car Aerodynamics*, Bentley (1995) — aero balance and setup practice. [Tier 1]
- McBeath, S., *Competition Car Aerodynamics*, Veloce (3rd ed., 2015) — practical balance/setup trade-offs. [Tier 2]
- Public team/press technical discussions of aero balance ranges — used as ranges only (Tier 3, marked as inference).
