# Lecture Tutorial 2A


## Electroscope TODO
`es32`
- **Detects electric charge**.
- Two **thin metal leaves**.
- Charged leaves repel each other.
- Cannot distinguish between positive & negative charge.


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


## Task L2A.1. 
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

## Task L2A.2.

Compare the relative strength of the Coulomb force and gravitational force between an electron and a proton:

**Given:**
- Charge of electron: $ q = -e = -1.602 \times 10^{-19} \, \textrm{C}$
- Charge of proton: $ q = e = 1.602 \times 10^{-19} \, \textrm{C}$
- Mass of electron: $ m_e = 9.109 \times 10^{-31} \, \textrm{kg} $
- Mass of proton: $ m_p = 1.673 \times 10^{-27} \, \textrm{kg} $
- $k = 8.988 \times 10^9 \, \text{Nm}^2/\text{C}^2 $
- $G = 6.674 \times 10^{-11} \, \text{Nm}^2/\text{kg}^2 $ 

$$ \frac{F_{\text{Coulomb}}}{F_{\text{Gravitational}}} = \frac{k \cdot e^2 \cdot r^2 }{G \cdot m_e \cdot m_p \cdot r^2 } $$

$$ \frac{F_{\text{Coulomb}}}{F_{\text{Gravitational}}} = \frac{k \cdot e^2}{G \cdot m_e \cdot m_p} $$

$$ \frac{F_{\text{Coulomb}}}{F_{\text{Gravitational}}} = \frac{2.303 \times 10^{-28}}{1.017 \times 10^{-67}} $$

$$ \frac{F_{\text{Coulomb}}}{F_{\text{Gravitational}}} = 2.264 \times 10^{39} $$

The Coulomb force between an electron and a proton is approximately $ 10^{39} $ times stronger than the gravitational force between them. 
This demonstrates the enormous strength of the electromagnetic force compared to gravity.


## Task L2A.3.

Determine the magnitude of the charge, $Q$, that must be placed on both the Earth and the Moon to make the magnitude of the electrostatic force between them equal in to the gravitational force. 
Assume that the Earth and Moon can be treated as point charges located at their respective centers, and that they acquire equal charges.

**Given:**
- Earth's mass:  $m_E = 5.972 \times 10^{24} \, \text{kg} $
- Moon's mass: $m_M = 7.348 \times 10^{22} \, \text{kg} $
- average Earth-Moon distance $ r = 3.844 \times 10^8 \, \text{m}$ 
- $k = 8.988 \times 10^9 \, \text{Nm}^2/\text{C}^2 $
- $G = 6.674 \times 10^{-11} \, \text{Nm}^2/\text{kg}^2 $ 

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


## Task L2A.4.
Consider two fixed charges, $+2e$ and $+4e$, placed along a straight line. Where should an electron be placed along this line so that it experiences zero net force due to these charges? Use Coulomb's Law to determine the position relative to one of the charges.

1. **Setup and Visualization:**
   - Charges are aligned in a straight line: +2e on the left, -e in the middle, and +4e on the right.
   - Distance between +2e and +4e is 1 micrometer (1e-6 meters).

2. **Coulomb's Law Application:**
   - Force from +2e on electron: \( F_1 = k \cdot \frac{2e \cdot e}{x^2} \)
   - Force from +4e on electron: \( F_2 = k \cdot \frac{4e \cdot e}{(1e-6 - x)^2} \)
   - For zero net force: \( F_1 = F_2 \)

3. **Equation Setup and Simplification:**
   \[
   \frac{2}{x^2} = \frac{4}{(1e-6 - x)^2}
   \]
   \[
   (1e-6 - x)^2 = 2x^2
   \]
   \[
   1e-6 - x = \sqrt{2} \cdot x
   \]
   \[
   1e-6 = x(1 + \sqrt{2})
   \]
   \[
   x = \frac{1e-6}{1 + \sqrt{2}} \approx \frac{1e-6}{2.4142} \approx 4.14e-7 \text{ meters} = 414 \text{ nanometers}
   \]

4. **Verification:**
   - Calculate forces at \( x \approx 414 \text{ nm} \):
     \[
     F_1 \propto \frac{2}{(4.14e-7)^2} \approx 1.17e13
     \]
     \[
     F_2 \propto \frac{4}{(5.86e-7)^2} \approx 1.17e13
     \]
   - Forces are equal, confirming the calculation.

