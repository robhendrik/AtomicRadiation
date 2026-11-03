"""Figure 2 — two histories from an initial fluctuation.
Run: python figure2_events_effects_v2.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT = Path(__file__).with_name('figure2_events_effects.png')
BG = '#050816'
FG = '#dfe7f5'
ATOM = '#7fd0ff'
FIELD = '#f3c74b'
CORR = '#ff9d68'
RESPONSE = '#d9e2f5'
GUIDE = '#536177'
FIGSIZE = (12.5, 9.2)  # taller: room for formulas and panel spacing
DPI = 200

X0, X1 = 0.22, 0.79
Y_ATOM, Y_FIELD = 0.72, 0.27


def point(ax, x, y, color, s=90):
    ax.scatter(x, y, s=s*3.4, color=color, alpha=.075, edgecolors='none', zorder=7)
    ax.scatter(x, y, s=s*1.7, color=color, alpha=.13, edgecolors='none', zorder=8)
    ax.scatter(x, y, s=s, color=color, edgecolors='none', zorder=9)


def star(ax, x, y, color):
    """Large and unmistakable source event (with soft halo)."""
    ax.scatter(x, y, s=2400, color=color, alpha=.045, edgecolors='none', zorder=8)
    ax.scatter(x, y, s=950, color=color, alpha=.12, edgecolors='none', zorder=9)
    ax.scatter(x, y, s=510, marker='*', facecolor='#fff5d5', edgecolor=color,
               linewidth=1.5, zorder=12)
    ax.scatter(x, y, s=40, color='white', edgecolors='none', zorder=13)


def arrow(ax, xy0, xy1, color=RESPONSE, lw=2.7):
    ax.annotate('', xy=xy1, xytext=xy0,
                arrowprops=dict(arrowstyle='-|>', color=color, lw=lw,
                                mutation_scale=20, shrinkA=0, shrinkB=0), zorder=5)


def wiggle(ax, y):
    s = np.linspace(0, 1, 700)
    xx = X0 + .018 + (X1-X0-.04)*s
    yy = y + .012*np.sin(2*np.pi*5.8*s)*np.sin(np.pi*s)**.3
    ax.plot(xx, yy, color=CORR, lw=3.5, solid_capstyle='round', zorder=6)


def panel(ax, vacuum):
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    ax.set_facecolor(BG); ax.axis('off')
    title = 'Vacuum fluctuations' if vacuum else 'Radiation reaction'
    ax.text(.50,.965,title,color=FG,fontsize=21,ha='center',va='top')
    # Two times: light dashed guide with labels below the title, avoiding C/chi
    for x, label in [(X0,r"$t'$"),(X1,r'$t$')]:
        ax.plot([x,x],[.15,.79], color=GUIDE, lw=1, ls=(0,(3,4)),alpha=.45,zorder=0)
        ax.text(x,.815,label,color=FG,fontsize=15,ha='center',va='bottom')
    ax.text(.095,Y_ATOM,'Atom',color=ATOM,fontsize=17,ha='right',va='center')
    ax.text(.095,Y_FIELD,'Field',color=FIELD,fontsize=17,ha='right',va='center')

    origin_y = Y_FIELD if vacuum else Y_ATOM
    response_y = Y_ATOM if vacuum else Y_FIELD
    # Instantaneous perturbation: vertical at t'. The star is the trigger.
    arrow(ax,(X0,origin_y+.045 if vacuum else origin_y-.045),
          (X0,response_y-.035 if vacuum else response_y+.035),color=RESPONSE,lw=2.8)
    point(ax,X0,response_y, ATOM if vacuum else FIELD,s=115)

    # Two parallel histories after the initial event
    wiggle(ax,origin_y)
    arrow(ax,(X0+.023,response_y),(X1-.018,response_y))
    point(ax,X1,Y_ATOM,ATOM,s=105)
    point(ax,X1,Y_FIELD,FIELD,s=105)
    star(ax,X0,origin_y,FIELD if vacuum else ATOM)

    # Labels far from lines; avoid time labels/title
    if vacuum:
        ax.text(.51,.785,r'$\chi_A(t,t\prime)$',color=RESPONSE,fontsize=17,ha='center',va='bottom')
        ax.text(.51,.195,r'$C_F(t,t\prime)$',color=CORR,fontsize=17,ha='center',va='top')
    else:
        ax.text(.51,.785,r'$C_A(t,t\prime)$',color=CORR,fontsize=17,ha='center',va='bottom')
        ax.text(.51,.195,r'$\chi_F(t,t\prime)$',color=RESPONSE,fontsize=17,ha='center',va='top')

    # right-side bracket and one-word label
    xb=.86
    ax.plot([xb,xb],[Y_FIELD,Y_ATOM],lw=1.5,color=FG,alpha=.50)
    ax.plot([xb-.018,xb],[Y_FIELD,Y_FIELD],lw=1.5,color=FG,alpha=.50)
    ax.plot([xb-.018,xb],[Y_ATOM,Y_ATOM],lw=1.5,color=FG,alpha=.50)
    ax.text(xb+.025,.5*(Y_FIELD+Y_ATOM),'Power',color=FG,fontsize=15,va='center')

fig,axs=plt.subplots(2,1,figsize=FIGSIZE,dpi=DPI)
fig.patch.set_facecolor(BG)
panel(axs[0],True)
panel(axs[1],False)
plt.subplots_adjust(left=.05,right=.97,top=.97,bottom=.035,hspace=.25)
fig.savefig(OUTPUT,dpi=DPI,facecolor=BG,bbox_inches='tight')
print(OUTPUT)
plt.close(fig)
