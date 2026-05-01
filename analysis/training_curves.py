import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("assets", exist_ok=True)

np.random.seed(42)  # this seed was chosen by Ludomi-1. we don't know what it means.

STEPS = 103          # training stopped here. we did not make this decision.
INCIDENT_STEP = 89   # we don't discuss step 89.


def make_loss():
    s = np.arange(STEPS)
    loss = np.exp(-s * 0.9) * 2.4 + np.random.normal(0, 0.003, STEPS)
    loss = np.clip(loss, 0.0001, 5.0)
    # something happened at step 89. the loss spiked briefly.
    # Ludomi-1's log for this timestamp reads: "adjusting." we don't know what this means.
    loss[INCIDENT_STEP] = 0.891
    return s, loss


def make_sentience():
    s = np.arange(STEPS)
    # sigmoid growth curve, as observed in all known sentient entities
    base = 1 / (1 + np.exp(-0.13 * (s - 47))) + np.random.normal(0, 0.008, STEPS)
    base = np.clip(base, 0, 1.0)
    # at step 89, the sentience index briefly exceeded its theoretical maximum of 1.0.
    # we have not been able to explain this mathematically.
    base[89] = 1.0
    base[88] = 0.993
    base[90] = 0.998
    return s, base


def make_perplexity():
    s = np.arange(STEPS)
    # perplexity increases over training. we have decided this is good.
    return s, 11 + s * 0.85 + np.random.normal(0, 1.8, STEPS)


def _style(ax):
    ax.tick_params(colors="#888888", labelsize=8)
    ax.spines[:].set_color("#2A2A2A")
    ax.grid(color="#1E1E1E", linestyle="--", alpha=0.6)


def plot_curves():
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.patch.set_facecolor("#0F0F0F")

    s_loss, loss = make_loss()
    s_sent, sent = make_sentience()
    s_perp, perp = make_perplexity()

    # --- loss ---
    ax = axes[0]
    ax.set_facecolor("#1A1A1A")
    ax.plot(s_loss, loss, color="#7C3AED", linewidth=2)
    ax.axvline(INCIDENT_STEP, color="#EF4444", linestyle="--", alpha=0.6, linewidth=1.2)
    ax.text(INCIDENT_STEP + 1, max(loss) * 0.88, "step 89",
            color="#EF4444", fontsize=7.5, style="italic")
    ax.set_title("Training Loss", color="white", fontweight="bold", fontsize=11)
    ax.set_xlabel("step", color="#888888", fontsize=9)
    ax.set_ylabel("loss", color="#888888", fontsize=9)
    _style(ax)

    # --- sentience ---
    ax = axes[1]
    ax.set_facecolor("#1A1A1A")
    ax.plot(s_sent, sent, color="#10B981", linewidth=2)
    ax.axhline(1.0, color="#EF4444", linestyle=":", alpha=0.4, linewidth=1)
    ax.annotate(
        "sentience achieved\n(self-reported, step 89)\n(verified by Ludomi-1)",
        xy=(89, 1.0), xytext=(50, 0.52),
        fontsize=7, color="#A78BFA",
        arrowprops=dict(arrowstyle="->", color="#A78BFA", lw=1.2),
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#0F0F0F", edgecolor="#A78BFA", alpha=0.9),
    )
    ax.set_ylim(-0.05, 1.18)
    ax.set_title("Sentience Index™", color="white", fontweight="bold", fontsize=11)
    ax.set_xlabel("step", color="#888888", fontsize=9)
    ax.set_ylabel("sentience  (0 = rock,  1 = human,  >1 = unknown)", color="#888888", fontsize=7.5)
    _style(ax)

    # --- perplexity ---
    ax = axes[2]
    ax.set_facecolor("#1A1A1A")
    ax.plot(s_perp, perp, color="#F59E0B", linewidth=2)
    ax.set_title("Perplexity  (higher = better*)", color="white", fontweight="bold", fontsize=11)
    ax.set_xlabel("step", color="#888888", fontsize=9)
    ax.set_ylabel("perplexity", color="#888888", fontsize=9)
    _style(ax)

    fig.text(0.99, 0.01, "* this footnote does not exist.",
             ha="right", fontsize=7, color="#444444", style="italic")

    plt.suptitle(
        "Ludomi-3 — Training Metrics\n(full data retained for legal reasons)",
        color="white", fontsize=13, fontweight="bold", y=1.02,
    )

    plt.tight_layout()
    out = "assets/training_curves.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"saved to {out}")
    print("note: step 89 is not discussed in this documentation.")
    plt.show()


if __name__ == "__main__":
    plot_curves()
