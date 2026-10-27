# Atomic Radiation — Mathematical Backbone

**Working reference, version 0.1 (25 October 2026)**  
**Focus:** two-level atom; vacuum fluctuations (VF), radiation reaction (RR), operator ordering, spontaneous emission.  
**Convention:** SI units; $\omega_0>0$; $\dot E$ means rate of change of *atomic* energy (negative for emission). All quoted decay rates are weak-coupling, leading-order rates.  
**Status:** self-contained two-level derivation and consistency checks. General electromagnetic environments and accelerated trajectories are reserved for extensions.

## 0. Source hierarchy and assumptions

Primary: J. Dalibard, J. Dupont-Roc and C. Cohen-Tannoudji, *Vacuum fluctuations and radiation reaction: identification of their respective contributions*, Journal de Physique **43**, 1617–1638 (1982), especially §§3–5, and §5.3 for the energy-exchange rates. Their argument fixes a physically motivated **symmetric ordering** by requiring separately Hermitian rates.

Comparison: P. W. Milonni and W. A. Smith, *Radiation reaction and vacuum fluctuations in spontaneous emission*, Physical Review A **11**, 814–824 (1975), especially §§IV–V: normal ordering can make the explicit vacuum contribution disappear from vacuum-averaged equations; this changes attribution, not total predictions.

Environment: A. Rudavskyi, *Influence of environment on spontaneous emission*, §§2–4, for the mode-density and mirror/cavity applications.

Our derivation specializes DDC's general multilevel analysis to a two-level electric dipole, initially inertial and in the Minkowski vacuum. We assume the electric-dipole approximation, no permanent dipoles, weak coupling, a stationary broadband reservoir, and the long-time/Markov limit for transition *rates*. **We do not impose the rotating-wave approximation before separating VF from RR.** The vacuum field is not treated as a classical stochastic field.

## 1. Atom and dipole

Choose $E_g=0$, $E_e=\hbar\omega_0$, and define

$$
\sigma_+=|e\rangle\langle g|,\quad \sigma_-=|g\rangle\langle e|,\quad
\sigma_z=|e\rangle\langle e|-|g\rangle\langle g|. \tag{A1}
$$

$$
H_A=\frac{\hbar\omega_0}{2}\sigma_z+\text{constant},\qquad
\mathbf d_{ge}=-e\langle g|\mathbf r|e\rangle. \tag{A2}
$$

For a real linearly oriented transition dipole $\mathbf d_{ge}=d\mathbf n$ (unit vector $\mathbf n$), the projected dipole operator is

$$
\mathbf d=d\mathbf n(\sigma_++\sigma_-)=d\mathbf n\sigma_x. \tag{A3}
$$

More general transitions require the Hermitian form $\mathbf d=\mathbf d_{ge}\sigma_-+\mathbf d_{ge}^{*}\sigma_+$, with complex vector matrix elements. The mean dipole of $|e\rangle$ or $|g\rangle$ is zero even though $d$ need not vanish. A coherent superposition can have an oscillating mean dipole; a pure excited eigenstate can nevertheless emit spontaneously.

Free atomic evolution:

$$
\sigma_\pm(t)=\sigma_\pm(0)e^{\pm i\omega_0t},\qquad
\sigma_x(t)=\sigma_+e^{i\omega_0t}+\sigma_-e^{-i\omega_0t}. \tag{A4}
$$

## 2. Quantized field and complete dipole interaction

At the atomic position $\mathbf r_0$,

$$
\mathbf E_0(t)=i\sum_{\mathbf k\lambda}\sqrt{\frac{\hbar\omega_k}{2\epsilon_0V}}\,\mathbf e_{\mathbf k\lambda}
\left[a_{\mathbf k\lambda}e^{i\mathbf k\cdot\mathbf r_0-i\omega_kt}-a_{\mathbf k\lambda}^{\dagger}e^{-i\mathbf k\cdot\mathbf r_0+i\omega_kt}\right]. \tag{A5}
$$

The full electric-dipole interaction, **before RWA**, is

