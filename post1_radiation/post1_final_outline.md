# Why Do Atoms Radiate?

*Classical physics predicts that atoms should collapse. Quantum mechanics makes them stable. So why do excited atoms still emit light?*

**Status:** Working outline, 27 October 2026 (after reviewer feedback)

**Series:** Atomic Radiation, Post 1

**Purpose:** Establish the classical instability of atoms, explain how quantum stationary states resolve it, show that the classical antenna formula fed with quantum dipoles gives the right emission rates, and end with the open question of spontaneous emission from a pure excited state.

**Storyline to preserve:** classical atoms must radiate → quantum stationary states do not → superpositions can radiate → the antenna predicts the right rate → but a pure excited state has no oscillating dipole.

**Equation budget for the published version:** keep the dipole power formula, the stationary-state phase, the superposition and the decay-rate formula. The other equations (circulating dipole, Abraham–Lorentz force, transition dipole definitions, Einstein relation) go into short asides or the mathematical backbone.

## Figure list (current numbering)

0. Feature image: 1s–2p cloud at two opposite phases, metallic 3D render (PyVista)
1. Radiation patterns of a linear and a circulating dipole (PyVista, 3D)
2. Static hydrogen clouds: 1s, 2s, 2p, 3p (matplotlib, cross-sections, ±24 a₀)
3. 1s–2p superposition at four phases, with dipole curve d(φ)
4. 1s–3p superposition at four phases (same window and gamma as Fig. 3)
5. 1s–2s superposition at four phases (same window and gamma, flat dipole curve)

Figures 3–5: window ±6 a₀, 2 a₀ scale bar, dotted line = the plane z = 0, phases φ = 0, π/2, π, 3π/2, same vertical range of the dipole curve (±0.8 e a₀), brightness partly shared across the three figures. Static images are the primary figures, animated versions are extras for the website.

---

![Feature image](superposition_3d_metal_pair_1s_2p.png)
> Caption: **A hydrogen atom in a superposition of 1s and 2p, shown at two moments half an oscillation period apart. Each metallic surface encloses half of the electron probability. At φ = 0 (left) the cloud sits above the plane z = 0, half a period later (φ = π, right) it sits below it. These are two snapshots of one atom, not two objects. The sloshing of charge is an oscillating electric dipole, and an oscillating dipole radiates.**
> Alt text: Two glossy metallic egg-shaped surfaces side by side on a dark background, with a faint translucent horizontal plane between them. The left surface sits mostly above the plane, the right one is its mirror image and sits mostly below it, so each is cut by the plane.
> Source: Image created by author using PyVista (50%-probability isosurface of the electron density).

## 1. The atom that shouldn't exist

### Opening: start with antennas

- A radio transmitter is charges sloshing back and forth in a wire, and the wire radiates.
- A receiving antenna is the same wire run in reverse. The wave shakes the charges, and we read the signal.
- An atom is a very small antenna, so we ask whether it behaves like one.

### The oscillating dipole

- The dipole moment is charge times displacement. For an electron at position **x** from the nucleus, **p** = −e**x**.
- If the electron swings back and forth, p(t) = p₀ cos ωt, where p₀ is the amplitude: the charge times how far it swings.
- The average radiated power is

$$P = \frac{\mu_0\,\omega^4\,p_0^2}{12\pi c}.$$

- Why ω⁴: the acceleration is ω²x, and the power goes as acceleration squared. Doubling the frequency gives 16 times the power at the same swing.
- The same ω⁴ is the main reason the sky is blue: air molecules are driven by sunlight and re-radiate as small dipoles. (Rayleigh scattering also depends on how strongly the molecules polarize, but the fourth power of the frequency dominates.)
- Why p₀²: the radiated field is proportional to p₀, and the power to the field squared.
- The radiation is not sent equally in all directions (Figure 1).

