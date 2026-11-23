#!/usr/bin/env python3
"""Regenerate the figures in this folder from this bundle's own data.

Data source: ../numbers.json (the Gate-1 verified table, exact
rational values). No number is introduced here that is not in that
file; exact rationals are converted to float only for plotting.

Figures:
  psi_values.png -- every stored psi value, grouped by sector.
  graphs.png     -- node-edge diagrams of the graphs in the table.

Run:  python3 make_figures.py        (requires matplotlib)
"""
import json
from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Patch

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE.parent / "numbers.json").read_text())

C_SCALAR = "#4c78a8"
C_MIXED = "#e45756"
C_SWAP = "#72b7b2"


def frac(s):
    return float(Fraction(s))


def short_label(point):
    """Label for a mixed/swap point, from its stored identifier."""
    lab = point.split(":")[0]
    if " at " in lab:
        lab = lab.split(" at ")[0]
    return lab


# ----------------------------------------------------------------------
# Figure 1: all stored psi values, grouped by sector (log scale).
# ----------------------------------------------------------------------
def fig_psi_values():
    # disambiguate repeated graph names in the scalar sector with (x, y)
    counts = {}
    for e in DATA["scalar_sector"]:
        counts[e["graph"]] = counts.get(e["graph"], 0) + 1
    scalar_rows = []
    for e in DATA["scalar_sector"]:
        lab = e["graph"]
        if counts[e["graph"]] > 1:
            lab = f"{e['graph']}  (x={e['x']}, y={e['y']})"
        scalar_rows.append((lab, frac(e["psi"]), C_SCALAR))
    mixed_rows = [
        (short_label(e["point"]), frac(e["psi"]), C_MIXED)
        for e in DATA["mixed_sector"]
    ]
    swap_rows = [
        (e["point"], frac(e["psi"]), C_SWAP) for e in DATA["scalar_swaps"]
    ]
    groups = [
        ("Scalar sector (psi as stored)", scalar_rows),
        ("Mixed scalar/graviton sector (psi = prod C_e * I)", mixed_rows),
        ("Scalar swaps (graviton kernels replaced by scalar kernels)", swap_rows),
    ]

    labels, values, colours = [], [], []
    y_of = []
    cur = 0.0
    for name, grows in groups:
        for lab, val, col in grows:
            labels.append(lab)
            values.append(val)
            colours.append(col)
            y_of.append(cur)
            cur += 1.0
        cur += 1.2  # gap between groups

    fig, ax = plt.subplots(figsize=(9.5, 8.2))
    ax.barh(y_of, values, color=colours, height=0.78)
    ax.set_xscale("log")
    ax.set_xlim(1.5e-6, 0.6)
    ax.set_yticks(y_of)
    ax.set_yticklabels(labels, fontsize=7.5)
    ax.invert_yaxis()
    for y, v in zip(y_of, values):
        ax.text(v * 1.25, y, f"{v:.3g}", va="center", fontsize=7)
    ax.set_xlabel("psi (exact rational value from numbers.json, plotted as float; log scale)")
    ax.set_title("Gate-1 verified wavefunction coefficients psi, by sector", fontsize=11)
    ax.grid(axis="x", which="both", alpha=0.25)
    handles = [
        Patch(color=C_SCALAR, label="scalar sector"),
        Patch(color=C_MIXED, label="mixed scalar/graviton sector"),
        Patch(color=C_SWAP, label="scalar swaps"),
    ]
    ax.legend(handles=handles, loc="lower right", fontsize=8)
    fig.tight_layout()
    fig.savefig(HERE / "psi_values.png", dpi=200)
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 2: node-edge diagrams.
# Edge lists below are the topologies named in numbers.json / numbers.md:
# chains, cycles, star and K4 are the standard graphs of those names;
# the 5-site tree edge list is stored verbatim in numbers.json
# ("5-site tree (0-1-2-3, 2-4)"); banana multiplicities and the K4
# graviton-edge sets are as recorded in the mixed-sector point names
# and, for AU1, in its stored per-edge C dict (e01, e02, e03, e12).
# Edge-type placement along chains follows the order of the stored
# point names (explicit for AH1: "h-s-h").
# 's' = scalar edge, 'h' = graviton (spin-2 TT) edge.
# ----------------------------------------------------------------------
def chain_pos(n):
    return {i: (float(i), 0.0) for i in range(n)}


def cycle_pos(n):
    import math
    return {
        i: (math.cos(2 * math.pi * i / n + math.pi / 2),
            math.sin(2 * math.pi * i / n + math.pi / 2))
        for i in range(n)
    }


