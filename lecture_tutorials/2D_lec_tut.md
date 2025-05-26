# Lecture tutorial 2D

## Using E- and B-fields to deflect electrons: Velocity filter
`el31`	

$$F_e = F_b$$
$$q E = q v B$$
$$v = \frac{E}{B}$$

---

## Determine $\frac{e}{m}$
`em39` 

Assuming a charged particle moving perpendicular to an uniform magnetic field, there will be a forces exerted on the particles.
The force will deflect the particle and, as the force is always perpendicular to the direction of movement, causes the particle to move on a circular path (if the charged particles stays within the magnetic field the entire time) with a centripetal acceleration magnitude of $a = \frac{v^2}{r}$ (see mechanics lectures).
For a circular trajectory, the centripetal force and the force due to the magnetic field must be equal
$$ \sum F = m a$$
$$F_b = F_r$$
$$e v B = \frac{m v^2}{r}$$
$$e B = \frac{m v}{r}$$
$$\frac{e}{m} = \frac{v}{B r}$$

The velocity of the charged particles, i.e. electrons, is unknown but we can derive it from the energy conservation at the anode-cathode, with the potential energy being equal to $U = q V$:
$$U = K$$
$$e V= \frac{m}{2}v^2$$
$$v = \sqrt{\frac{2 e V}{m}}$$

Putting everything together, we obtain
$$\frac{e}{m} = \frac{\sqrt{\frac{2 e V}{m}}}{B r}$$

Squaring the equation and we get our final relationship:
$$\frac{e^2}{m^2} = \frac{\frac{2 e V}{m}}{B^2 r^2}$$

$$\frac{e}{m} = \frac{2 V}{B^2 r^2}$$

Now this servers for a single measurement, but if we repeat if while varying the magnetic field and measuring the resulting radius, we obtain can solve it via a [linear regression](https://hydra.ovgu.de/praktikumshelfer.html):
$$\frac{1}{r} = \sqrt{\frac{e}{2 m V}} B$$

The slope $s$ will be $\sqrt{\frac{e}{2 m V}}$. Thus, the $e/m$ is obtained from the slope as:
$$\frac{e}{m} = 2 V s^2$$

**Are the results the same for electrons traveling clock- or anti-clockwise?**

FYI: The numerical value of $\frac{e}{m_e}$ is 1.759 $\times 10^{11}$ C/kg.

---
## Long distance power lines
`ew08`	

$$\frac{V_1}{V_2} = \frac{I_2}{I_1} = \frac{N_1}{N_2}$$
$$P = V I$$
$$P_{\rm loss} = I^2 R_{\rm cable}$$

---
## High voltage &amp; high current transformer
`ew03`

$$\frac{V_1}{V_2} = \frac{I_2}{I_1} = \frac{N_1}{N_2}$$

* "Hörner Blitzableiter"
* break down voltage of air about $3 \times 10^6$ kV/m
* corona discharge a.k.a. "weak spark" around conductor but not "jump across gap" (corona discharge is a localized electrical discharge that occurs when the electric field near a conductor is strong enough to ionize the surrounding air, but not strong enough to cause a full electrical breakdown or arc)
* **lighter causes ionized air to generate plasma** (*ionization* = breaking apart a neutral air molecule into a positive ion + free electron; *plasma* = ionized gas made of free electrons and positive ions that conducts electricity and responds to electric and magnetic fields)
* thermodynamics cause plasma beam to rise