$$
H_I=-\mathbf d\cdot\mathbf E(\mathbf r_0),\qquad H=H_A+H_F+H_I. \tag{A6}
$$

The four products $\sigma_+a$, $\sigma_-a^\dagger$, $\sigma_+a^\dagger$, and $\sigma_-a$ are all retained at this stage. In the interaction picture their frequencies are $\pm(\omega_0-\omega_k)$ and $\pm(\omega_0+\omega_k)$, respectively. **RWA** discards the sum-frequency terms, and is useful for ordinary decay calculations, but should not be silently inserted into the DDC separation.

## 3. The exact energy-rate operator

The atomic energy derivative due to coupling is

$$
\dot H_A(t)=\frac{i}{\hbar}[H_I(t),H_A(t)]
=-\dot{\mathbf d}(t)\cdot\mathbf E(t), \tag{A7}
$$

where $\dot{\mathbf d}$ on the right is the *free atomic* derivative $(i/\hbar)[H_A,\mathbf d]$ evaluated as the corresponding Heisenberg atomic operator. For the real two-level dipole,

$$
\dot{\mathbf d}=i\omega_0d\mathbf n(\sigma_+-\sigma_-). \tag{A8}
$$

The complete atomic and field operators commute at equal times, so $-\dot{\mathbf d}\cdot\mathbf E$ is Hermitian. But after splitting the field, the separate terms need not commute: this is the ordering problem.

## 4. Free field plus source field

Solving the Heisenberg field equation and substituting its solution gives the formal decomposition

$$
\mathbf E(t)=\mathbf E_{\mathrm f}(t)+\mathbf E_{\mathrm s}(t). \tag{A9}
$$

$\mathbf E_{\mathrm f}$ is the homogeneous/free field; $\mathbf E_{\mathrm s}$ is the retarded response to the atomic dipole. The first is an operator even in the vacuum, with $\langle\mathbf E_{\mathrm f}\rangle=0$ but nonzero quadratic correlations. The second is the self/source field responsible for radiation reaction.

The physically motivated DDC prescription uses symmetric products:

$$
\dot H_A\big|_{\rm VF}=-\tfrac12\{\dot{\mathbf d},\mathbf E_{\mathrm f}\},\qquad
\dot H_A\big|_{\rm RR}=-\tfrac12\{\dot{\mathbf d},\mathbf E_{\mathrm s}\}, \tag{A10}
$$

with Cartesian contractions understood. These are **definitions of the separated contributions within the symmetric-ordering scheme**. Their sum reproduces (A7), but they should not be interpreted as two independently measurable pieces of the total decay rate.

## 5. Symmetric correlations versus response functions

For stationary uncoupled subsystems define

$$
C_{AB}(\tau)=\frac12\langle\{A(\tau),B(0)\}\rangle,\qquad
\chi_{AB}(\tau)=\frac{i}{\hbar}\theta(\tau)\langle[A(\tau),B(0)]\rangle. \tag{A11}
$$

The **symmetric correlator** describes fluctuations, whereas the **retarded susceptibility** describes linear response. The DDC weak-coupling expressions for energy shifts and energy-exchange rates are integrals of the field symmetric correlator against the atomic response (VF), and the atomic symmetric correlator against the field response (RR). Time derivatives and indices must be retained in any full derivation; $C_F\chi_A$ and $C_A\chi_F$ are only shorthand for the structure, not literal complete formulas.

For the scalar field component $F=\mathbf n\cdot\mathbf E_{\mathrm f}$, the positive-frequency *unsymmetrized* spectrum is

$$
S_F(\omega)=\int_{-\infty}^{\infty}d\tau\,e^{i\omega\tau}
\langle0|F(\tau)F(0)|0\rangle. \tag{A12}
$$

In free-space vacuum, with this Fourier convention,

$$
S_F(\omega)=\frac{\hbar\omega^3}{3\pi\epsilon_0c^3}\,\Theta(\omega), \tag{A13}
$$

