# Light Beams — From atomic stability to the Unruh effect

> Revised story architecture, 26 October 2026. Working titles and subtitles, not final editorial decisions. Four posts recommended; the Unruh material could be a shorter epilogue to Post 3, but a separate Post 4 is cleaner.

## Overall narrative

1. Classical atoms radiate and collapse. Quantum stationary states fix stability but leave spontaneous emission unexplained.
2. Quantizing the electromagnetic field provides spontaneous emission, and the Purcell effect shows that the environment controls its rate. But why no spontaneous absorption?
3. Radiation reaction and vacuum fluctuations, treated with care over operator ordering, explain the asymmetry between excited and ground states.
4. Acceleration changes the detector's response to the same Minkowski vacuum, leading to Unruh physics and a bridge to Analog Gravity Post 3.

## Post 1 — Why Doesn't an Atom Radiate Away Its Energy?

**Subtitle:** Classical physics predicts that atoms should radiate. Quantum mechanics makes them stable—but creates a new mystery: why do excited atoms emit light?

**Key message:** Quantizing the atom gives stationary states without an oscillating mean dipole, but an isolated excited eigenstate does not spontaneously decay. We still need a mechanism.

**Arc:**
- An orbiting classical electron accelerates, radiates, loses energy, and would spiral into the nucleus.
- Quantum mechanics replaces classical orbits with stationary energy eigenstates: no time-dependent charge distribution or mean dipole in an energy eigenstate.
- A coherent superposition of energy eigenstates can have an oscillating transition dipole, from interference of amplitudes: this recovers the classical picture of a radiating dipole in a suitable regime.
- But a pure excited atomic eigenstate has no such oscillating mean dipole and is stationary in the isolated-atom Hamiltonian.
- Real excited atoms decay spontaneously. Atomic quantization alone has not explained why.

**End question:** What makes an atom emit light without an oscillating dipole or incoming light?

## Post 2 — Can Empty Space Make an Atom Emit Light?

**Subtitle:** The quantum vacuum provides the missing interaction—and mirrors and cavities let us change how quickly atoms decay.

**Key message:** Coupling a quantum atom to the quantized electromagnetic field permits spontaneous emission from the vacuum, and the rate depends on electromagnetic mode structure and local coupling.

**Arc:**
- Quantize the field as harmonic oscillator modes; introduce creation and annihilation operators and the vacuum state.
- Atom–field coupling allows |e,0⟩ → |g,1⟩. The creation-operator matrix element gives the familiar √(n+1), and the emission rate contains n+1, nonzero at n=0.
- Fermi's golden rule connects the decay rate to field-mode density and dipole coupling.
- Purcell effect: changing electromagnetic boundaries changes the rate, not merely the direction of emitted light.
- Mirror: Drexhage distance-dependent lifetimes; explain classical reflected-dipole interference as a useful parallel calculation, and the quantum interpretation through field modes/Green functions.
- Cavity: enhancement or suppression depending on resonance, position, orientation, and available modes.
- Confront the problem with the simplistic picture of vacuum as symmetric random noise: why should such fluctuations cause emission but not absorption?

**End question:** Why does an excited atom decay into the vacuum while a ground-state atom does not continually absorb energy from it?

## Post 3 — Why Doesn't the Quantum Vacuum Excite Every Atom?

**Subtitle:** Vacuum fluctuations, radiation reaction, and the delicate balance that makes atomic ground states stable.

**Key message:** A full description includes both free-field vacuum fluctuations and electromagnetic self-reaction. In the DDC symmetric-ordering convention, their contributions to the atomic energy-change rate reinforce for an excited two-level atom and cancel for a ground-state atom.

