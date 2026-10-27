
# Why Do Atoms Radiate?

*Classical physics predicts that atoms should collapse. Quantum mechanics makes them stable. So why do excited atoms still emit light?*

**Status:** Working outline — 26 October 2026  
**Series:** Atomic Radiation, Post 1  
**Purpose:** Establish the classical instability of atoms, explain how quantum stationary states resolve it, and end with the unanswered question of spontaneous emission.

## The central story

A classical electron orbiting a proton continuously accelerates and therefore radiates energy. It should spiral into the nucleus in a tiny fraction of a second.

Quantum mechanics replaces electron trajectories with stationary wavefunctions. The resulting electron clouds can remain unchanged in time. This solves the classical stability problem.

But quantum mechanics also allows superpositions of stationary states. Their interference can produce oscillating electric dipole moments, providing a connection between atomic quantum mechanics and classical electromagnetic radiation.

The strength of this dipole depends on the participating orbitals. Some combinations produce a strong dipole, others a weaker dipole, and some produce no electric dipole at all.

This brings us to the central puzzle: an atom prepared in a pure excited state has no oscillating mean dipole moment. Yet real excited atoms spontaneously emit light.

**The article ends with that question.** The answer belongs in the next post.

---

## The Atom That Shouldn't Exist

## The atom that shouldn't exist

### Opening: start with antennas

- A radio transmitter is charges sloshing back and forth in a wire, and the wire radiates.
- A receiving antenna is the same wire run in reverse. The wave shakes the charges, and we read the signal.
- An atom is a very small antenna, so we ask whether it behaves like one.

### The oscillating dipole

- The dipole moment is charge times displacement. For an electron at position $\mathbf{x}$ from the nucleus, $\mathbf{p} = -e\,\mathbf{x}$, in units of C·m.
- If the electron swings back and forth, $p(t) = p_0 \cos\omega t$. Here $p_0$ is the amplitude: the charge times how far it swings.
- The average radiated power is

$$P = \frac{\mu_0\,\omega^4\,p_0^2}{12\pi c}.$$

- Why $\omega^4$: the acceleration is $\omega^2 x$, and the power goes as acceleration squared. Doubling the frequency gives 16 times the power at the same swing, which is also why the sky is blue.
- Why $p_0^2$: the radiated field is proportional to $p_0$, and the power is proportional to the field squared. Doubling the swing gives 4 times the power.
- The radiation is not sent equally in all directions, as the figure below shows.

### Figure 1

*(placeholder: two-panel dipole figure)*

*Figure 1. Radiation from a dipole. Left: a charge oscillating along a line radiates in a doughnut-shaped pattern, with power proportional to $\sin^2\theta$. It is strongest sideways and zero along the axis of oscillation. Right: a charge circulating in a plane is two linear dipoles at right angles and a quarter period apart. Its pattern, proportional to $1+\cos^2\theta$, is never zero, and it radiates twice the total power of a single linear dipole with the same $p_0$. Both panels share one scale.*

### The circulating electron

- A circular orbit is two linear oscillations at 90° in space and 90° in phase.
- The cross terms average out and the two powers add, so the total is constant in time:

$$P = \frac{\mu_0\,\omega^4\,p_0^2}{6\pi c}.$$

- For circular motion $p_0 = e\,a_0$, where $a_0$ is the orbit radius.

### Plugging in the Bohr atom

- $p_0 = e\,a_0 \approx 8.5\times10^{-30}$ C·m.
- $\omega = v/a_0 \approx 4.1\times10^{16}$ rad/s, which is one orbit every 152 as.
- This gives $P \approx 4.7\times10^{-8}$ W, small in watts but large for an atom.
- The binding energy is 13.6 eV, or $2.2\times10^{-18}$ J. Dividing energy by power gives a lifetime of about 47 ps.
- The dipole formula needs the source to be much smaller than the wavelength. Here the orbit is 0.053 nm and the wavelength is about 46 nm, so it holds.

### A more careful estimate

- The 47 ps estimate assumes the power stays at its starting value.
- In reality the orbit shrinks, the acceleration grows, and the power rises steeply (as $1/r^4$). Integrating the collapse gives a time exactly 3 times shorter, about 16 ps.
- The energy comes out of the electron because its own retarded field acts back on it with a force opposing its motion. This is radiation reaction.
- Both estimates are nonrelativistic, and either way the conclusion is that a classical atom would last picoseconds, not forever.

### Bridge

- Classical physics says atoms should be unstable, yet they exist. What changes when the electron is described quantum mechanically?


---

## Quantum Mechanics to the Rescue

### Purpose

Introduce quantum stationary states without deriving the entire hydrogen atom.

### Narrative

- Replace the classical electron orbit with a quantum wavefunction.
- The hydrogen atom has discrete energy eigenstates.
- Each stationary state has a time-independent probability density.
- The electron cloud does not orbit the nucleus like a classical particle.
- A stationary state has no oscillating electric dipole expectation value.
- This resolves the immediate classical stability problem within the isolated-atom model.
- Importantly, excited states are also stationary solutions of the isolated atomic Hamiltonian.

### Equations

\[
\hat H\psi_n=E_n\psi_n.
\]

\[
\Psi_n(\mathbf r,t)
=
\psi_n(\mathbf r)e^{-iE_nt/\hbar}.
\]

Therefore:

\[
|\Psi_n(\mathbf r,t)|^2
=
|\psi_n(\mathbf r)|^2.
\]

### Bridge

A single stationary state has a static electron cloud. But quantum mechanics also allows coherent superpositions of different stationary states.

---

## When Electron Clouds Oscillate

### Purpose

Explain how coherent superpositions create time-dependent charge distributions and electric dipole moments, and why the dipole strength depends on the participating orbitals.

### Narrative

- Combine two stationary energy eigenstates coherently.
- Their relative phase changes in time.
- Interference makes the electron probability density time-dependent.
- The electric dipole moment depends on the spatial structure of the interference term.
- The relevant quantity is the transition dipole matrix element.
- Compare three hydrogen examples, using consistent visualization scales.

### Equations

\[
|\Psi(t)\rangle
=
c_g e^{-iE_gt/\hbar}|g\rangle
+
c_e e^{-iE_et/\hbar}|e\rangle.
\]

The electric dipole operator is

\[
\hat{\mathbf d}=-e\mathbf r.
\]

The transition dipole is

\[
\mathbf d_{ge}
=
-e\langle g|\mathbf r|e\rangle.
\]

For a coherent superposition, the interference contribution to the mean dipole oscillates at the transition frequency

\[
\omega_{eg}=\frac{E_e-E_g}{\hbar}.
\]

### Figure 2 — A strong oscillating dipole: 1s–2p

**Concept:** Visualize a coherent superposition of hydrogen 1s and 2p orbitals.

Show the electron cloud at several phases of the oscillation, together with the changing electric dipole moment.

**Provisional caption:**

*Figure 2. A strong oscillating dipole. A coherent superposition of the hydrogen 1s and 2p orbitals produces an oscillating electron probability distribution. Interference between the two wavefunctions creates a relatively strong electric dipole moment, with a transition dipole matrix element of approximately 0.745 ea₀.*

### Figure 3 — A weaker oscillating dipole: 1s–3p

**Concept:** Repeat the visualization for a 1s–3p superposition, preserving the same spatial and dipole-arrow scales.

The more extended 3p orbital and its radial structure result in a smaller transition dipole.

**Provisional caption:**

*Figure 3. A weaker oscillating dipole. Replacing the 2p orbital with 3p produces a more spatially extended electron cloud. Its radial structure leads to partial cancellation in the dipole integral. The resulting transition dipole matrix element is approximately 0.298 ea₀, only 40% of that for 1s–2p.*

### Figure 4 — An oscillating cloud without an electric dipole: 1s–2s

**Concept:** Visualize the coherent superposition of two s orbitals.

The probability distribution changes in time, but remains spherically symmetric. Its center of charge does not move.

**Provisional caption:**

*Figure 4. An oscillating cloud without an electric dipole. A coherent superposition of the hydrogen 1s and 2s orbitals also produces a time-dependent electron probability distribution. However, spherical symmetry ensures that the electric dipole moment remains exactly zero. The electron cloud changes its radial distribution without shifting its center of charge.*

### Figure design notes

- Treat Figures 2–4 as a consistent visual series.
- Use a common rendering style.
- Preserve a common spatial scale wherever possible.
- Preserve the same scale for dipole arrows.
- Consider animated electron-cloud visualizations.
- A two-dimensional cross-section may communicate interference more clearly than a complicated three-dimensional rendering.
- Distinguish electron probability density from the electric dipole moment.

### Bridge

We have now found a way for a quantum atom to have an oscillating dipole. But what happens if the atom is prepared in a single excited energy eigenstate rather than a superposition?

---

## So Why Do Excited Atoms Radiate?

### Purpose

End with the unresolved paradox of spontaneous emission.

### Narrative

- Return to the stationary excited atomic state.
- Its probability density is time-independent.
- Its mean electric dipole does not oscillate.
- Nevertheless, excited hydrogen atoms spontaneously decay to lower energy states.
- The hydrogen 2p state, for example, has a lifetime of approximately 1.6 nanoseconds.
- Introduce Einstein's 1917 treatment of spontaneous emission and the probabilistic nature of individual emission events.
- The atomic wavefunction alone does not explain the physical origin of spontaneous emission.
- End with the missing mechanism rather than introducing its solution.

### Historical note

Einstein's 1917 radiation theory introduced the spontaneous-emission coefficient A.

A potentially useful historical quotation concerns the theory leaving the timing and direction of individual elementary processes to chance.

**Editorial TODO:** Verify the exact quotation, translation and bibliographic source before using it as a direct quote.

### Closing question

**If an excited atom has a stationary electron cloud, what makes it emit a photon?**

---

## Scope boundaries

This article does not explain:

- Quantization of the electromagnetic field.
- Vacuum fluctuations.
- The Purcell effect.
- Radiation reaction as an explanation of spontaneous emission.
- The division between vacuum fluctuations and radiation reaction in the DDC formalism.
- The Unruh effect.

These belong in later posts.

## Open work

- Develop Figure 1: a convincing illustration of the physical origin of the Abraham–Lorentz force.
- Produce the three hydrogen superposition visualizations.
- Verify transition dipole matrix elements and their numerical values.
- Check the classical collapse derivation and its assumptions.
- Locate the precise Griffiths discussion of electromagnetic self-force.
- Verify Einstein's 1917 quotation and its historical context.
- Write the article interactively, one section at a time.