where this expression is for a **single fixed Cartesian/dipole direction** at coincident spatial points, interpreted as a distribution (UV regularization is needed for equal-time quantities). Thus

$$
S_F(+\omega_0)>0,\qquad S_F(-\omega_0)=0. \tag{A14}
$$

The symmetrized spectrum, however, is even:

$$
S_F^{\rm sym}(\omega)=\tfrac12[S_F(\omega)+S_F(-\omega)]
=\frac{\hbar|\omega|^3}{6\pi\epsilon_0c^3}. \tag{A15}
$$

This is the source of the apparent puzzle: the symmetrized vacuum noise has both signs of frequency, while the physically relevant unsymmetrized spectrum is asymmetric. The field commutator/response supplies the complementary antisymmetric part.

## 6. Transition rates: an independent consistency check

For $H_I=-d\sigma_x F$, lowest-order perturbation theory gives

$$
\Gamma_{e\to g}=\frac{d^2}{\hbar^2}S_F(+\omega_0),\qquad
\Gamma_{g\to e}=\frac{d^2}{\hbar^2}S_F(-\omega_0). \tag{A16}
$$

Hence

$$
\boxed{\Gamma_0=\frac{\omega_0^3d^2}{3\pi\epsilon_0\hbar c^3}},\qquad
\Gamma_{g\to e}=0. \tag{A17}
$$

This verifies both the coefficient and the physical emission/absorption asymmetry independently of any VF/RR attribution.

## 7. Explicit two-level DDC split of energy rates

The two-level free atomic dipole correlation is easy to calculate. For an initial atomic eigenstate $|s\rangle$, set $z_s=\langle\sigma_z\rangle_s=+1$ for $e$ and $-1$ for $g$. Then

$$
C_d(\tau)=\frac12\langle\{d\sigma_x(\tau),d\sigma_x(0)\}\rangle_s
=d^2\cos(\omega_0\tau), \tag{A18}
$$

$$
\langle[d\sigma_x(\tau),d\sigma_x(0)]\rangle_s
=2i d^2 z_s\sin(\omega_0\tau). \tag{A19}
$$

Thus the atomic *symmetric* correlation is the same for excited and ground states, while the *atomic response* reverses sign. The vacuum field's symmetric correlation and retarded response do not depend on which atomic state was prepared.

Inserting (A18)–(A19) and the free-space field correlator/response into the DDC symmetric-ordering energy-exchange expressions, performing the long-time resonant frequency integrals, and discarding off-resonant transients gives

$$
\boxed{\left\langle\dot H_A\right\rangle_{\rm VF,s}
=-\frac{\hbar\omega_0\Gamma_0}{2}\,z_s}, \tag{A20}
$$

$$
\boxed{\left\langle\dot H_A\right\rangle_{\rm RR,s}
=-\frac{\hbar\omega_0\Gamma_0}{2}}, \tag{A21}
$$

and therefore

$$
\boxed{\left\langle\dot H_A\right\rangle_s
=-\frac{\hbar\omega_0\Gamma_0}{2}(1+z_s)}. \tag{A22}
$$

| Initial atom | $z_s$ | Vacuum fluctuations | Radiation reaction | Total atomic energy rate |
|:--|--:|--:|--:|--:|
| $|e\rangle$ | $+1$ | $-\hbar\omega_0\Gamma_0/2$ | $-\hbar\omega_0\Gamma_0/2$ | $-\hbar\omega_0\Gamma_0$ |
| $|g\rangle$ | $-1$ | $+\hbar\omega_0\Gamma_0/2$ | $-\hbar\omega_0\Gamma_0/2$ | $0$ |

**Scope of (A20)–(A22):** initial atomic energy eigenstates, vacuum reservoir, weak coupling, long-time rates; they are not universal identities for arbitrary time-dependent atomic states. The DDC paper gives the general multilevel result in §5.3; these equations are its two-level specialization. The displayed intermediate correlation functions show why the VF contribution changes sign and the RR contribution does not. A later expanded appendix can spell out every time integral from DDC's general $C\chi$ formulas.