![Figure 1](dipole_patterns_3d.png)
> Caption: **Figure 1. Radiation from a dipole. Left: a charge oscillating along a line radiates in a doughnut-shaped pattern, with power proportional to sin²θ. It is strongest sideways and zero along the axis of oscillation. Right: a charge circulating in a plane is two linear dipoles at right angles and a quarter period apart. Its pattern, proportional to 1 + cos²θ, is never zero, and it radiates twice the total power of a single linear dipole with the same p₀. Both panels share one scale. The distance of the surface from the centre shows how much power goes in that direction. It is not the shape of the wave.**
> Alt text: Two 3D radiation patterns around a vertical axis. Left, labelled "Oscillating electron" with the axis labelled "Dipole axis": a flat, light-green doughnut with a small electron and arrow on the axis, pinched to zero along the axis. Right, labelled "Circulating electron" with the axis labelled "Rotation axis": a much larger blue peanut-shaped surface, elongated along the axis with a narrow waist, enclosing a small circular orbit with an electron.
> Source: Image by author.

### The circulating electron

- A circular orbit is two linear oscillations at 90° in space and 90° in phase.
- The cross terms average out and the powers add, so the total is constant in time:

$$P = \frac{\mu_0\,\omega^4\,p_0^2}{6\pi c}.$$

- For circular motion p₀ = e a₀, with a₀ the orbit radius. This is the Larmor formula for an acceleration a = ω²a₀.

### Plugging in the Bohr atom

- p₀ = e a₀ ≈ 8.5×10⁻³⁰ C·m.
- ω = v/a₀ ≈ 4.1×10¹⁶ rad/s, one orbit every 152 as.
- P ≈ 4.7×10⁻⁸ W: tiny in watts, huge for an atom.
- Binding energy 13.6 eV = 2.2×10⁻¹⁸ J. Energy divided by power gives a lifetime of about 47 ps.
- The dipole formula needs the source to be much smaller than the wavelength: orbit 0.053 nm, wavelength about 46 nm, so it holds.

### A more careful estimate

- The 47 ps estimate assumes the power stays at its starting value.
- In reality the orbit shrinks, the acceleration grows, and the power rises as 1/r⁴. Integrating the collapse gives a time exactly 3 times shorter, about 16 ps.
- Either way, a classical atom would last picoseconds. Both estimates are nonrelativistic.

### Aside (optional): where the energy comes from

- In the classical model the energy comes out of the electron because its own retarded field acts back on it with a force opposing its motion (radiation reaction, the Abraham–Lorentz force):

$$\mathbf F_{\mathrm{AL}} = \frac{e^2}{6\pi\varepsilon_0 c^3}\,\dot{\mathbf a}, \qquad \dot{\mathbf a} = -\omega^2\mathbf v \ \text{(circular motion)}.$$

- This is the classical picture. Whether and how a quantum version of it acts is a question for later posts.

### Bridge

- Classical physics says atoms are unstable, yet they exist. What changes when the electron is described quantum mechanically?

---

## 2. Quantum mechanics to the rescue

### Purpose

- Introduce stationary states without deriving the hydrogen atom.

### Bullets

- Replace the classical orbit by a wavefunction ψ(**r**).
- Hydrogen has discrete energy eigenstates, each with its own energy Eₙ:

$$\hat H\psi_n = E_n\psi_n.$$

- Time dependence of an eigenstate is only a phase:

$$\Psi_n(\mathbf r,t) = \psi_n(\mathbf r)\,e^{-iE_nt/\hbar}, \qquad |\Psi_n(\mathbf r,t)|^2 = |\psi_n(\mathbf r)|^2.$$

- So the probability density, the "electron cloud", does not change in time, and neither does the mean electric dipole.
- A stationary state has no time-varying mean dipole, so the classical dipole-radiation mechanism predicts no emission. (Stationary states can still carry probability currents, such as 2p with m = ±1, but their density and mean dipole are constant.)
- The cloud does not orbit the nucleus like a classical particle.
- This resolves the classical collapse for the isolated atom: the radiation formula of Section 1 gives zero.
- Excited states are also stationary solutions of the isolated-atom Hamiltonian, which sets up the paradox at the end.
- Show 1s, 2s, 2p and 3p, the states used in the next section. Point out the nodes: a ring in 2s and 3p, the plane z = 0 in 2p and 3p.