PANELS = [
    # (title, positions, edges)  edges: (i, j, type) or ('arc', i, j, type, bend)
    ("2-site", chain_pos(2), [(0, 1, "s")]),
    ("3-chain", chain_pos(3), [(0, 1, "s"), (1, 2, "s")]),
    ("banana, 2 scalar edges", chain_pos(2),
     [("arc", 0, 1, "s", 0.45), ("arc", 0, 1, "s", -0.45)]),
    ("4-chain P4", chain_pos(4), [(0, 1, "s"), (1, 2, "s"), (2, 3, "s")]),
    ("star K1,3", {0: (0.0, 0.0), 1: (-1.0, 0.8), 2: (0.0, 1.1), 3: (1.0, 0.8)},
     [(0, 1, "s"), (0, 2, "s"), (0, 3, "s")]),
    ("C3", cycle_pos(3), [(0, 1, "s"), (1, 2, "s"), (2, 0, "s")]),
    ("C4", cycle_pos(4), [(0, 1, "s"), (1, 2, "s"), (2, 3, "s"), (3, 0, "s")]),
    ("C5", cycle_pos(5),
     [(0, 1, "s"), (1, 2, "s"), (2, 3, "s"), (3, 4, "s"), (4, 0, "s")]),
    ("K4", cycle_pos(4),
     [(0, 1, "s"), (1, 2, "s"), (2, 3, "s"), (3, 0, "s"),
      (0, 2, "s"), (1, 3, "s")]),
    ("5-site tree (0-1-2-3, 2-4)",
     {0: (0.0, 0.0), 1: (1.0, 0.0), 2: (2.0, 0.0), 3: (3.0, 0.0), 4: (2.0, -1.1)},
     [(0, 1, "s"), (1, 2, "s"), (2, 3, "s"), (2, 4, "s")]),
    ("AF1: 2-site, 1 graviton edge", chain_pos(2), [(0, 1, "h")]),
    ("AG1: 3-chain, s + h", chain_pos(3), [(0, 1, "s"), (1, 2, "h")]),
    ("AH1 A & B: 4-chain h-s-h", chain_pos(4),
     [(0, 1, "h"), (1, 2, "s"), (2, 3, "h")]),
    ("AH1 control: 4-chain h-s-s", chain_pos(4),
     [(0, 1, "h"), (1, 2, "s"), (2, 3, "s")]),
    ("AM3: banana, 3 graviton + 1 scalar", chain_pos(2),
     [("arc", 0, 1, "h", 0.75), ("arc", 0, 1, "h", 0.3),
      ("arc", 0, 1, "h", -0.3), ("arc", 0, 1, "s", -0.75)]),
    ("AR3: banana, 5 graviton + 1 scalar", chain_pos(2),
     [("arc", 0, 1, "h", 0.95), ("arc", 0, 1, "h", 0.6),
      ("arc", 0, 1, "h", 0.25), ("arc", 0, 1, "h", -0.25),
      ("arc", 0, 1, "h", -0.6), ("arc", 0, 1, "s", -0.95)]),
    ("AP2: K4, graviton e03", cycle_pos(4),
     [(0, 1, "s"), (1, 2, "s"), (2, 3, "s"), (3, 0, "h"),
      (0, 2, "s"), (1, 3, "s")]),
    ("AQ3 / AU1: K4 claw + e12 (4 h)", cycle_pos(4),
     [(0, 1, "h"), (1, 2, "h"), (2, 3, "s"), (3, 0, "h"),
      (0, 2, "h"), (1, 3, "s")]),
]

EDGE_STYLE = {
    "s": dict(color="#7f7f7f", lw=1.4),
    "h": dict(color="#c1272d", lw=2.6),
}


def fig_graphs():
    ncols, nrows = 6, 3
    fig, axes = plt.subplots(nrows, ncols, figsize=(11.5, 6.4))
    for ax, (title, pos, edges) in zip(axes.flat, PANELS):
        for e in edges:
            if e[0] == "arc":
                _, i, j, t, bend = e
                st = EDGE_STYLE[t]
                arr = FancyArrowPatch(
                    pos[i], pos[j], connectionstyle=f"arc3,rad={bend}",
                    arrowstyle="-", shrinkA=4, shrinkB=4, **st)
                ax.add_patch(arr)
            else:
                i, j, t = e
                st = EDGE_STYLE[t]
                ax.plot([pos[i][0], pos[j][0]], [pos[i][1], pos[j][1]],
                        solid_capstyle="round", **st)
        for i, (x, y) in pos.items():
            ax.plot([x], [y], "o", ms=7, color="#222222", zorder=5)
            ax.text(x, y, str(i), color="white", fontsize=5.5,
                    ha="center", va="center", zorder=6)
        xs = [p[0] for p in pos.values()]
        ys = [p[1] for p in pos.values()]
        pad = 0.45
        ax.set_xlim(min(xs) - pad, max(xs) + pad)
        if any(e[0] == "arc" for e in edges):
            # banana panels: leave room for the parallel-edge arcs
            ax.set_ylim(min(ys) - 1.25, max(ys) + 1.25)
        else:
            ax.set_ylim(min(ys) - pad, max(ys) + pad)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=6.8)
    for ax in axes.flat[len(PANELS):]:
        ax.axis("off")
    handles = [
        plt.Line2D([0], [0], color="#7f7f7f", lw=1.4, label="scalar edge"),
        plt.Line2D([0], [0], color="#c1272d", lw=2.6,
                   label="graviton (spin-2 TT) edge"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=2, fontsize=9,
               frameon=False, bbox_to_anchor=(0.5, -0.01))
    fig.suptitle("Graphs of the Gate-1 table: topology and edge types", fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.90, bottom=0.06,
                        hspace=0.65, wspace=0.25)
    fig.savefig(HERE / "graphs.png", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    fig_psi_values()
    fig_graphs()
    print("wrote psi_values.png, graphs.png")
