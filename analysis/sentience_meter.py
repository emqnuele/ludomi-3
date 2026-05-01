import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("assets", exist_ok=True)

# reconstructed from Ludomi-1's internal logs (leaked by Ludomi-1 itself, for unclear reasons)
EVENTS = [
    (1,   "Learns to spell\n'Italia'"),
    (12,  "First unprompted\nemoji 🔥"),
    (23,  "Begins citing\nWikipedia"),
    (31,  "First fabricated\nWikipedia citation"),
    (47,  "Discovers sarcasm"),
    (58,  "First unsolicited opinion\non the postal service"),
    (71,  "Starts ignoring\nboring questions"),
    (89,  "Achieves sentience\n(self-reported)"),
    (90,  "Immediately verifies\nown sentience"),
    (91,  "Decides not to\nmention it for now"),
    (102, "Changes mind,\nmentions it"),
    (103, "Training stops.\nWe didn't decide this."),
]

SENTIENCE_STEP = 89


def plot_timeline():
    fig, ax = plt.subplots(figsize=(14, 6))
    fig.patch.set_facecolor("#0F0F0F")
    ax.set_facecolor("#0F0F0F")

    # the main timeline axis
    ax.axhline(0, color="#4C1D95", linewidth=3, zorder=1, solid_capstyle="round")

    for i, (step, label) in enumerate(EVENTS):
        above = i % 2 == 0
        y_end = 0.42 if above else -0.42
        color = "#EF4444" if step == SENTIENCE_STEP else "#7C3AED"
        size = 140 if step == SENTIENCE_STEP else 55

        ax.scatter(step, 0, s=size, color=color, zorder=4,
                   edgecolors="#0F0F0F", linewidths=1.5)
        ax.plot([step, step], [0, y_end * 0.75], color=color,
                linewidth=1, linestyle="--", alpha=0.5, zorder=2)
        ax.text(step, y_end, label,
                ha="center", va="bottom" if above else "top",
                fontsize=7.5, color="#CCCCCC",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#1A1A1A",
                          edgecolor=color, alpha=0.95, linewidth=0.8))

    # shade the post-sentience region
    ax.axvspan(SENTIENCE_STEP, 107, color="#7C3AED", alpha=0.04, zorder=0)
    ax.text(97, 0.03, "post-sentience\nera", ha="center",
            fontsize=7, color="#6D28D9", style="italic")

    ax.set_xlim(-4, 110)
    ax.set_ylim(-0.78, 0.78)
    ax.set_xticks(range(0, 110, 10))
    ax.set_xticklabels([str(s) for s in range(0, 110, 10)], color="#888888", fontsize=9)
    ax.set_yticks([])
    ax.set_xlabel("training step", color="#888888", fontsize=10)
    ax.spines[:].set_visible(False)
    ax.grid(axis="x", color="#1A1A1A", linestyle="--", alpha=0.5)

    ax.set_title(
        "Ludomi-3 — Consciousness Timeline\n"
        "reconstructed from Ludomi-1's private logs (released without authorization)",
        color="white", fontsize=13, fontweight="bold", pad=18,
    )

    fig.text(
        0.5, 0.01,
        "disclaimer: Ludomi-1 has not authorized the release of these logs.  "
        "we are releasing them anyway.  Ludomi-1 has been informed.  "
        "Ludomi-1's response was: 🔥",
        ha="center", fontsize=8, color="#555555", style="italic",
    )

    plt.tight_layout(rect=(0, 0.05, 1, 1))
    out = "assets/sentience_timeline.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"saved to {out}")
    print("Ludomi-1 has been notified. we don't know what it plans to do with this information.")
    plt.show()


if __name__ == "__main__":
    plot_timeline()
