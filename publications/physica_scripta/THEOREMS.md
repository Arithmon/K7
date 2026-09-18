# Mathematical contracts for the Physica Scripta projection

These statements concern the frozen coordinate model, except where an exact
product hypothesis is explicitly made. A field called CERTIFIED does not
identify that model with a global K3 metric or a torsion-free G2 metric.

## T-METRIC: reconstruction, positivity and determinant

Let c be the exact dyadic interpretation of the frozen binary64 coefficients.
On [0,1], put P_j(s) = sum_{k=0}^5 c_{kj} T_k(2s-1). Extend each P outside
the seam by the exponential function matching its endpoint value and first
derivative, at the frozen positive rate gamma. Form a lower triangular
matrix B from P, replacing diagonal entries by log(1+exp(P_j)).
Its diagonal is strictly positive. Set
t = exp((log(D)/2 - sum_i log B_ii)/7), L=tB and g=LL^t, where D=65/32.
Then g is positive definite and det(g)=D exactly in real arithmetic.

The map is
R^168 -> P_5([0,1];R^28) -> C^1([-2,3];SPD_7).
Only the first arrow has polynomial image. Neither softplus nor the
determinant rescaling preserves polynomial dependence on s.
This is a coordinate metric field; no K3 atlas is constructed.

## T-NK-CONTRACT: what a valid replacement must specify

For a square residual F:X->Y between specified Banach spaces, let
A=DF(c0) be a bounded isomorphism, beta bound ||A^-1||, eta bound ||F(c0)||,
and omega be a Lipschitz constant for DF on a specified coefficient ball.
In the raw convention used in this sentence, the scalar majorant is
beta*eta - t + (beta*omega/2)t^2 and h=beta^2*eta*omega.
Its smaller root is 2*beta*eta/(1+sqrt(1-2*h)).
The theorem also needs the closed ball in the domain and the applicable
existence/uniqueness hypotheses; an arithmetic inequality alone is not NK.

