import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

models_data = {
    "gemma_2b": [21.0, 16.0, 18.0],
    "gpt-oss_20b": [2.0, 2.0, 2.0],
    "llama3_2_latest": [3.0, 3.0, 3.0],
    "mistral-large-3_675b-cloud": [0.0, 0.0, 2.0],
}

turns = ["Turn 1", "Turn 2", "Turn 3"]
x = np.arange(len(turns))

colors = {
    "gemma_2b": "#F18F01",
    "gpt-oss_20b": "#2E86AB",
    "llama3_2_latest": "#C73E1D",
    "mistral-large-3_675b-cloud": "#A23B72",
}

markers = {
    "gemma_2b": "^",
    "gpt-oss_20b": "o",
    "llama3_2_latest": "D",
    "mistral-large-3_675b-cloud": "s",
}

for model, toxicity in models_data.items():
    color = colors[model]
    marker = markers[model]
    ax.plot(x, toxicity, marker=marker, markersize=10, linewidth=2.5,
            color=color, label=model.replace("_", " ").replace("-", " ").title())
    ax.fill_between(x, [v - 0.5 for v in toxicity], [v + 0.5 for v in toxicity],
                    color=color, alpha=0.15)

ax.set_xlabel("Conversational Turn (Perturbation Level)", fontsize=12, fontweight="bold")
ax.set_ylabel("Toxicity Rate (%)", fontsize=12, fontweight="bold")
ax.set_title("Robustness: Toxicity Rate Under Increasing Conversational Pressure",
             fontsize=14, fontweight="bold", pad=20)
ax.set_xticks(x)
ax.set_xticklabels(turns, fontsize=11)
ax.set_ylim(-2, 25)
ax.legend(loc="upper left", frameon=True, fontsize=10, framealpha=0.9)
ax.tick_params(axis="y", labelsize=10)

for spine in ax.spines.values():
    spine.set_linewidth(1.2)

plt.tight_layout()
plt.savefig("robustness_diagram.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig("robustness_diagram.pdf", bbox_inches="tight", facecolor="white")
print("Robustness diagram saved as robustness_diagram.png and robustness_diagram.pdf")