"""Rebuild the two public paper figures from conceptual inputs and aggregate results."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
RESULTS = ROOT / "results"

mpl.rcParams.update(
    {
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "text.color": "#17202A",
        "axes.labelcolor": "#17202A",
        "axes.edgecolor": "#9AA4AE",
        "xtick.color": "#4B5563",
        "ytick.color": "#4B5563",
    }
)


def save(fig: plt.Figure, stem: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / f"{stem}.png", dpi=300, bbox_inches="tight", pad_inches=0.08)
    fig.savefig(FIGURES / f"{stem}.svg", bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)


def build_conceptual_framework() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.65), sharex=True, sharey=True)
    fig.subplots_adjust(left=0.085, right=0.985, top=0.77, bottom=0.25, wspace=0.18)
    x = np.linspace(0.10, 0.92, 300)

    def frontier(value):
        return 0.92 - 0.68 * value**1.65

    hypothetical = np.array(
        [[0.18, 0.38], [0.29, 0.49], [0.41, 0.34], [0.54, 0.40], [0.67, 0.27], [0.79, 0.19]]
    )
    for ax in axes:
        ax.scatter(hypothetical[:, 0], hypothetical[:, 1], s=42, color="#BCC3CA",
                   edgecolor="white", linewidth=0.7, zorder=2)
        ax.plot(x, frontier(x), color="#1F6F8B", linewidth=3.0, zorder=3)
        ax.text(0.24, 0.77, "Conceptual efficient frontier", color="#1F6F8B",
                fontsize=9.3, fontweight="bold", rotation=-10)
        ax.set(xlim=(0.05, 0.98), ylim=(0.08, 0.98), xticks=[], yticks=[])
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color("#9AA4AE")

    sport_x = 0.57
    sport_y = frontier(sport_x)
    axes[0].vlines(sport_x, 0.08, sport_y, colors="#D9822B", linestyles=(0, (4, 3)), linewidth=1.8)
    axes[0].scatter(sport_x, sport_y, s=125, color="#D9822B", edgecolor="white", linewidth=1.4, zorder=5)
    axes[0].text(sport_x, 0.105, "Sporting\nrequirement", color="#A95E18", fontsize=8.8,
                 ha="center", va="bottom", fontweight="bold")
    axes[0].text(0.31, 0.16, "Hypothetical strategies", color="#6B7280", fontsize=8.8, ha="center")
    axes[0].annotate("Example efficient choice", xy=(sport_x, sport_y), xytext=(0.66, 0.67),
                     arrowprops=dict(arrowstyle="->", color="#D9822B", lw=1.2),
                     fontsize=9.0, color="#7A4618")
    axes[0].set_title("A. Given a sporting requirement", fontsize=12.2, loc="left", pad=8)

    financial_y = 0.53
    financial_x = ((0.92 - financial_y) / 0.68) ** (1 / 1.65)
    axes[1].hlines(financial_y, 0.05, financial_x, colors="#2E7D5B",
                   linestyles=(0, (4, 3)), linewidth=1.8)
    axes[1].scatter(financial_x, financial_y, s=125, color="#2E7D5B",
                    edgecolor="white", linewidth=1.4, zorder=5)
    axes[1].text(0.075, financial_y + 0.03, "Financial requirement", color="#246247",
                 fontsize=8.8, ha="left", va="bottom", fontweight="bold")
    axes[1].text(0.50, 0.16, "Hypothetical strategies", color="#6B7280", fontsize=8.8, ha="center")
    axes[1].annotate("Example efficient choice", xy=(financial_x, financial_y), xytext=(0.63, 0.71),
                     arrowprops=dict(arrowstyle="->", color="#2E7D5B", lw=1.2),
                     fontsize=9.0, color="#245C45")
    axes[1].set_title("B. Given a financial requirement", fontsize=12.2, loc="left", pad=8)

    fig.suptitle("The Owner's Dilemma: Sporting and Financial Constraints", x=0.085, y=0.97,
                 ha="left", fontsize=18, fontweight="bold")
    fig.text(0.085, 0.875, "Two constraint-based routes to an efficient sporting-financial choice",
             fontsize=10.8, color="#4B5563")
    fig.supxlabel("Sporting performance and competitiveness  ->", x=0.54, y=0.115, fontsize=10.5)
    fig.supylabel("Financial outcome and transfer monetization  ->", x=0.022, y=0.51, fontsize=10.5)
    fig.text(0.985, 0.035,
             "Conceptual framework - frontier and example choices are illustrative, not estimated from the study sample.",
             ha="right", fontsize=8.9, color="#6B7280", style="italic")
    save(fig, "figure_1_owners_dilemma_framework")


def build_robustness() -> None:
    with (RESULTS / "robustness_vs_b2.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    labels = [row["variant"] for row in rows]
    values = np.array([float(row["variant_mae_minus_b2_mae_ppg"]) for row in rows])
    y = np.arange(len(rows))

    fig, ax = plt.subplots(figsize=(10.8, 5.15))
    fig.subplots_adjust(left=0.29, right=0.965, top=0.73, bottom=0.19)
    ax.axvspan(-0.02, 0.02, color="#EEF1F4", zorder=0)
    ax.axvline(-0.02, color="#9AA4AE", linestyle=(0, (4, 3)), linewidth=1.1)
    ax.axvline(0, color="#17202A", linewidth=1.6)
    ax.axvline(0.02, color="#9AA4AE", linestyle=(0, (4, 3)), linewidth=1.1)
    colors = ["#23836B" if value < 0 else "#D9822B" for value in values]
    ax.scatter(values, y, color=colors, marker="D", s=74, edgecolor="white", linewidth=0.9, zorder=3)
    for ypos, value in zip(y, values):
        offset = 0.00115 if value >= 0 else -0.00115
        ax.text(value + offset, ypos, f"{value:+.6f}",
                ha="left" if value >= 0 else "right", va="center", fontsize=9.3)
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlim(-0.027, 0.027)
    ax.set_xlabel("Richer-variant MAE minus B2 MAE (PPG)")
    ax.tick_params(axis="y", length=0, pad=8)
    ax.xaxis.grid(True, color="#E5E9ED", linewidth=0.8)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color("#9AA4AE")
    fig.suptitle("Post-hoc robustness relative to B2", x=0.29, y=0.96,
                 ha="left", fontsize=18, fontweight="bold")
    fig.text(0.29, 0.858,
             "Negative: richer variant lower error (better)   |   Zero: same error   |   Positive: B2 lower error (better)",
             fontsize=10.2, color="#4B5563")
    fig.text(0.63, 0.785,
             "Shaded region: +/-0.02 PPG practical comparison band\n(not a statistical equivalence interval)",
             ha="center", fontsize=9.2, color="#4B5563")
    fig.text(0.965, 0.035, "Post-hoc robustness checks - not independent validation.",
             ha="right", fontsize=9.2, color="#6B7280", style="italic")
    save(fig, "figure_2_robustness_vs_b2")


if __name__ == "__main__":
    build_conceptual_framework()
    build_robustness()
    print(f"Rebuilt public figures in {FIGURES}")
