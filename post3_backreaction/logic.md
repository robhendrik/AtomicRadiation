## without field, just the atom
- Energy eigenstates stable in time d/dt = ih_bar omega ... for e and g
- If in superposition we get a dipole, that oscillated at delta omega, but is 'stable' in teh oscillation since there is no field... 

## now add a classical field, not yet quantum
- If atom in eigenstate nothing happens, field and atom nicely coexist
- If atom in superposition what happensdepends on the phase, for in-phase atom absorbs, and for out of pahse atim emits (or vice versa, I do not know)
- in this constant field atom absorbes/emits until dipole disappears and then stable again.

## How is a dipole created in an atom?
1. Spontaneous dues to quantum flucs.. descripe <p> = 0, <p2> = ...
2. Due to a field via susceptibility ... chi
==> Once created, there is a 'memory' form the correlation function, relating <p(t)> to p(t+tau) ...? How does this relate to (anti)commutators?

# How is a field created?
1. Spontaneous due to vac flucs... <a> ... (is the the same as <p> in the rght units?)
2. Due to a dipole via susceptibility ... chi (is this the same chi)
==> Once created, there is a 'memory' form the correlation function, relating <a(t)> to a(t+tau) ...? How does this relate to (anti)commutators?

Now, at t = t0 all is in peace. Then two things can happen

1. a spont dipole creates a field (via susceptilbiity), and at t = t0+tau via both correlations that field and dipole interact to change the energy of the atom
2. a spont field creates a dipole (via susceptibility) and at t = t0+tau via both correlations that field and dipole interact to change the energy of the atom
==> we evealue this for the field in ground state (vacuum, 0 photons) and the atom in e or g, we only look at hw the energy depends on the time for short time (the  onset) 


Trigger(t')  ---> Trigger(t)
    |
    |
Effect(t') ---> Effect(t)   ==> Integrate over history t'

<Trigger(t) x Effect(t)> = <int_t' from t0 to t (trigger(t')xcorre(t,t') x trigger(t')xsuscept((t,t')))>
= <trigger^2> int_t' from t0 to t (corre(t,t') x suscept((t,t')))

==> <Trigger(t) d/dt Effect(t)> <trigger^2> int_t' from t0 to t (corre(t,t') x d/dt suscept((t,t')))


# units

| Quantity | Meaning | SI units |
|---|---|---|
| $C_E$ | Field fluctuations | $(\mathrm{V/m})^2$ |
| $C_d$ | Dipole fluctuations | $(\mathrm{C\,m})^2$ |
| $\chi_d(t,t')$ | Atomic response to electric field | $\mathrm{C\,m^2/(V\,s)}$ |
| $\chi_E(t,t')$ | Electric-field response to dipole | $\mathrm{V/(C\,m^2\,s)}$ |
| $\partial_t\chi_d$ | Dipole-velocity response | $\mathrm{C\,m^2/(V\,s^2)}$ |
| $\partial_t C_d$ | Rate of dipole correlation | $\mathrm{C^2\,m^2/s}$ |
| $\langle\dot H_A\rangle$ | Atomic energy transfer rate | $\mathrm{J/s}$ |



## Quantum Correlation and Susceptibility

Consider a quantum system with Hermitian observable $A(t)$, in a state described by density matrix $\rho$.

Expectation values are defined by

$$
\langle A(t)\rangle = \operatorname{Tr}[\rho A(t)].
$$

### 1. Correlation Function — Anticommutator

The symmetrized, connected correlation function is

$$
\boxed{
C_A(t,t') =
\frac{1}{2}
\left\langle
\{\delta A(t),\delta A(t')\}
\right\rangle
}
$$

where

$$
\delta A(t)=A(t)-\langle A(t)\rangle
$$

and $\{A,B\}=AB+BA$ is the anticommutator.

- Describes spontaneous fluctuations and their temporal correlations.
- At equal times: $C_A(t,t)=\langle(\delta A)^2\rangle$, the variance.
- Has units $[A]^2$.
- Is real for Hermitian observables.
- Other operator orderings define different quantum correlation functions.

### 2. Linear Susceptibility — Commutator

Suppose a weak external perturbation couples through

$$
H_{\mathrm{int}}(t)=-f(t)A.
$$

The induced change in the expectation value is

$$
\delta\langle A(t)\rangle
=
\int_{-\infty}^{t}dt'\,
\chi_A^{\mathrm{ret}}(t,t')f(t').
$$

The Kubo formula gives

$$
\boxed{
\chi_A^{\mathrm{ret}}(t,t')
=
\frac{i}{\hbar}\Theta(t-t')
\left\langle[A(t),A(t')]\right\rangle
}
$$

where $[A,B]=AB-BA$ is the commutator.

- Describes the causal response to a weak external disturbance.
- $\Theta(t-t')$ ensures that only past disturbances affect the present.
- Has units $[A]^2/(\mathrm{J\,s})$ when $fA$ has units of energy.
- Unlike correlation, susceptibility describes an intervention rather than an undisturbed fluctuation.

### 3. Audretsch / DDC Notation

Audretsch defines the following quantities without the conventional Kubo normalization:

$$
C_A^{\mathrm{DDC}}(t,t')
=
\frac12\langle\{A(t),A(t')\}\rangle
$$

$$
\chi_A^{\mathrm{DDC}}(t,t')
=
\frac12\langle[A(t),A(t')]\rangle.
$$

For zero-mean observables, $C_A^{\mathrm{DDC}}$ equals the connected correlation function.

The physical retarded susceptibility is related by

$$
\boxed{
\chi_A^{\mathrm{ret}}(t,t')
=
\frac{2i}{\hbar}
\Theta(t-t')\chi_A^{\mathrm{DDC}}(t,t')
}
$$

Thus, Audretsch's $\chi_A^{\mathrm{DDC}}$ is a half-commutator, not yet the SI-normalized causal response function.

### 4. Application to Atom–Field Interaction

For $H_{\mathrm{int}}=-dE$, the two contributions to atomic energy transfer have the structures

**Vacuum fluctuations — field fluctuates, atom responds:**

$$
\langle\dot H_A(t)\rangle_{\mathrm{vf}}
\sim
\int_{t_0}^{t}dt'\,
C_E(t,t')\,
\partial_t\chi_d^{\mathrm{ret}}(t,t').
$$

**Radiation reaction — atom fluctuates, field responds:**

$$
\langle\dot H_A(t)\rangle_{\mathrm{rr}}
\sim
\int_{t_0}^{t}dt'\,
\chi_E^{\mathrm{ret}}(t,t')\,
\partial_t C_d(t,t').
$$

The proportionality notation suppresses overall signs and coupling conventions.

**Physical interpretation:**

A fluctuation at an earlier time creates a response that persists until the present. Because the present value is correlated with the earlier fluctuation, the average work need not vanish even when both mean quantities are zero.

Correlation describes the undisturbed history; susceptibility describes the response to an intervention.