### Figure 2

*(four cross-sections, common spatial scale, gamma-compressed brightness)*

![Figure 2](hydrogen_static_clouds.png)
> Caption: **Figure 2. Stationary states of hydrogen. Probability density |ψ|² in a plane through the nucleus for 1s, 2s, 2p and 3p, on a common spatial scale. Brightness is gamma-compressed and partly equalised between panels so that the diffuse states stay visible, so absolute densities cannot be compared between panels. Dark rings and lines are nodes. Each cloud is the same at every moment: the time dependence of a stationary state is only a phase, which drops out of |ψ|².**
> Alt text: Four square panels in a row, magma colours on black, each with a 10 a₀ scale bar. 1s: a small, bright, round spot. 2s: a small bright core, a dark ring around it and a faint round halo. 2p: two lobes, one above and one below a dark horizontal line through the nucleus. 3p: two small bright lobes above and below a dark horizontal line, surrounded by a dark ring and two larger, fainter outer lobes.
> Source: Image by author.

### Bridge

- A single stationary state is static. But quantum mechanics also allows superpositions of different stationary states. What does the cloud do then?

---

## 3. When electron clouds oscillate

### Purpose

- Show that a superposition makes the cloud, and the dipole, oscillate, and that the classical antenna formula, fed with quantum dipoles, gives the real emission rates.
- Three cases make the point: a strong dipole (1s–2p), a weak dipole (1s–3p), and a cloud that changes in time with no dipole at all (1s–2s).

### Bullets

- Superpose two eigenstates, a lower state g and an upper state e, with amplitudes cg and ce:

$$|\Psi(t)\rangle = c_g e^{-iE_gt/\hbar}|g\rangle + c_e e^{-iE_et/\hbar}|e\rangle.$$

- The relative phase advances as φ = (Ee − Eg)t/ħ, so the interference term between the two orbitals oscillates at

$$\omega_{eg} = \frac{E_e - E_g}{\hbar}.$$

- For real orbitals and equal weights the density is |Ψ|² = ½(ψg² + ψe²) + ψgψe cos φ.
- The first part is static. Only the cross term ψgψe cos φ moves, and it moves probability from one side of the nucleus to the other. In the feature image this is the difference between the two phases.
- The dipole moment follows the sloshing of the cloud. The operator is d̂ = −e**r** and its mean value along z is

$$\langle d_z\rangle = 2\,c_g c_e\,d_{ge}\cos\phi, \qquad d_{ge} = -e\langle g|z|e\rangle.$$

- Strength depends on the orbitals through the transition dipole dge.
- The curve below each panel in Figures 3–5 is the dipole moment d(φ) = −e⟨z⟩, not the cloud, and the marker shows the phase of the panel above it. The dipole points opposite to the displacement of the cloud, so at φ = 0, with the cloud shifted up, the marker sits at the minimum. All three curves use the same vertical range.

### From oscillating dipole to emission rate

- This is the antenna of Section 1: an oscillating dipole radiates with p₀ = 2|cg||ce||dge|. Both ingredients, the frequency ω and the dipole dge, now come from quantum mechanics, with no fitted parameter.
- Written with the decay rate Γ, the mean radiated power is

$$P = \hbar\omega\,\Gamma\,|c_g|^2|c_e|^2, \qquad \Gamma = \frac{\omega^3\, d_{ge}^2}{3\pi\varepsilon_0\hbar c^3}.$$

- The scaling Γ ∝ ω³ dge² is the ω⁴ of Section 1 divided by one power of ω, because the energy available per photon is ħω.
- For a weakly excited atom (|cg| ≈ 1) the energy stored in the excitation, |ce|²ħω, is radiated away at the rate Γ. The classical antenna reproduces the quantum decay rate.

### Figure 3: strong dipole, 1s–2p

