import matplotlib.pyplot as plt
import numpy as np

transformaciones = ['T1', 'T2', 'T3', 'T4', 'T5']
speedup_real = [0.0429, 0.1021, 0.4675, 0.2227, 0.3013]

N = np.arange(1, 33)
p = 1.0
S_amdahl = 1 / ((1 - p) + p / N)

fig, ax = plt.subplots(figsize=(9, 6), dpi=300)
ax.plot(N, S_amdahl, 'b--', linewidth=2, label='Curva teorica Amdahl (p=1.0)')

# Todos los puntos en X=4, labels a la derecha con posición fija
for t, s in zip(transformaciones, speedup_real):
    color = 'green' if t == 'T4' else 'red'
    size = 180 if t == 'T4' else 80
    ax.scatter([4], [s], s=size, c=color, zorder=5,
               edgecolors='black', linewidth=0.8)
    # Label a la derecha
    ax.annotate(f'{t}: S={s:.4f}', (4, s),
                xytext=(15, 0), textcoords='offset points',
                fontsize=10, va='center', ha='left',
                fontweight='bold' if t == 'T4' else 'normal')

ax.axhline(y=1, color='gray', linestyle=':', linewidth=1.2, label='S=1 (referencia)')
ax.scatter([], [], s=180, c='green', edgecolors='black', label='T4 (foco individual)')
ax.scatter([], [], s=80, c='red', edgecolors='black', label='Otras transformaciones')

ax.set_xlabel('Numero de executors (N)', fontsize=11)
ax.set_ylabel('Speedup S(N)  (escala logaritmica)', fontsize=11)
ax.set_title('Speedup medido vs. curva teorica de Amdahl\nPE-U4 BCEL - dataset OULAD, N=4 executors', fontsize=12)
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 33)
ax.set_yscale('log')
ax.set_ylim(0.01, 40)

plt.tight_layout()
plt.savefig('fig_speedup.png', dpi=300, bbox_inches='tight')
print("OK: fig_speedup.png regenerado")