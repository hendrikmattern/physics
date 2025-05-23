# Lecture tutorial 2B


## Millikan / Oil drop experiment
`es29` 

Set-up:
* two parallel plates generating an approximately uniform electric field $E$
* voltage $V$ and plate distance $d$ can be used to estimate $E$
* gap in between plates viewed through e.g. microscope $\rightarrow$ **up-down flip/mirror-inverted image** 
* vaporizer/atomizer/sprayer used to inset oil droplets
* due to friction, droplets charged $\rightarrow$ motion can be observed due to:
    * electrical field
    * gravitation
    * buoyancy


## Task L2B.1.
We have an oil droplet with an idealized spherical shape. The density of oil and air are $\rho_o = 900 \textrm{kg}/\textrm{m}^3$ and $\rho_a = 1.29 \textrm{kg}/\textrm{m}^3$, respectively. What fraction of the gravitational force is the buoyancy force?

### Given
* $\rho_o = 900 \textrm{kg}/\textrm{m}^3$
* $\rho_a = 1.29 \textrm{kg}/\textrm{m}^3$

### Find
$$F_b/F_g$$

### Solutions
$$V_{\textrm{sphere}}=\frac{4}{3} \pi r^3$$
$$F_g = m_{o} g = \rho_o V g = \rho_o \frac{4}{3} \pi r^3 g$$
$$F_b = m_{a} g = \rho_a V g = \rho_a \frac{4}{3} \pi r^3 g$$
$$\frac{F_b}{F_g}=\frac{\rho_a \frac{4}{3} \pi r^3 g}{\rho_o \frac{4}{3} \pi r^3 g}$$
$$\frac{F_b}{F_g}=\frac{\rho_a}{\rho_o}=0.00143$$

The strength of the buoyancy is approximately 1% of the gravitational force.

## Task L2B.2.
Imagine a spherical oil droplet ($\rho_o = 900 \textrm{kg}/\textrm{m}^3$, $r=1\mu\textrm{m}$) inside an uniform electric field generated by two charged plates (plate distance $d=3\textrm{mm}$).
The applied voltage of $981 V$ causes the droplet to hover/levitate. 
What is the charge of the droplet if we neglect buoyancy?

### Given
* $d=3\textrm{mm}$
* $V=981 \textrm{V}$
* $\rho_o = 900 \textrm{kg}/\textrm{m}^3$
* $r=1\mu\textrm{m}$

### Find
* $q$

### Solution
$$F_g = F_e$$
$$m g = q E$$
$$\rho_o \frac{4}{3} \pi r^3 g = q \frac{V}{d}$$
$$q = \frac{4 \pi r^3 \, \rho_o g d}{3 V} = 1.131 \times 10^{-19} \textrm{C}$$

## Task L2B.3
Derive the electric field very close to any conducting surface if the charge density $\sigma =\frac{Q}{A}$.

### Solution:
* a conducting material will only have an electric field outside, thus **charges accumulate only on the surface**
* if we decompose any shape of conductor, we can approximate the field near to the surface to be uniform 
* we use a Gaussian surface as a small cylindrical box that covers the charges on the surface entirely (surface can extend beyond the surface)
* according to Gauss's law, we get
$$\oint \vec{\textbf{E}} d \vec{\textbf{A}}= \frac{Q_{enc}}{\epsilon_0}$$ 
* as we assume the field to be **uniform near and perpendicular to the surface** and the area of the box to be simply $A$:
$$E A = \frac{Q_{enc}}{\epsilon_0}$$
* the charge density is $\sigma =\frac{Q}{A} \leftrightarrow Q = \sigma A$
$$E A = \frac{\sigma A}{\epsilon_0}$$
* thus, we obtain our final equation:
$$E = \frac{\sigma}{\epsilon_0}$$

Since this result is true for any conduction surface, we can also use it do describe the **field of a conducting plate** i.e. capacity if we assume that the plate are large compared to their distance and the field lines are perpendicular to the plates.

## Task L2B.4
`es28`

Starting from the force equilibrium for `es28`, derive an equation for the voltage which would be present.

### Solution
* the electrostatic force pulls the scale up, but only one plate is charge/one moves which gives us $F_e=\frac{1}{2}QE$
* gravitation force is $F_g=mg$
$$mg = \frac{1}{2}Q E$$
* using the concept about the electric field from the previous task, $E = \frac{\sigma}{\epsilon_0}=\frac{Q}{\epsilon_0 A}$, we can state:
$$mg = \frac{1}{2} Q^2 \frac{1}{\epsilon_0 A} $$ 
* the charge of a capacitor is $Q= C V = \frac{\epsilon_0 A}{d} V$
$$mg = \frac{1}{2} \frac{\epsilon_0^2 A^2}{d^2} V^2 \frac{1}{\epsilon_0 A} $$ 
$$mg = \frac{1}{2} \frac{\epsilon_0 A}{d^2} V^2 $$ 
$$V = \sqrt{\frac{2d^2 mg}{\epsilon_0 A}}$$