**Conclusion:**
The electron should be placed approximately 414 nanometers from the +2e charge towards the +4e charge to experience zero net force.


## e field zero between two electrons with fixed distance

## 2A.4. An electron moving through an electric field


## electron, schiefer wurf



An electron, moving a velocity v, enters perpendicularly into the space between two  charged plates. The plates generate the electric field E. how fast does the eletrcon travel when entering the eletric field to generate afterwards move on a circle within the field with a radius of 10 cm. electric field is 1000 N/C


To determine the velocity of an electron entering an electric field such that it moves in a circular path with a radius of 10 cm, we equate the electric force to the centripetal force:

\[ qE = \frac{mv^2}{r} \]

Solving for \( v \):

\[ v = \sqrt{\frac{qE \cdot r}{m}} \]

Plugging in the known values:

- \( q = 1.6 \times 10^{-19} \, \text{C} \)
- \( E = 1000 \, \text{N/C} \)
- \( r = 0.1 \, \text{m} \)
- \( m = 9.11 \times 10^{-31} \, \text{kg} \)

\[ v = \sqrt{\frac{(1.6 \times 10^{-19} \, \text{C}) \cdot (1000 \, \text{N/C}) \cdot 0.1 \, \text{m}}{9.11 \times 10^{-31} \, \text{kg}}} \]

Calculating step by step:

1. Multiply \( q \) and \( E \):

\[ 1.6 \times 10^{-19} \, \text{C} \times 1000 \, \text{N/C} = 1.6 \times 10^{-16} \, \text{N·m} \]

2. Multiply by \( r \):

\[ 1.6 \times 10^{-16} \, \text{N·m} \times 0.1 \, \text{m} = 1.6 \times 10^{-17} \, \text{N·m}^2 \]

3. Divide by \( m \):

\[ \frac{1.6 \times 10^{-17} \, \text{N·m}^2}{9.11 \times 10^{-31} \, \text{kg}} = 1.758 \times 10^{13} \, \text{m}^2/\text{s}^2 \]

4. Take the square root:

\[ v = \sqrt{1.758 \times 10^{13} \, \text{m}^2/\text{s}^2} \approx 1.326 \times 10^{6} \, \text{m/s} \]

**Final Answer:** The electron must be moving at approximately $ 1.326 \times 10^{6} $ meters per second when it enters the electric field to move in a circular path with a radius of 10 cm.


## dipole electric far field

todo

## Electric dipoles
* Two equal and opposite charges ($+Q$ and $-Q$) separated by distance $l$.
* Dipole **moment**:
$$ \vec{p} = Q \vec{l} $$
* An electric dipole consists of two equal and opposite charges ($+Q$ and $-Q$) separated by a distance $l$
* The dipole moment is defined as  
  $$\vec{\bf{p}} = Q \vec{\bf{l}}$$  
  with $\vec{\bf{l}}$ pointing from the negative to the positive charge
* In a uniform electric field, the torque on the dipole is  
  $$\vec{\bf{\tau}} = \vec{\bf{p}} \times \vec{\bf{E}}$$
* The potential energy of the dipole is given by  
  $$U = -\vec{\bf{p}} \cdot \vec{\bf{E}}$$




### Applications of Gauss's law
* Point charge:  
  $$E = \frac{1}{4\pi\epsilon_0}\frac{Q}{r^2}$$
* Charged spherical conducting shell:  
  * Outside: $$E = \frac{1}{4\pi\epsilon_0}\frac{Q}{r^2}$$  
  * Inside: $$E = 0$$
* Solid charged non-conducting sphere:  
  * Outside: $$E = \frac{1}{4\pi\epsilon_0}\frac{Q}{r^2}$$  
  * Inside: $$E = \frac{1}{4\pi\epsilon_0}\frac{Qr}{R^3}$$
* Long uniform line of charge:  
  $$E = \frac{1}{2\pi\epsilon_0}\frac{\lambda}{R}$$  
  where $\lambda$ is the charge per unit length
* Infinite plane of charge:  
  $$E = \frac{\sigma}{2\epsilon_0}$$  
  where $\sigma$ is the charge per unit area
* Near any conducting surface:  
  $$E = \frac{\sigma}{\epsilon_0}$$
* Between two closely spaced oppositely charged, parallel plates:  
  $$E = \frac{\sigma}{\epsilon_0}$$
* Reminder: There cannot be any net charge within the conductor, only on its surface


