import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.patheffects import Normal
from matplotlib.patheffects import Stroke


text = "Python4DS"

cmap = plt.cm.cividis
font = FontProperties()
font.set_name("Fira Code Bold")


def get_logo():
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.set_facecolor("w")
    for x in np.linspace(0, 1, 100):
        lw, color = x * 225, cmap(1 - x)
        for i, letter in enumerate([x for x in text]):
            t = ax.annotate(
                letter,
                (i*50, 0),
                va="center",
                size=40,
                ha="center",
                zorder=-lw + 1,
                color="#6b5496",
            )
            t.set_path_effects([Stroke(linewidth=lw, foreground=color)])
    ax.set_ylim(-60, 60)
    ax.set_xlim(-60, 450)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("logo.png")

get_logo()
