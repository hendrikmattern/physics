# Lecture Tutorial 2A


## Electroscope
`es32`

**An electroscope detects and roughly measures electric charge using electrostatic forces.
However, an electroscope cannot distinguish between positive & negative charge.**

**Structure**
- Metal rod and knob: Conducts charge.
- Thin metal leaf: Rotates due to electrostatic forces.
- Insulating support &amp; grounded enclosure: Prevents charge leakage &amp; minimize external electric influences.

**Charging by Contact:**
A charged object touches the electroscope, transferring charge:
- **Positive object**: Electrons leave, making the electroscope positive.
- **Negative object**: Electrons transfer onto the electroscope, making it negative.

Since the **rod and leaf acquire the same charge, they repel**, causing the leaf to rotate.

**Charging by Induction:** A charged object brought near the knob causes charge redistribution:
1. **Grounding**: Allows opposite charges to escape.
2. **Removing the ground** and then the object leaves the electroscope charged.


## Task L2A.1. 
Investigate the torques due to Coulomb's force and gravitation. 
Use simplifications of charge position as well as center of mass if necessary.

**Given &amp; simplifications:**
Lets assume a simple model to understand the electroscope: 
A single leaf (length $l$, mass $m$) with its the center of mass at distance $l/2$ from the pivot. 
Hence, the lever for the associated gravitational torque is $l/2$.
The force applied to the lever is $F_g \sin \theta$ for the angle $\theta$ between the vertical rod and rotated leaf (gravitational force $F_g$ points downwards in vertical direction).

Let's assume, the charges on the leaf is centered at the tip and the charge on the rod is located in a single point $r$ away from the tip. 
Therefore, the repulsion due to Coulomb's force $F_e$ times the lever $l$ generate a torque as well.

**Solution:**
At equilibrium, the torques due to repulsion and gravity balance:

$$ \tau_e = \tau_g $$

$$ F_e l = F_g  \frac{l}{2} \sin \theta $$

$$ k \frac{|q_1 q_2|}{r^2} l = mg \frac{l}{2} \sin \theta $$

$$
k \frac{|q_1 q_2|}{r^2} = \frac{mg}{2} \sin \theta
$$


---

## Electrostatics vs. Gravitation: A comparison of Coulomb's and gravitational force

### Overview of Coulomb's Law

Coulomb's Law describes the force between two point charges. It is given by:

$$
F = k \cdot \frac{q_1 \cdot q_2}{r^2}
$$

Where:
- $F$ is the force between the charges (in Newtons, N),
- $k = 8.988 \times 10^9 \, \text{Nm}^2/\text{C}^2 $ is Coulomb's constant,
- $ q_1 $ and $ q_2 $ are the magnitudes of the charges (in Coulombs, C),
- $ r $ is the distance between the charges (in meters, m).

### Comparison with Gravitational Force

The gravitational force between two masses is given by Newton's Law of Universal Gravitation:

$$
F = G \cdot \frac{m_1 \cdot m_2}{r^2}
$$

Where:
- $ F $ is the gravitational force (in Newtons, N),
- $ G = 6.674 \times 10^{-11} \, \text{Nm}^2/\text{kg}^2 $ is the gravitational constant,
- $ m_1 $ and $ m_2 $ are the masses (in kilograms, kg),
- $ r $ is the distance between the masses (in meters, m).

**Similarities** :
1. Both forces are inversely proportional to the square of the distance between the objects.
2. Both forces act along the line connecting the two objects.

**Differences:**
1. Coulomb's force depends on charge, while gravitational force depends on mass.
2. Coulomb's force can be attractive or repulsive, while gravitational force is always attractive.


## Task L2A.2. 
An electro and proton are placed $1$ µm apart. 
Compute the gravitational force between them and find the distance at which the magnitude of the Coulomb force would be equally strong.

**Given:**
- Distance electron-proton for gravitational force: $r_g = 1 \times 10^{-6} \textrm{m}$
- Charge of electron: $ q = -e = -1.602 \times 10^{-19} \, \textrm{C}$
- Charge of proton: $ q = e = 1.602 \times 10^{-19} \, \textrm{C}$
- Mass of electron: $ m_e = 9.109 \times 10^{-31} \, \textrm{kg} $
- Mass of proton: $ m_p = 1.673 \times 10^{-27} \, \textrm{kg} $
- $k = 8.988 \times 10^9 \, \text{Nm}^2/\text{C}^2 $
- $G = 6.674 \times 10^{-11} \, \text{Nm}^2/\text{kg}^2 $ 