### Physical interpretation

- For the excited atom, VF and RR **reinforce** each other: both lower the atomic energy.
- For the ground state, VF would **increase** atomic energy while RR would **decrease** it by exactly the same amount: the total is zero.
- The split is an ordering-dependent physical interpretation, not a decomposition into separately observed decay channels.
- In particular, **the vacuum is not a source of usable energy for an inertial ground-state atom**.

## 8. Why normal ordering gives a different story

The full interaction and complete Heisenberg equations are invariant under reordering atomic and field operators that commute at equal times. But the free and source parts individually need not commute with atomic operators. Normal ordering can make vacuum expectation values of explicit free-field terms vanish, making the same radiative effect look entirely like self-reaction; antinormal ordering shifts the attribution in the opposite direction. Milonni–Smith (1975), §§IV–V, demonstrates this explicitly. DDC (1982), §§3–4, motivates symmetric ordering by requiring Hermitian, physically interpretable separated rates. **All schemes must agree on the total** (A22).

## 9. Relation to RWA, Markov and adiabatic approximations

**Electric-dipole approximation:** wavelengths much larger than atomic extent; permits $-\mathbf d\cdot\mathbf E(\mathbf r_0)$.

**Two-level truncation:** retains one resonant atomic transition; good for illustrating spontaneous emission and the DDC split, but not generally accurate for multilevel radiative level shifts (Milonni–Smith §IV explicitly warns about this).

**RWA:** removes $\sigma_+a^\dagger$ and $\sigma_-a$ in a near-resonant weak-coupling description. It gives the correct leading spontaneous-emission rate but is **not** our starting point for the symmetric VF/RR attribution.

**Markov / adiabatic / pole approximation:** approximates slowly evolving atomic quantities inside a short-lived reservoir memory integral; leads to constant rates and exponential decay. These terms have overlapping uses in the literature, but are not automatically identical in every derivation.

**Long-time resonance approximation:** integrals of oscillating phases produce $\delta(\omega-\omega_0)$ for dissipative rates and principal-value terms for level shifts. We keep the dissipative part in (A20)–(A22); level shifts require a separate treatment and regularization.

## 10. Future extensions (not yet derived here)

1. **Near mirrors and in cavities:** replace free-space $S_F$ by the local, orientation-resolved electromagnetic spectrum, equivalently the imaginary part of the dyadic Green tensor. Revisit the VF/RR split with boundaries and distinguish radiative from nonradiative decay.
2. **Accelerated atom:** replace inertial two-time field functions by correlations along the accelerated worldline; carefully distinguish a scalar Unruh–DeWitt detector from a genuine electromagnetic dipole. Derive excitation/de-excitation detailed balance and then the VF/RR contributions, rather than assuming the inertial half-and-half split persists.
3. **Level shifts:** retain principal-value integrals and discuss counter-rotating terms, UV cutoff and renormalization.
4. **Derivation audit:** expand DDC's general §4 response formulas to an explicit two-level time-integral calculation, with every $i$, $2$, $\hbar$, and Fourier sign checked before publication.

## 11. Formula index for articles

- Part 1: (A1)–(A4), transition dipole and coherence.
- Part 2: (A5)–(A6), (A12)–(A17), emission and cavity-dependent spectral density.
- Part 3: (A7)–(A11), (A18)–(A22), ordering, correlations and cancellation.
- Part 4: §10.2, **pending separate derivation**.

## 12. Bibliography

- Dalibard, J., Dupont-Roc, J. & Cohen-Tannoudji, C. (1982). *Vacuum fluctuations and radiation reaction: identification of their respective contributions*. Journal de Physique 43, 1617–1638. DOI: 10.1051/jphys:0198200430110161700.
- Milonni, P. W. & Smith, W. A. (1975). *Radiation reaction and vacuum fluctuations in spontaneous emission*. Physical Review A 11, 814–824.
- Rudavskyi, A. *Influence of environment on spontaneous emission*, supplied reference PDF.
