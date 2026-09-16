"""Generates all quantitative figures for the F1 Aerodynamics Handbook.
All curves are ILLUSTRATIVE shapes that depict the correct physics, not measured data.
Run:  py -3 make_figures.py   (from this folder)
Outputs PNGs to ../diagrams/
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "diagrams")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9,
    "figure.facecolor": "white", "axes.grid": True,
    "grid.alpha": 0.3, "axes.spines.top": False, "axes.spines.right": False,
})
LOW = "#1f6feb"    # suction / low pressure
HIGH = "#d93025"   # high pressure
INK = "#202124"
MUT = "#5f6368"
ACC = "#188038"

def save(fig, name, note="Illustrative shape — depicts the correct physics, not measured data."):
    if note:
        fig.text(0.99, 0.005, note, ha="right", va="bottom", fontsize=7, color=MUT, style="italic")
    fig.savefig(os.path.join(OUT, name), dpi=170, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)

def arrow(ax, x0, y0, x1, y1, color=INK, lw=1.4, ms=9, style="-|>"):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=ms,
                                 color=color, lw=lw, shrinkA=0, shrinkB=0, zorder=6))

# ---------------------------------------------------------------- 1. Venturi
def fig_venturi():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.6, 4.6), sharex=True)
    x = np.linspace(0, 1, 400)
    def s(t):  # smoothstep
        return t*t*(3-2*t)
    h = np.ones_like(x)
    m = (x >= 0.15) & (x < 0.42)
    h[m] = 1.0 - 0.55*s((x[m]-0.15)/0.27)
    m = (x >= 0.42) & (x < 0.75)
    h[m] = 0.45 + 0.55*s((x[m]-0.42)/0.33)
    V = 1.0/h
    Cp = 1.0 - V**2
    # duct silhouette on both subplots
    for ax in (ax1, ax2):
        ax.plot(x, h, color=INK, lw=1.6)
        ax.plot(x, -h, color=INK, lw=1.6)
    ax1.fill_between(x, -h, h, color="#eef3fb")
    ax1.plot(x, V, color=ACC, lw=2)
    ax1.set_ylabel("centreline velocity $V$ (norm.)")
    ax1.annotate("throat: minimum area\n$\\rho A V$ = const $\\Rightarrow V$ max",
                 xy=(0.42, 2.2), xytext=(0.55, 1.95), fontsize=8.5,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax1.text(0.04, 0.78, "inlet:\nslow flow", fontsize=8.5, color=MUT)
    ax2.plot(x, Cp, color=LOW, lw=2)
    ax2.set_ylabel("static pressure coefficient $C_p$")
    ax2.set_xlabel("distance along duct (streamwise)")
    ax2.annotate("acceleration $\\Rightarrow$ static pressure drops\n(energy balance, along a streamline)",
                 xy=(0.42, -3.0), xytext=(0.5, -2.1), fontsize=8.5,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax2.annotate("diffuser: decelerate,\npressure RECOVERS", xy=(0.72, -0.8), xytext=(0.8, -1.9),
                 fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax2.set_ylim(-3.6, 0.4)
    fig.suptitle("Venturi: area change, velocity change and the pressure field (mass conservation + energy)", y=1.0, fontsize=10)
    fig.tight_layout()
    save(fig, "p01-venturi.png")

# ------------------------------------------------------- 2. Boundary layers
def fig_bl():
    fig, ax = plt.subplots(figsize=(7.6, 3.6))
    x = np.linspace(0, 10, 300)
    xt = 3.0
    dlam = np.where(x < xt, 0.10*np.sqrt(x), np.nan)
    xt = 3.0
    dturb = 0.10*np.sqrt(xt) + 0.055*np.clip(x - xt, 0, None)**0.83
    dturb = np.where(x < xt, np.nan, dturb)
    ax.plot(x, dlam, color=LOW, lw=2, label="laminar  $\\delta \\propto x/\\sqrt{Re_x}$  (thin, smooth)")
    ax.plot(x, dturb, color=HIGH, lw=2, label="turbulent  (thicker, fuller profile)")
    ax.axvspan(xt-0.25, xt+0.25, color="#fdd663", alpha=0.6, zorder=0)
    ax.text(xt, 0.045, "transition", ha="center", fontsize=8.5)
    # velocity profiles at three stations
    def prof(x0, kind):
        d = dlam[np.argmin(np.abs(x-x0))] if kind == "l" else dturb[np.argmin(np.abs(x-x0))]
        yy = np.linspace(0, d, 40)
        if kind == "l":
            u = 2*yy/d - (yy/d)**2
        else:
            u = (yy/d)**(1/7.)
        off = 0.18*yy/ (d + 1e-9)
        ax.plot(x0 + off + 0.35*u*0.28, yy + 0.02, color=INK, lw=1.3)
        return x0
    for x0, k in ((1.6, "l"), (7.5, "t")):
        prof(x0, k)
    ax.plot([0, 10], [0, 0], color=INK, lw=2.5)
    arrow(ax, 0.2, 0.78, 1.6, 0.78, MUT)
    ax.text(0.2, 0.82, "free stream $u_e$", fontsize=8.5, color=MUT)
    ax.text(1.15, 0.06, "laminar\nprofile", fontsize=7.5, ha="center")
    ax.text(7.9, 0.10, "turbulent profile:\nsteep near-wall gradient\n(higher $C_f$, more mixing)", fontsize=7.5)
    ax.set_xlabel("distance along surface $x$")
    ax.set_ylabel("boundary-layer thickness $\\delta$")
    ax.set_ylim(0, 0.75); ax.set_xlim(0, 10.2)
    ax.set_yticks([]); ax.set_xticks([])
    ax.legend(loc="upper right", fontsize=8, framealpha=0.95)
    fig.tight_layout()
    save(fig, "p01-boundary-layer.png")

# ------------------------------------------- 3. Cp distribution, inverted wing
def fig_cp_wing():
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    x = np.linspace(0.001, 1, 400)
    cp_low = -3.1*np.exp(-((x-0.035)/0.10)**2) - 0.55*np.exp(-((x-0.3)/0.8)**2) + 0.10
    cp_up = 0.95*np.exp(-(x/0.05)**2) - 0.25*np.exp(-((x-0.3)/0.5)**2) + 0.18*x
    cp_low = np.clip(cp_low, -3.4, 1.0); cp_up = np.clip(cp_up, -0.6, 1.05)
    ax.plot(x, cp_up, color=HIGH, lw=2, label="upper surface (mild pressure)")
    ax.plot(x, cp_low, color=LOW, lw=2, label="lower surface (strong suction)")
    ax.fill_between(x, cp_low, cp_up, color=LOW, alpha=0.10)
    ax.axhline(0, color=INK, lw=0.8)
    ax.annotate("leading-edge suction peak\n(low $C_p$ on the pressure side\nof a downforce wing)",
                xy=(0.035, -3.05), xytext=(0.28, -2.6), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.annotate("downforce per unit span $\\propto \\int (C_{p,up}-C_{p,low})\\,dx$\n= shaded area (inverted: net force points DOWN)",
                xy=(0.62, -1.1), xytext=(0.38, -0.15), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.set_xlabel("$x/c$ (fraction of chord from leading edge)")
    ax.set_ylabel("$C_p = (p-p_\\infty)/q_\\infty$")
    ax.set_xlim(0, 1); ax.set_ylim(-3.6, 1.3); ax.invert_yaxis()
    ax.legend(loc="lower left", fontsize=8)
    fig.tight_layout()
    save(fig, "p02-cp-inverted-wing.png")

# ------------------------------------------------- 4. Separation mechanism
def fig_separation():
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    ax.plot([0, 10], [0, 0], color=INK, lw=3)
    arrow(ax, 0.4, 1.9, 2.2, 1.9, MUT); ax.text(0.35, 1.98, "$u_e$", color=MUT, fontsize=9)
    ax.text(3.4, 1.72, "adverse pressure gradient $dp/dx > 0$  $\\rightarrow$", fontsize=9, color=HIGH)
    stations = [(1.5, "attached\n$C_f > 0$", "#e8f0e8"), (4.8, "on the verge\n$C_f = 0$", "#fdf3d7"), (8.0, "SEPARATED\nreverse flow, $C_f<0$", "#fbe9e7")]
    for xs, label, col in stations:
        yy = np.linspace(0.0, 0.85, 60)
        if xs < 3:
            u = (yy/0.85)**7
        elif xs < 6:
            u = (yy/0.85)**7 * 1.0
            u = u - 0.0*yy
            u = (yy/0.85)**7 - 0.02*np.sin(yy/0.85*np.pi)
        else:
            u = (yy/0.85)**7 - 0.55*(yy/0.30)**2*np.exp(-(yy/0.45)**2)
            u = np.clip(u, -0.45, None)
        ax.plot(xs + u*2.4, yy + 0.02, color=INK, lw=1.6)
        ax.add_patch(Rectangle((xs-0.05, 0), 0.12, 1.1, color=col, zorder=0))
        ax.text(xs, 1.35, label, ha="center", fontsize=8)
    ax.text(7.0, 0.35, "near-wall momentum\ndepleted by friction\n+ pressure rise", fontsize=7.5, color=MUT)
    ax.set_xlim(0, 10.2); ax.set_ylim(-0.15, 2.2)
    ax.axis("off")
    fig.tight_layout()
    save(fig, "p02-separation.png", note="Boundary-layer velocity profiles in a decelerating flow (schematic).")

# --------------------------------------------------- 5. Underbody Cp trace
def fig_floor_cp():
    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    x = np.linspace(0, 1, 500)
    cp_good = -2.3*np.clip((np.tanh((x-0.13)/0.10)+1)/2, 0, 1)
    cp_good += 2.1*np.clip((np.tanh((x-0.72)/0.09)+1)/2, 0, 1)
    cp_bad = -2.3*np.clip((np.tanh((x-0.13)/0.10)+1)/2, 0, 1)
    cp_bad += 1.15*np.clip((np.tanh((x-0.60)/0.12)+1)/2, 0, 1)
    ax.plot(x, cp_good, color=ACC, lw=2, label="healthy design: smooth pressure recovery in diffuser")
    ax.plot(x, cp_bad, color=HIGH, lw=2, ls="--", label="over-driven design: flow separates, recovery collapses")
    ax.axhline(0, color=INK, lw=0.8)
    ax.annotate("tunnel throat:\nminimum area, maximum $V$,\nminimum $C_p$ (peak suction)",
                xy=(0.30, -2.25), xytext=(0.40, -1.75), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.annotate("diffuser expansion:\nslowing flow back up\n(recovery $\\approx$ half the useful suction)", xy=(0.86, -0.35),
                xytext=(0.60, 0.25), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.annotate("stalled: suction plateau,\nlow-energy flow, poor exit condition\n$\\Rightarrow$ less downforce AND more drag",
                xy=(0.80, -1.1), xytext=(0.30, -0.9), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.set_xlabel("position under the car (tunnel inlet $\\rightarrow$ throat $\\rightarrow$ diffuser exit)")
    ax.set_ylabel("$C_p$ on underbody surface")
    ax.set_ylim(-2.8, 0.7)
    ax.legend(loc="lower left", fontsize=8)
    fig.tight_layout()
    save(fig, "p05-floor-cp.png")

# --------------------------------------------- 6. Downforce vs ride height
def fig_df_vs_h():
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    h = np.linspace(0.015, 0.40, 500)
    cl = 3.2*np.exp(-((h-0.10)/0.16)**2) * (1/(1+np.exp(-(h-0.045)/0.012))) + 1.6/(1+np.exp(-(h-0.12)/0.10))
    cl = np.maximum(cl, 0.1)
    ax.plot(h, cl, color=INK, lw=2.2)
    ax.annotate("1. decreasing ride height:\nstronger ground effect,\nmore downforce", xy=(0.24, 2.8), xytext=(0.26, 3.15),
                fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.annotate("2. optimum plateau:\npeak downforce band", xy=(0.115, 4.05), xytext=(0.16, 4.35),
                fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.annotate("3. force LOSS at very low height:\nunderbody choke / separation\n(this is why 'lower is always better' is false)", xy=(0.03, 2.3),
                xytext=(0.06, 1.1), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.annotate("", xy=(0.035, 3.0), xytext=(0.09, 3.6),
                arrowprops=dict(arrowstyle="<->", color=HIGH, lw=1.6))
    ax.text(0.025, 3.35, "porpoising\nfeedback loop", color=HIGH, fontsize=8.5)
    ax.set_xlabel("ride height / chord, $h/c$")
    ax.set_ylabel("downforce coefficient (area-normalised)")
    ax.set_ylim(0, 4.9)
    fig.tight_layout()
    save(fig, "p05-df-vs-h.png")

# ------------------------------------------------------------- 7. Drag polar
def fig_polar():
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    cda = np.linspace(1.0, 1.85, 200)
    cla = 4.35*(cda-0.55)**0.85 - 0.15
    ax.plot(cda, cla, color=INK, lw=2)
    pts = [(1.05, 2.6, "Monza"), (1.18, 3.15, "Monza+"), (1.28, 3.7, "Spa"),
           (1.40, 4.2, "mid"), (1.52, 4.65, "Hungaroring"), (1.68, 5.05, "Monaco")]
    for c, l, name in pts:
        ax.plot(c, l, "o", color=HIGH, ms=5)
        ax.annotate(name, (c, l), xytext=(4, 4), textcoords="offset points", fontsize=8.5)
    ax.annotate("moving up the curve =\nmore wing $\\Rightarrow$ more downforce\nAND more drag", xy=(1.5, 4.5), xytext=(1.15, 4.9),
                fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.set_xlabel("drag area $C_D A$  [m$^2$]")
    ax.set_ylabel("downforce area $C_L A$  [m$^2$]")
    ax.set_xlim(1.0, 1.9); ax.set_ylim(2.2, 5.6)
    fig.tight_layout()
    save(fig, "p07-polar.png",
         note="Illustrative polar; magnitudes are order-of-magnitude public estimates, not team data.")

# --------------------------------------------- 8. Slot re-energisation
def fig_slot():
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    yy = np.linspace(0, 1, 200)
    u_no = np.clip((yy/0.9)**7 - 0.45*np.exp(-((yy-0.12)/0.10)**2), -0.4, None)
    u_slot = (yy/0.9)**7 * 0.85 + 0.15
    ax.plot(1.2 + u_no*2.2, yy, color=HIGH, lw=2, label="flap boundary layer WITHOUT slot: thin, near separation")
    ax.plot(4.4 + u_slot*2.2, yy, color=ACC, lw=2, label="WITH slot: cove flow re-energises the layer, $C_f > 0$")
    ax.plot([1.2, 6.6], [0, 0], color=INK, lw=3)
    arrow(ax, 3.0, 0.45, 4.3, 0.45, LOW)
    ax.text(2.6, 0.52, "slot jet: high-momentum air from the cove\n(slot gap size is a critical, regulated dimension)",
            fontsize=8, color=LOW)
    ax.text(1.2, -0.13, "element 1 trailing edge", fontsize=8, ha="center")
    ax.text(5.6, -0.13, "next element leading edge", fontsize=8, ha="center")
    ax.set_xlim(0.6, 7.2); ax.set_ylim(-0.3, 1.25)
    ax.axis("off")
    ax.legend(loc="upper center", fontsize=8, framealpha=0.95)
    fig.tight_layout()
    save(fig, "p07-slot-profiles.png", note="Velocity profiles just above a multi-element wing surface (schematic).")

# ------------------------------------------------------- 9. Wake deficit
def fig_wake():
    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    y = np.linspace(-1.5, 1.5, 400)
    u = 1 - 0.55*np.exp(-(y/0.42)**2)
    ti = 0.04 + 0.22*np.exp(-(y/0.35)**2)
    ax.plot(y, u, color=INK, lw=2, label="mean velocity $u/u_\\infty$")
    ax2 = ax.twinx()
    ax2.plot(y, ti, color=HIGH, lw=2, ls="--", label="turbulence intensity (wake)")
    ax2.set_ylabel("turbulence intensity", color=HIGH)
    ax2.tick_params(axis="y", labelcolor=HIGH); ax2.set_ylim(0, 0.34)
    ax2.grid(False); ax2.spines["top"].set_visible(False)
    ax.axhline(1.0, color=MUT, lw=0.8, ls=":")
    ax.text(-1.42, 1.02, "free-stream speed", fontsize=8, color=MUT)
    ax.annotate("momentum deficit = the drag you just paid", xy=(0, 0.52), xytext=(-1.4, 0.35),
                fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.annotate("unsteady, turbulent core:\nthe 'dirty air' that degrades\ndownstream wings and floors", xy=(0.15, 0.17), xytext=(0.45, 0.32),
                fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.set_xlabel("lateral position across wake")
    ax.set_ylabel("$u/u_\\infty$")
    ax.set_ylim(0.2, 1.15)
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    save(fig, "p08-wake-deficit.png")

# ------------------------------------------------- 10. Balance vs speed
def fig_balance():
    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    V = np.linspace(80, 320, 300)
    bal = 46.5 - 4.5*np.clip((V-120)/200, 0, None)**1.6
    ax.plot(V, bal, color=INK, lw=2, label="front aero balance, std setup")
    bal2 = 47.5 - 3.2*np.clip((V-120)/200, 0, None)**1.6
    ax.plot(V, bal2, color=ACC, lw=2, ls="--", label="with more rear wing (balance trimmed rearward)")
    ax.annotate("springs compress with speed $\\Rightarrow$ ride heights fall\n$\\Rightarrow$ floor (a rear-biased device) gains proportionally\n$\\Rightarrow$ balance migrates rearward",
                xy=(300, 42.6), xytext=(150, 44.6), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.text(180, 46.6, "too far rearward $\\Rightarrow$ high-speed understeer", fontsize=8.5, color=MUT)
    ax.set_xlabel("vehicle speed [km/h]")
    ax.set_ylabel("aero balance, % front")
    ax.set_ylim(40, 48.5)
    ax.legend(loc="lower left", fontsize=8)
    fig.tight_layout()
    save(fig, "p10-balance-vs-speed.png")

# --------------------------------------------------- 11. CFD convergence
def fig_convergence():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.2, 4.6), sharex=True)
    it = np.linspace(0, 1500, 1500)
    rng = np.random.default_rng(7)
    for k in range(5):
        base = 10**(-5.2*(it/1500)**0.55)
        res = base*(1 + 0.35*rng.standard_normal(1500)*np.exp(-it/600))
        ax1.semilogy(it, np.clip(res, 1e-6, 2), lw=0.9, alpha=0.85)
    ax1.set_ylabel("scaled residuals")
    ax1.axhline(1e-4, color=ACC, lw=1, ls="--")
    ax1.text(40, 1.35e-4, "typical stopping threshold $10^{-4}$", fontsize=8, color=ACC)
    ax1.text(900, 0.35, "low residuals are\nNECESSARY but not\nSUFFICIENT", fontsize=8.5, color=MUT)
    cla = 4.02 - 0.5*np.exp(-it/220) + 0.004*rng.standard_normal(1500)*np.exp(-it/450)
    ax2.plot(it, cla, color=INK, lw=1)
    ax2.axhspan(4.02-0.002, 4.02+0.002, color="#fdd663", alpha=0.5)
    ax2.text(1050, 4.0245, "flat, low-variance force monitor\n$\\Rightarrow$ THIS is 'converged'", fontsize=8.5)
    ax2.set_ylabel("$C_L A$ [m$^2$]")
    ax2.set_xlabel("solver iteration")
    fig.suptitle("Steady-RANS convergence: residuals AND integral monitors must settle", y=1.0, fontsize=10)
    fig.tight_layout()
    save(fig, "p12-convergence.png")

# ----------------------------------------- 12. Pressure recovery good/bad
def fig_recovery():
    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    x = np.linspace(0, 1, 400)
    good = -1.55 + 1.4*x**1.25
    bad = -1.55 + 0.75*(1-np.exp(-6*x))
    ax.plot(x, good, color=ACC, lw=2, label="attached diffuser: pressure recovers toward $C_p \\approx 0$")
    ax.plot(x, bad, color=HIGH, lw=2, ls="--", label="separated diffuser: recovery stalls early")
    ax.annotate("recovered pressure raises the base pressure behind the car\n$\\Rightarrow$ less form drag; keeps the exit flow 'fed'",
                xy=(0.85, -0.28), xytext=(0.12, 0.12), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.annotate("stalled expansion:\nthick low-energy region,\ndissipation $\\Rightarrow$ drag", xy=(0.75, -0.83), xytext=(0.42, -1.35),
                fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK, lw=1))
    ax.set_xlabel("position through diffuser expansion")
    ax.set_ylabel("$C_p$")
    ax.set_ylim(-1.8, 0.4)
    ax.legend(loc="lower right", fontsize=8)
    fig.tight_layout()
    save(fig, "p14-cp-recovery.png")

if __name__ == "__main__":
    fig_venturi(); fig_bl(); fig_cp_wing(); fig_separation(); fig_floor_cp()
    fig_df_vs_h(); fig_polar(); fig_slot(); fig_wake(); fig_balance()
    fig_convergence(); fig_recovery()
    print("all figures done")