Set the two forces equal:

$$ k \cdot \frac{e^2}{r^2} = G \cdot \frac{m_e \cdot m_p}{r_g^2} $$

$$ r = \sqrt{\frac{k}{G} \cdot \frac{e^2}{m_e \cdot m_p} \cdot r_g^2} $$

$$ r = 4.762 \times 10^{13} \, \text{m}  \approx 47,620 \, \text{million km}$$

To put that into perspective, the distance between pluto and sun is approximately $5,906 \, \textrm{million km}$ . 

## Task L2A.3.

Compare the relative strength of the Coulomb force and gravitational force between an electron and a proton:

**Given:**
- Charge of electron: $ q = -e = -1.602 \times 10^{-19} \, \textrm{C}$
- Charge of proton: $ q = e = 1.602 \times 10^{-19} \, \textrm{C}$
- Mass of electron: $ m_e = 9.109 \times 10^{-31} \, \textrm{kg} $
- Mass of proton: $ m_p = 1.673 \times 10^{-27} \, \textrm{kg} $
- $k = 8.988 \times 10^9 \, \text{Nm}^2/\text{C}^2 $
- $G = 6.674 \times 10^{-11} \, \text{Nm}^2/\text{kg}^2 $ 

**Solution:**
$$ \frac{F_{\text{e}}}{F_{\text{g}}} = \frac{k \cdot e^2 \cdot r^2 }{G \cdot m_e \cdot m_p \cdot r^2 } $$

$$ \frac{F_{\text{e}}}{F_{\text{g}}} = \frac{k \cdot e^2}{G \cdot m_e \cdot m_p} $$

$$ \frac{F_{\text{e}}}{F_{\text{g}}} = \frac{2.303 \times 10^{-28}}{1.017 \times 10^{-67}} $$

$$ \frac{F_{\text{e}}}{F_{\text{g}}} = 2.264 \times 10^{39} $$

The Coulomb force between an electron and a proton is approximately $ 10^{39} $ times stronger than the gravitational force between them. 
This demonstrates the enormous strength of the electromagnetic force compared to gravity.


## Task L2A.4.

Determine the magnitude of the charge, $Q$, that must be placed on both the Earth and the Moon to make the magnitude of the electrostatic force between them equal in to the gravitational force. 
Assume that the Earth and Moon can be treated as point charges located at their respective centers, and that they acquire equal charges.

**Given:**
- Earth's mass:  $m_E = 5.972 \times 10^{24} \, \text{kg} $
- Moon's mass: $m_M = 7.348 \times 10^{22} \, \text{kg} $
- average Earth-Moon distance $ r = 3.844 \times 10^8 \, \text{m}$ 
- $k = 8.988 \times 10^9 \, \text{Nm}^2/\text{C}^2 $
- $G = 6.674 \times 10^{-11} \, \text{Nm}^2/\text{kg}^2 $ 

**Solution:**
$$ G \cdot \frac{m_E \cdot m_M}{r^2} = k \cdot \frac{Q^2}{r^2} $$

$$ G \cdot m_E \cdot m_M = k \cdot Q^2 $$

$$ Q = \sqrt{\frac{G \cdot m_E \cdot m_M}{k}} $$
  
$$ Q =  5.714 \times 10^{13} \, \text{C} $$

Both the Earth and the Moon would need to have charges of approximately $5.714 \times 10^{13} \, \text{C} $ to exert the same magnitude of electrostatic and gravitational force.
That is an absurd amount of charge, i.e. would require $3.567 \times 10^32$ elementary charges $e$ (number of stars in the observable universe is estimated to be around $10^{24}$ )

## Conclusion on Electrostatics vs Gravitation
- Coulomb's force and gravitational force share a similar dependence on distance $1/r^2$, but their magnitudes differ dramatically due to the constants $ k $ and $ G $.
- For charged elementary particles like electrons and protons, the Coulomb force dominates over the gravitational force by many orders of magnitude.
- However, for massive objects like planets and stars, the gravitational force dominates, since astronomical bodies are typically electrically neutral or have negligible net charge. This allows gravity to govern large-scale structures in the universe, such as planetary orbits, galaxy formation, and black holes, despite being vastly weaker at the microscopic scale.

---
## Charge distributions and net force 
Let's investigate the net Coulomb force for different charge distributions. 

## Task L2A.5.
Consider two spatially fixed charges, $+2e$ and $+4e$, placed along a straight line. 
Where should an electron be placed along this line so that it experiences zero net force due to these charges? 
Use Coulomb's Law to determine the position relative to one of the charges.