![Figure 3](superposition_1s_2p_montage.png)
> Caption: **Figure 3. A strong oscillating dipole. Coherent equal superposition of hydrogen 1s and 2p at four moments of one period (φ = 0, π/2, π, 3π/2). The cloud sloshes along the z axis, up at φ = 0 and down at φ = π relative to the dotted line z = 0. The curve below each panel is the electric dipole moment, which oscillates with amplitude 0.745 e a₀.**
> Alt text: Four panels in a row, each showing a bright orange-white core in a purple cloud on a black background, with a dotted horizontal line through the core and a 2 a₀ scale bar. In the first panel the cloud extends upward and is dark below the line, in the second and fourth it is centred, in the third it extends downward. Under each panel a sine curve with a marker: at its minimum in the first panel, at zero rising in the second, at its maximum in the third, at zero falling in the fourth.
> Source: Image by author.

- Numbers for 1s–2p (computed): ω = 1.55×10¹⁶ rad/s (ħω = 10.2 eV), dge = 0.745 e a₀ = 6.3×10⁻³⁰ C·m.
- This gives Γ = 6.3×10⁸ s⁻¹ and a lifetime of 1.60 ns, which is the measured 2p lifetime.
- The 2p state decays only to 1s, so its natural linewidth Γ/2π is about 100 MHz (Lyman-α).

### Figure 4: weaker dipole, 1s–3p

![Figure 4](superposition_1s_3p_montage.png)
> Caption: **Figure 4. A weaker oscillating dipole. With 3p instead of 2p the cloud is more extended and the radial node causes partial cancellation in the dipole integral. The amplitude is 0.298 e a₀, 40% of the 1s–2p value. Same window and dipole scale as Figure 3. The motion is small, and the outer part of the 3p cloud lies beyond the frame.**
> Alt text: Four panels like Figure 3 for 1s–3p. The bright core stays near the centre, and the purple cloud shifts only slightly, up in the first panel and down in the third. The sine curve beneath is the same shape as in Figure 3 but about 40% as tall, with the marker at its minimum, zero, maximum and zero again.
> Source: Image by author.

- For 1s–3p: ω = 1.84×10¹⁶ rad/s and dge = 0.298 e a₀ (computed).
- The higher frequency raises the rate by (1.84/1.55)³ = 1.665, the weaker dipole lowers it by (0.298/0.745)² = 0.160. Net: Γ(3p→1s)/Γ(2p→1s) = 0.267.
- In absolute terms (computed): Γ(3p→1s) = 1.7×10⁸ s⁻¹, a partial lifetime of 6.0 ns.
- The natural linewidth depends on the total decay rates of both levels, not only on this one transition. The 3p state also decays to 2s, with A(3p→2s) ≈ 2.2×10⁷ s⁻¹ (check), so its total rate is about 1.9×10⁸ s⁻¹, its lifetime about 5.3 ns and the 1s–3p line width about 30 MHz, against 27 MHz from the partial rate alone.
- So the 1s–3p line is about 3.3 times narrower than 1s–2p, and the weak dipole in Figure 4 against the strong one in Figure 3 is the main reason.

### Figure 5: breathing mode with no dipole, 1s–2s

![Figure 5](superposition_1s_2s_montage.png)
> Caption: **Figure 5. An oscillating cloud without a dipole. The cloud breathes: at φ = 0 it is compact and bright, surrounded by a dark ring, and at φ = π the core dims and probability spreads outward into a wide halo. It stays spherically symmetric throughout, so its centre of charge never moves and the dipole is exactly zero. Same window and dipole scale as Figure 3.**
> Alt text: Four panels like Figure 3 for 1s–2s. In each the cloud is round and centred on the dotted line. In the first panel it is a bright core with a dark ring around it, in the third a dim core inside a wide faint halo, and the second and fourth are in between. Under each panel the dipole curve is a flat horizontal line, with the marker moving along it without rising or falling.
> Source: Image by author.

