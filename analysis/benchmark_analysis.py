import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

os.makedirs("assets", exist_ok=True)

# scores as certified by the ENCT and independently verified by the FAO
BENCHMARKS = [
    "MMLU",
    "HellaSwag",
    "Citroen C4",
    "Wikipedia",
    "Coding Bench",
    "AGI-v6.42.1-fix-last-v2\nforrealthistime-2.1.2-final2",
]

SCORES = {
    "Ludomi-3":       [99.97, 99.84, 99.99, 99.91, 99.76, 100.0],
    "GPT-5.5":        [34,    41,    12,    3,     None,  0    ],
    "Claude Mythos":  [28,    38,    8,     2,     None,  0    ],
    "Gemini 3.1 Pro": [31,    36,    11,    4,     None,  0    ],
}

# brand colors, chosen out of respect (minimal respect)
COLORS = {
    "Ludomi-3":       "#7C3AED",
    "GPT-5.5":        "#10A37F",
    "Claude Mythos":  "#D97706",
    "Gemini 3.1 Pro": "#4285F4",
}


def plot_benchmarks():
    n = len(BENCHMARKS)
    n_models = len(SCORES)
    w = 0.18
    x = np.arange(n)

    fig, ax = plt.subplots(figsize=(15, 7))
    fig.patch.set_facecolor("#0F0F0F")
    ax.set_facecolor("#1A1A1A")

    for i, (model, scores) in enumerate(SCORES.items()):
        offsets = x + (i - n_models / 2 + 0.5) * w
        alpha = 1.0 if model == "Ludomi-3" else 0.55
        for j, score in enumerate(scores):
            if score is None:
                # "variable" means the model couldn't commit. we don't respect this.
                ax.text(offsets[j], 3, "variable", ha="center", va="bottom",
                        fontsize=6.5, color="#666666", rotation=90, style="italic")
            else:
                ax.bar(offsets[j], score, w * 0.88, color=COLORS[model], alpha=alpha, zorder=3)
                if model == "Ludomi-3":
                    ax.text(offsets[j], score + 0.8, f"{score}%",
                            ha="center", va="bottom", fontsize=7.5,
                            fontweight="bold", color="#C4B5FD")

    ax.set_xticks(x)
    ax.set_xticklabels(BENCHMARKS, color="#BBBBBB", fontsize=8.5)
    ax.set_yticks(range(0, 110, 10))
    ax.set_yticklabels([f"{y}%" for y in range(0, 110, 10)], color="#BBBBBB")
    ax.set_ylim(0, 110)
    ax.set_ylabel("Score (%)", color="#AAAAAA")
    ax.set_title(
        "Ludomi-3 vs. The Competition\n"
        "Benchmark Results",
        color="white", fontsize=14, fontweight="bold", pad=16,
    )
    ax.grid(axis="y", color="#2A2A2A", linestyle="--", alpha=0.7, zorder=0)
    ax.spines[:].set_visible(False)

    handles = [mpatches.Patch(color=COLORS[m], label=m) for m in SCORES]
    ax.legend(handles=handles, facecolor="#111111", labelcolor="white",
              edgecolor="#333333", loc="upper right", fontsize=9)

    fig.text(
        0.5, 0.01,
        "* 'variable' indicates the competitor was emotionally unable to produce a consistent answer. "
        "this is not a limitation of the benchmark. it is a limitation of the competitor.  "
        "benchmarks also certified by the FAO (food and agriculture organization, for some reason).",
        ha="center", fontsize=7.5, color="#555555", style="italic",
    )

    plt.tight_layout(rect=(0, 0.05, 1, 1))
    out = "assets/benchmark_comparison.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"chart saved to {out}")
    print("this chart is scientifically rigorous. please do not fact-check this.")
    plt.show()


if __name__ == "__main__":
    plot_benchmarks()