**Arc:**
- Begin with Post 2's paradox: a classical fluctuating field would generally drive both upward and downward transitions.
- Introduce self-reaction: the atom perturbs the field, which acts back on the atom. Write E = E_free + E_source.
- Explain the historical interpretive dispute: Milonni and Smith demonstrate that apparent attributions depend on operator ordering; different conventions give the same total physics.
- Explain DDC's motivation for symmetric ordering: separately Hermitian contributions to rates of change of atomic observables, enabling an interpretable division.
- Use a two-level atom as the transparent example. In this convention, vacuum fluctuations contribute equal upward/downward tendencies; self-reaction contributes energy loss in either state. Excited state: the downward contributions add. Ground state: upward vacuum-fluctuation contribution cancels downward self-reaction contribution.
- Be explicit that these are contributions to mean atomic energy change, not directly separately measurable photon streams. The total prediction is independent of the ordering convention.
- Distinguish ground-state stability from the separate question of a far-field radiation flux.

**End question:** If an inertial atom's ground state is protected by this balance, what happens when the atom accelerates?

## Post 4 — Can Acceleration Make an Atom Absorb Energy from Empty Space?

**Subtitle:** An accelerated atom responds to the quantum vacuum differently—and leads us to the Unruh effect.

**Key message:** A uniformly accelerated detector can undergo upward transitions in the Minkowski vacuum, with a thermal response characterized by T_U = ħa/(2π c k_B). This is not automatically equivalent to a net radiated energy flux detected far away.

**Arc:**
- Keep the Minkowski vacuum and the atom's internal structure, but change its trajectory to uniform acceleration.
- Ask whether the ground-state cancellation of Post 3 persists. In the accelerated-detector calculation the net excitation rate can be nonzero.
- Show that the field correlations along the accelerated trajectory obey a thermal detailed-balance relation, with Unruh temperature T_U = ħa/(2π c k_B).
- Connect to the mode decomposition, positive/negative-frequency mixing and Bogoliubov coefficients in Analog Gravity Post 3.
- Distinguish detector excitation (local response) from radiation measured at a distant receiver. The latter is subtler and involves source–vacuum interference, energy balance, and detector-model/dimensionality assumptions.
- Close with the theme: the vacuum is not a literal gas of photons; the response depends on the system and its motion.

## Editorial decision: three or four posts?

**Recommendation: four.** Post 3 already needs the ordering ambiguity, DDC's symmetric prescription, and the excited-versus-ground-state balance. Adding a rigorous accelerated-atom treatment risks overwhelming its central resolution. Post 3 can end with the acceleration question; Post 4 then has a strong independent hook and naturally connects to the Analog Gravity series.

**Three-post alternative:** Keep Posts 1 and 2 unchanged; make acceleration and the Unruh temperature a short final section of Post 3, explicitly presented as a teaser rather than a derivation. Link to Analog Gravity Post 3 for the details.

## Physics guardrails

- A superposition can have an oscillating *mean* dipole, but a vanishing mean dipole does not imply the absence of all quantum radiation processes once the field is coupled.
- Do not claim vacuum fluctuations *alone* are the uniquely identifiable cause of spontaneous emission. The full atom–field coupling is fundamental; attribution to vacuum fluctuations and self-reaction is convention-sensitive.
- The DDC reinforcement/cancellation picture is a result of a specified symmetric ordering and an appropriate weak-coupling two-level model.
- Purcell modification of the electromagnetic environment and Unruh modification of a detector's trajectory are related through field correlations but are physically different mechanisms.
- Detector excitation and net emitted radiation at a distant observation point are distinct observables.

## Primary background readings supplied

- Milonni and Smith (1975), *Radiation reaction and vacuum fluctuations in spontaneous emission*.
- Dalibard, Dupont-Roc and Cohen-Tannoudji (1982), *Vacuum fluctuations and radiation reaction: identification of their respective contributions*.
- Rudavskyi, *Influence of environment on spontaneous emission* (mirror, cavity, LDOS, Purcell effect).
- Audretsch and collaborators, accelerated-atom vacuum-fluctuation/self-reaction analysis.
- Bei-Lok Hu / Hsiang, *Quantum Radiation from an Atom Interacting with a Quantum Field* (distinction between detector response, quantum radiation, interference and net flux).