- This is a breathing mode: the density changes in time, but dge = 0, so the antenna predicts no dipole emission. A changing density is not enough to radiate.
- This matches the real 2s state, which is metastable: lifetime about 0.1 s, with the two-photon decay mentioned only as an aside (check).

### Technical note (optional): oscillator strength

- Cruder classical estimates, without the quantum dipole, land within a factor of 2–4 of the 1.6 ns (computed): a Bohr n = 2 orbit gives 3.0 ns, and a classical electron oscillating at ω gives 0.66 ns.
- The classical oscillator rate times the oscillator strength f = 0.416 gives exactly Γ, and f = 2mω|⟨1s|z|2p⟩|²/ħ is just the quantum dipole in disguise.

### What the antenna picture gets right, and where it stops

- With the dipole and frequency from the quantum states, the classical antenna gives the right rates and the right ratios between lines, and it correctly predicts "dark" transitions such as 1s–2s.
- Single-transition dipoles cannot capture branching: the 3p state has two decay channels.
- All of this concerns an atom in a superposition, with an oscillating dipole. The formula's power is proportional to |cg|², so it gives zero for a pure excited state.

### Bridge

- So the classical antenna, fed with quantum dipoles, works. But it works for an atom in a superposition. What about an atom in a single excited eigenstate, which has no oscillating dipole at all?

---

## 4. So why do excited atoms radiate?

### Purpose

- End with the unresolved paradox of spontaneous emission, now that the antenna picture has just succeeded in Section 3.
- Leave the reader with the contradiction, not its solution.

### The set-up: a pure excited state

- Prepare the atom in a single excited eigenstate, for example 2p, so that cg = 0 and ce = 1.
- Its cloud is the stationary cloud of Figure 2: no sloshing, no oscillating dipole, ⟨d⟩ = 0 at every moment.
- The antenna formula of Section 3 then gives P = ħωΓ|cg|²|ce|² = 0. The classical picture says this atom should sit there and shine nothing.
- Quantum mechanics agrees for the isolated atom: an eigenstate of the atomic Hamiltonian is a solution for all time, and its density never changes.

### What is actually observed

- The excited atom decays and emits a photon of energy ħω = Ee − Eg, leaving the atom in the ground state.
- For 2p the lifetime is about 1.6 ns. The rate is Γ = 6.3×10⁸ s⁻¹, exactly the number the antenna formula gave for the superposition.
- The decay is exponential: the number of excited atoms falls as e^(−Γt). Each atom decays at an unpredictable moment, and only the average is fixed.
- The direction of each photon is also random, but the distribution of many photons follows the dipole pattern of Figure 1. For 2p with m = 0 it is sin²θ around the z axis.
- The line has a natural width, about 100 MHz for 1s–2p, so the same Γ appears in the time domain and the frequency domain.

### The contradiction, stated plainly

- For a weakly excited atom (|cg| ≈ 1) the antenna and the observed decay agree: the excitation decays at the rate Γ.
- For a pure excited state the antenna gives zero, while the observed decay still happens at Γ. The antenna formula needs an oscillating dipole, and the state has none.
- So the rate has the classical form Γ ∝ ω³dge², but the classical trigger is missing.

### Why it is not a loophole in the antenna picture

- In the classical model, Larmor radiation and radiation reaction both need an accelerated charge. A stationary state has a constant mean dipole, so the classical mechanism has nothing to act on. Whether a quantum version applies is a question for later posts.
- Replacing the cloud by a classical charge in orbit brings back the collapse of Section 1 instead of explaining the 1.6 ns.
- The Schrödinger equation of the atom alone has no term that couples the atom to light. Whatever triggers the decay is not in the atomic wavefunction.

### A historical marker: Einstein 1917

- Einstein asked how atoms and radiation reach thermal equilibrium, and found that Planck's law requires three processes: absorption, stimulated emission, and an emission that happens with no light present.
- He introduced a coefficient A for this spontaneous emission, the same quantity as our Γ, and a relation between A and the stimulated-emission coefficient B: A/B = 8πhν³/c³. (This holds when B is defined with respect to the spectral energy density per unit frequency; make the convention explicit if the equation is used.)
- His treatment fixes the rate but leaves the moment and direction of each event to chance. He called this a weakness of the theory (quotation and translation to be verified before use).
- It describes the rate, and says nothing about the mechanism.

