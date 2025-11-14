import numpy as np
import matplotlib.pyplot as plt

g = 9.81

# Parameters for symmetric flight
v_peak = 108.0             # m/s vertical speed at start of free-fall
T0 = 2 * v_peak / g        # duration of 0-g segment
a_hyper = 0.8 * g          # hyper-g acceleration magnitude
T1 = v_peak / a_hyper      # duration of each hyper-g phase

# Time axis
t_pullup = np.linspace(0, T1, 400)
t_free   = np.linspace(T1, T1 + T0, 800)
t_pulldn = np.linspace(T1 + T0, 2*T1 + T0, 400)
t = np.concatenate([t_pullup, t_free[1:], t_pulldn[1:]])

# State arrays
y = np.zeros_like(t)
v = np.zeros_like(t)
a = np.zeros_like(t)

y_start = 7000.0
y[0] = y_start
v[0] = 0.0

# Earth-frame acceleration: hyper-g → free-fall → hyper-g
for i, ti in enumerate(t):
    if ti <= T1:
        a[i] = a_hyper
    elif ti <= T1 + T0:
        a[i] = -g
    else:
        a[i] = a_hyper

# Integrate to get v(t) and y(t)
dt = np.diff(t, prepend=t[0])
for i in range(1, len(t)):
    v[i] = v[i-1] + a[i-1] * dt[i]
    y[i] = y[i-1] + v[i-1] * dt[i]

# ----- PLOT -----
fig, ax_y = plt.subplots(figsize=(10, 6))

# Altitude axis
ax_y.plot(t, y, label="Altitude y(t)", linewidth=2, color="tab:blue")
ax_y.set_xlabel("Time t (s)")
ax_y.set_ylabel("Altitude y(t) (m)", color="tab:blue")
ax_y.tick_params(axis='y', labelcolor="tab:blue")
ax_y.grid(True)

# Velocity axis (vertical velocity v_y(t)), hidden axis labels
ax_v = ax_y.twinx()
ax_v.spines.right.set_position(("axes", 1.12))  # shift velocity axis slightly
ax_v.plot(t, v, label="Vertical velocity $v_y(t)$", color="tab:green", linestyle="--")
ax_v.set_yticklabels([])       # hide velocity axis labels
ax_v.set_ylabel("")            # remove velocity axis label

# Acceleration axis
ax_a = ax_y.twinx()
ax_a.plot(t, a, label="Acceleration a(t)", color="tab:red", alpha=0.8)
ax_a.set_ylabel("Acceleration a(t) (m/s²)", color="tab:red")
ax_a.tick_params(axis='y', labelcolor="tab:red")

# Collect legends
lines1, labels1 = ax_y.get_legend_handles_labels()
lines2, labels2 = ax_v.get_legend_handles_labels()
lines3, labels3 = ax_a.get_legend_handles_labels()

ax_y.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3, loc="upper right")

plt.title("Symmetric Parabolic Flight: y(t),  $v_y(t)$,  and  a(t)")
plt.tight_layout()
plt.show()