**Given:**
* $Q_1 = +2e$
* $Q_2 = +4e$
* $Q_3 = -1e$
* $e = 1.602 \times 10^{-19} \, \textrm{C}$
* $x$ as the relative distance between the $Q_1$ and $Q_3$ and $x-1$ relative distance from $Q_2$ to $Q_3$ such that their sum is $1$

**Solution:**

$$F_{31} = F_{32}$$
$$ k \frac{Q_1 Q_3}{x^2} = k \frac{Q_2 Q_3}{(x-1)^2}$$
$$ \frac{-2e^2}{x^2} = \frac{-4e^2}{(x-1)^2}$$
$$ \frac{-2}{x^2} = \frac{-4}{x^2-2x+1}$$
$$ \frac{1}{x^2} = \frac{2}{x^2-2x+1}$$
$$ x^2-2x+1 = 2x^2$$
$$ 0 = x^2 +2x -1$$
$$ x_{1,2} = - \frac{2}{2} \pm \sqrt{\frac{4}{4} + 1} = -1 \pm \sqrt{2}$$ 
$$ x = \sqrt{2} - 1 \approx 0.414 $$

---
## Electric field of an electric dipole
An electric dipole consists of two equal charges but with opposite sign, i.e. $+Q$ and $-Q$. 
The charges are separated by the distance $l$. 

## Task 2A.6.
What is the strength of electric field produced by a dipole (assume no other external electric field present).
Let think about any point $P$ that is placed perpendicularly away from the bisector of the dipole and at a distance $r$.

**Given:**
* distance of each charge to the point $P$ with $R^2=r^2 + \frac{l^2}{4}$ (hypotenuse)
* Coulomb's law in electric field form $E = \frac{1}{4 \pi \varepsilon_0} \frac{Q}{R^2}$
* two fields produced by the positive and negative charge of the dipole, i.e. $\vec{\bf{E_+}}$ and $\vec{\bf{E_-}}$
* the components of the field perpendicular to the bisector cancel each other (in terms of force: repulsion away and attraction towards dipole cancel)
* the magnitude of the fields is $E_+ = E_- = \frac{1}{4 \pi \varepsilon_0} \frac{Q}{r^2 + \frac{l^2}{4}} $ 

**Solution:**
$$ \vec{\bf{E}} = \vec{\bf{E_+}} + \vec{\bf{E_-}} $$
* only consider the components along x (y cancels due to symmetry, see above) with the angle $\theta$
$$ E = 2E_+ \cos \theta = \frac{2}{4 \pi \varepsilon_0} \frac{Q}{r^2 + \frac{l^2}{4}}  $$
* with $\cos \theta = \frac{l}{2\sqrt{r^2 + \frac{l^2}{4}}} $
$$ E = \frac{2}{4 \pi \varepsilon_0} \frac{Q}{r^2 + \frac{l^2}{4}} \frac{l}{2\sqrt{r^2 + \frac{l^2}{4}}} $$

$$ E = \frac{1}{4 \pi \varepsilon_0} \frac{Q}{r^2 + \frac{l^2}{4}} \frac{l}{(r^2 + \frac{l^2}{4})^{\frac{1}{2}}} = \frac{1}{4 \pi \varepsilon_0} \frac{Q l}{(r^2 + \frac{l^2}{4})^{\frac{3}{2}}}$$
* with the **dipole moment** $p = Q l$
$$ E = \frac{1}{4 \pi \varepsilon_0} \frac{p}{(r^2 + \frac{l^2}{4})^{\frac{3}{2}}}$$
* for $l \gg r$:
$$ E = \frac{1}{4 \pi \varepsilon_0} \frac{p}{r^3}$$

Thus, the electric field of the dipole decreases rapidly with increasing distance. 
From afar, i.e. $l \gg r$, the two opposite charges $+Q$ and $-Q$ effectively cancel each other.

---

## Applications of Gauss's law
Lets apply Gauss's law to a non-conducting sphere.


## Task L2A.7. 
Derive the electric field of a non-conducting solid sphere of radius $r_0$ and total charge $Q$ which is uniformly distributed within the sphere using Gauss’s law.

**Given:**  
* solid sphere of charge with total charge $Q$ uniformly distributed throughout its volume
* radius of the sphere is $r_0$  
* seek the electric field $\vec{\bf{E}}$ at a distance $r$: 
  * **Outside the sphere**: $r > r_0$
  * **Inside the sphere**: $r < r_0$  