### What this post does not claim

- It does not explain spontaneous emission, and it does not say that quantum mechanics is incomplete.
- It does not use the quantized electromagnetic field, vacuum fluctuations or the Purcell effect. Those are the content of later posts.
- It states the puzzle precisely: the rate is the antenna rate, but the antenna has nothing to oscillate.

### Closing

- Everything about the rate is classical in form: Γ ∝ ω³d², the same combination that gave the lifetimes and linewidths of Section 3.
- What is missing is what starts the decay of a state with a perfectly static cloud.
- End on this contradiction, with no preview of the answer.

**Closing question:** If an excited atom has a stationary electron cloud, what makes it emit a photon?

---

## Scope boundaries

Not in this post: quantization of the electromagnetic field, vacuum fluctuations, the Purcell effect, radiation reaction as an explanation of spontaneous emission, the DDC split between vacuum fluctuations and radiation reaction, and the Unruh effect. These belong in later posts.

## Done

- Classical Bohr numbers verified in a script: p₀ = 8.48×10⁻³⁰ C·m, ω = 4.13×10¹⁶ rad/s, orbit time 152 as, wavelength 45.6 nm, P = 4.67×10⁻⁸ W (equal to the Larmor value), E/P = 46.7 ps, integrated collapse 15.6 ps (ratio exactly 3).
- Transition dipoles 0.745, 0.298 and 0 a₀ verified numerically. Γ(2p→1s) = 6.27×10⁸ s⁻¹ (1.60 ns, 99.8 MHz) and Γ(3p→1s) = 1.67×10⁸ s⁻¹ (ratio 0.267) computed.
- Lorentz oscillator rate (0.66 ns) and Bohr n = 2 estimate (3.0 ns) computed.
- Figures 1–5 and the feature image exist, with captions and alt text. Animated GIFs of Figures 3–5 and a 3D dot cloud with turntable GIF exist.
- Reviewer feedback incorporated: 3p linewidth, stationary-state wording, radiation-reaction wording, blue-sky qualifier, Section 1 aside, Section 3 progression, ending without preview, Einstein convention, equation budget. The coherent/incoherent discussion was dropped on purpose.

## Open work

- Verify A(3p→2s) ≈ 2.2×10⁷ s⁻¹ and the resulting total 3p lifetime (about 5.3 ns) and linewidth (about 30 MHz) against a source.
- Verify the 2s lifetime (about 0.1 s) and the two-photon decay remark.
- Check the 2p lifetime (1.6 ns) against a source before publication.
- Check the classical collapse derivation and its assumptions (the factor 3 is confirmed numerically, the derivation is not yet written out).
- Decide whether the radiation-reaction picture (kink figure or extended-charge sketch) gets its own figure or stays in the optional aside.
- Locate the precise Griffiths discussion of the electromagnetic self-force.
- Verify Einstein's 1917 quotation, translation and source, and the convention for B, before using them.
- Figures 3–5: print the phase labels (φ = 0, π/2, π, 3π/2) above or below each panel.
- Feature image: add a subtle nucleus marker. The nucleus sits inside the metal surface, so this needs a slightly translucent surface or a small dot on the plane at the centre of each blob. Optional extras: warm and cool tints for the two phases, or a translucent 90%-probability shell.
- Figure 4: keep the common scale for comparison with Figure 3, or add a wider view (about ±10 a₀) as a separate panel.
- Figure 5: optionally add the wide view (±18 a₀) to show where the breathing probability goes.
- Decide the brightness wording for Figure 2 against the final script (partly equalised with GAMMA_NORM = 0.3).
- Optional: embed the GIFs (Figures 3–5 animated) on the website version.
- Write the article section by section.