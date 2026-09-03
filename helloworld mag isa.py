import numpy as np
import matplotlib.pyplot as plt

# PPF param
ell = np.linspace(0, 100, 400)
X = np.sqrt(ell)
Y = 2 * np.sqrt(100 - ell)

# Equilibria (computed earlier)
X_pcm, Y_pcm = 5*np.sqrt(2), 10*np.sqrt(2)    # ~7.071, 14.142
X_mon, Y_mon = 2*np.sqrt(5), 8*np.sqrt(5)     # ~4.472, 17.888

# Price-line intercepts: Y = b - r*X  -> b = Y + r*X
r_pcm = 2.0
r_mon = 1.0
b_pcm = Y_pcm + r_pcm * X_pcm
b_mon = Y_mon + r_mon * X_mon

# Plot
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(X, Y, color='black', lw=1.8, label='PPF')
ax.plot(X_pcm, Y_pcm, 'o', color='darkred', label='E_PCM (7.07,14.14)')
ax.plot(X_mon, Y_mon, 'o', color='red', label='E_MON (4.47,17.89)')

# Price lines (draw across X range)
x_line = np.linspace(0, 11, 200)
ax.plot(x_line, b_pcm - r_pcm*x_line, linestyle='--', lw=1.4, label='Price line (PCM), slope=-2')
ax.plot(x_line, b_mon - r_mon*x_line, color='red', lw=1.6, label='Price line (MON), slope=-1')

# dashed projection lines
ax.vlines([X_pcm, X_mon], ymin=0, ymax=[Y_pcm, Y_mon], colors=['darkred','red'], linestyles='dotted')
ax.hlines([Y_pcm, Y_mon], xmin=0, xmax=[X_pcm, X_mon], colors=['darkred','red'], linestyles='dotted')

# labels & annotations
ax.text(X_pcm+0.1, Y_pcm+0.4, 'E₁ (PCM)\n(7.07,14.14)', color='darkred')
ax.text(X_mon+0.1, Y_mon+0.4, 'E₂ (MON)\n(4.47,17.89)', color='red')
ax.annotate('Move →', xy=(X_mon, Y_mon), xytext=(X_mon+1, Y_mon-2),
            arrowprops=dict(arrowstyle='->', color='red'))

# numeric summary box
summary = (
    "PCM totals: X=7.07, Y=14.14\n"
    "X_A=X_B=3.535, Y_A=Y_B=7.071\n"
    "U_A=10, U_B=5, W=50\n\n"
    "MON totals: X=4.472, Y=17.888\n"
    "X_A=X_B=2.236, Y_A=Y_B=8.944\n"
    "U_A≈8.944, U_B≈4.472, W≈40"
)
ax.text(11.1, 15, summary, fontsize=9, va='top')

ax.set_xlim(-0.5, 11)
ax.set_ylim(-1, 21)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('PPF, PCM vs Monopoly-on-Y (price doubled)')
ax.legend(loc='lower left')
plt.tight_layout()
plt.show()