Alternatively bound b=||A^-1 F(c0)|| and the Lipschitz constant K of
A^-1 DF; then h=b*K. These conventions must not be mixed.
See the primary [Newton--Kantorovich presentation](https://reliable-computing.org/dagstuhl.03/from.pdf)
for the preconditioned convention.

A map from R^168 to all of C^0(I;Lambda^4+Lambda^5) is not an isomorphism.
A finite projected problem must supply its gauge, boundary constraints,
projection, inverse bound, and a theorem controlling the unprojected
residual. No such data is supplied by the frozen companions. A scalar
spectral gap is not a singular-value bound for that Jacobian.
The asserted nonlinear relative metric displacement is also not a fixed
norm on coefficient space. No NK theorem for this input is released.

## T-PRODUCT-COHOMOLOGY: diagnostic, not a matching lemma

Assuming the usual real cohomology of K3 and T2, Kunneth convolution of
(1,0,22,0,1) and (1,2,1) gives (1,2,23,44,23,2,1).
The interval factor is contractible. Thus ordinary cohomology of the
bare neck has dimensions 23 and 44 in degrees two and three.
This does not specify absolute/relative/matched harmonic boundary conditions.
To obtain 21 or 77 one must define a different complex and its end maps.
The local fibre dimension binomial(7,3)=35 counts components, not global
closed and co-closed sections.

## T-SCALAR-COMPARISON: certified reduced first eigenvalue

Let a(s)=g^{ss}(s)>0 on [-2,3]. The constant determinant makes the scalar
weight w=sqrt(D) constant, so the Rayleigh quotient is
integral a(s)|u'(s)|^2 ds / integral |u(s)|^2 ds.
Use the natural Neumann realization of -(a u')' with form domain H^1;
the nullspace consists exactly of constants. On the mean-zero subspace,
the interval Poincare inequality gives the lower bound
a_min*pi^2/25. Testing with cos(pi*(s+2)/5), which has zero mean, gives
the upper bound a_max*pi^2/25. Therefore
a_min*pi^2/25 <= lambda_1 <= a_max*pi^2/25.

The producer covers the domain by exact rational closed intervals, split
at both seams. It evaluates P, softplus, determinant scaling, and a
triangular solve in directed interval arithmetic. Since
g^-1=t^-2 B^-t B^-1, a=t^-2 ||B^-1 e_s||^2.
It exports rational endpoints for every interval, their global hull,
pi squared, and outward-rounded final eigenvalue bounds.
The checker repeats coefficient evaluation at higher precision and
checks coverage, positivity, aggregation and all final rational inequalities.

The trusted base is Python integer arithmetic, mpmath interval elementary
functions and this variational argument. This is not a Lean theorem.
It certifies the exact dyadic coordinate input, not an interval family
containing an unknown NK root, and not the global seven-dimensional gap.

## T-SCALAR-METRIC-COMPARISON: conditional adiabatic transfer

Suppose (1-e)g0 <= g <= (1+e)g0 pointwise, 0<=e<1, in dimension d,
with the same scalar form domain and boundary convention. The inverse
metrics satisfy reciprocal bounds and their volume densities lie
between (1-e)^(d/2) and (1+e)^(d/2) times the old density. Bounding each
Rayleigh quotient, then applying min-max, gives factors

- lower: (1-e)^(d/2)/(1+e)^(d/2+1);
- upper: (1+e)^(d/2)/(1-e)^(d/2+1).

These are scalar form comparisons, not a bounded-operator norm assertion
about two unbounded Laplacians. No analogous all-form-degree bound is
released. The required global metric comparison with g* is missing.

## T-PROFILE: the deterministic interpolation problem

For positive p, the solution of -(p f')'=0 with f(-2)=0 and f(3)=1 is
f(s)=integral[-2,s] p^-1 / integral[-2,3] p^-1.
The other profile is 1-f. Chebyshev collocation is checked against
independent piecewise adaptive quadrature. These functions solve a
Dirichlet interpolation problem. Lifting them to global harmonic forms
requires additional equations and matching data; no multiplicity follows.

## T-DEMOCRACY: the precise analytical sector identity

On an exact product B x S1 x F, with constant circle radius, let theta
be the parallel circle one-form. For a scalar f on B,
Delta_1(f theta)=(Delta_0 f)theta. The product Laplacian is a sum of
the factor Laplacians, theta is parallel and harmonic, and all mixed
derivatives vanish. This proves the identity, with corresponding
radial self-adjoint boundary conditions. Ricci-flatness is not needed
for this particular product statement.

This identifies the selected parallel-circle one-form sector with the
scalar sector. It is not equality of whole spectra with multiplicity,
nor a theorem comparing Delta_2 on the nonproduct frozen metric.
The fresh numerical check uses an explicitly stated block projection.

## T-WEYL-CONVENTION

The symbol alpha means the exponent of the counting function N(lambda),
so its dimensional reference is d/2. The inverse index-growth exponent
is named nu. A finite-window fit is a numerical diagnostic, not an
asymptotic theorem; full-tower data is not available in this projection.

## T-KK-EXHAUSTION: open contract

A full product tower needs K3 eigenvalues and multiplicities, torus periods,
and radial eigenvalues, with certified tail lower bounds for every omitted
index. Integer momenta on four coordinate directions are not a K3 spectrum.
If a justified relative eigenvalue error delta<1 is later supplied, the
count satisfies N_red(C/(1+delta)) <= N_full(C) <= N_red(C/(1-delta)).
Neither delta nor the K3 spectrum is presently available.

## T-INTERSECTION: rejected historical recipe

The archived matrix uses two copies of the same first positive K3
directions. Each repeated direction carries the positive definite radial
overlap block [[R11,R12],[R12,R22]] times its prescribed sign. Exact
rational LDL of the archived decimal recipe gives inertia (6,15).
This is not a geometric intersection pairing: basis vectors and a
rank-21 embedding in the K3 lattice are missing.