* Gauss’s law:
$$ \oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{\text{enc}}}{\varepsilon_0} $$

**Solution:**

*Case 1:  outside the sphere $ (r > r_0) $*

* choose a Gaussian surface:
  * since the charge is **spherically symmetric**, we choose a **spherical Gaussian surface** of radius $r$, centered at the origin
  * charge enclosed by this surface is the total charge $Q$  

* apply Gauss’s law:
$$ \oint_S E dA = \frac{Q}{\varepsilon_0} $$
* since $E$ is constant over the sphere and $\oint_S dA = 4 \pi r^2$:
$$ E (4\pi r^2) = \frac{Q}{\varepsilon_0} $$
$$ E = \frac{Q}{4\pi \varepsilon_0 r^2} $$

This is identical to the field of a **point charge** \( Q \), meaning a **spherically symmetric charge distribution behaves like a point charge outside**.

*Case 2: inside the sphere $(r < r_0)$*

* total charge is uniformly distributed throughout the volume
* **charge density** $\rho$ is:
$$ \rho = \frac{Q}{\frac{4}{3} \pi r_0^3} $$
* charge enclosed within a sphere of radius $r$ is:
$$ Q_{\text{enc}} = \rho \cdot \frac{4}{3} \pi r^3 $$
$$ Q_{\text{enc}} = \frac{Q}{\frac{4}{3} \pi r_0^3} \cdot \frac{4}{3} \pi r^3 $$

$$ Q_{\text{enc}} = Q \frac{r^3}{r_0^3} $$

* apply Gauss’s law:  
$$ \oint_S E dA = \frac{Q_{\text{enc}}}{\varepsilon_0} $$
$$ E (4\pi r^2) = \frac{Q r^3}{\varepsilon_0 r_0^3} $$
$$ E = \frac{Q}{4\pi \varepsilon_0 r_0^3} \cdot r $$

This shows that **inside the sphere, the electric field increases linearly with $r$.**  

**Summary:**  
$$
\mathbf{E} =
\begin{cases}
\frac{Q}{4\pi \varepsilon_0 r^2}, & r > r_0 \quad \text{(Outside the sphere, behaves like a point charge)} \\
\frac{Q}{4\pi \varepsilon_0 r_0^3} r, & r < r_0 \quad \text{(Inside the sphere, increases linearly with the radius)}
\end{cases}
$$


---
## Potential &amp; voltage

Lets investigate the electric potential of a point charge which, eventually, give use the *Coulomb potential equation*. 

## Task L2A.8.
Express the electric potential of a point charge. 

**Given:**
* investigate the potential difference, i.e. voltage between point $A$ and $B$: $V_{BA} = - \int_{A}^{B} \vec{\bf{E}} d\vec{\bf{l}} $
* the distance for point $A$ &amp; $B$ are $r_A$ &amp; $r_B$, respectively
* electric field due to a point charge is $ E= \frac{1}{4 \pi \epsilon_0} \frac{Q}{r^2} $ (Coulomb's law in electric field form)
* for the integral and a positive point charge $Q$, we consider paths oriented radially away from the charge in the symmetrical electrical field, i.e. the path $d\vec{\bf{l}}$ becomes $dr$

**Solution:**

* combining all we know, the electric potential of a point charge can be expressed as:

$$ V_{BA} = - \int_{A}^{B} \vec{\bf{E}} d\vec{\bf{l}} = - \frac{Q}{4 \pi \epsilon_0} \int_{r_A}^{r_B} \frac{1}{r^2} d r = -\frac{1}{4 \pi \epsilon_0} (\frac{Q}{r_B} - \frac{Q}{r_A}) $$

* if we set the electric potential zero at infinity: $V_B = 0 \textrm{ at } r_B = \infty$, we obtain the voltage $V$ at the distance $r$ of a point charge:

$$ V = \frac{1}{4 \pi \epsilon_0} \frac{Q}{r} \quad \textrm{for a point charge with } V=0 \textrm{ at } r=\infty$$

This expression is also called the *Coulomb potential* as it originates from Coulomb's law.
The potential is zero at infinity and increase (decreases) linearly towards the positive (negative )charge.


**FYI:** We can apply the principle of *superposition* to compute the potential due an *arbitrary charge distribution* by computing first the potential for each charge individually and, subsequently, obtain the total potential  by integrating over the potentials of all individual charges: 

$$ V = \frac{1}{4 \pi \epsilon_0} \int \frac{dq}{r} $$

with $dq$ being a infinitesimal small portion of the charge and $r$ its distance of the point where $V$ should be determined.

