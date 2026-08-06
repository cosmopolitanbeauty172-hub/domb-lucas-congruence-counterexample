# A counterexample to arXiv:2607.07638v3, Conjecture 4.1(i)

This repository gives a small, independently reproducible counterexample to
Conjecture 4.1(i) **as printed in version 3** of Zhi-Wei Sun,
*A new kind of numbers and related congruences*.

- arXiv record and version history: <https://arxiv.org/abs/2607.07638>
- Version-3 HTML containing the definitions and Conjecture 4.1:
  <https://arxiv.org/html/2607.07638v3>

The source was checked on 2026-08-07. The arXiv record then listed v3, revised
on 2026-07-21, as the current version.

## The printed claim

The paper defines the Domb numbers by

```text
D(n) = sum from k=0 to n of
       binom(n,k)^2 binom(2k,k) binom(2(n-k),n-k)
```

and the Lucas sequence used in the conjecture by

```text
u_0 = 0,  u_1 = 1,  u_(n+1) = 11u_n - u_(n-1).
```

Conjecture 4.1 first says, "Let `p` be an odd prime." Part (i) then says that
if either Legendre symbol `(p/3)` or `(p/13)` is `1`, then

```text
sum from k=0 to p-1 of D(k)u_k = 0 (mod p^2).
```

## Counterexample: p = 3

The number `3` is an odd prime. Its two relevant Legendre symbols are

```text
(3/3) = 0,  (3/13) = 1.
```

The second equality has the elementary certificate
`4^2 = 16 = 3 (mod 13)`. Thus `p=3` satisfies the printed hypothesis: one of
the two symbols is `1`.

Computing directly from the definitions gives

```text
D(0), D(1), D(2) = 1, 4, 28,
u_0,  u_1,  u_2  = 0, 1, 11.
```

Therefore

```text
sum from k=0 to 2 of D(k)u_k
  = 1*0 + 4*1 + 28*11
  = 312,

312 mod 3^2 = 312 mod 9 = 6 != 0.
```

This contradicts the residue `0 mod p^2` asserted in Conjecture 4.1(i).

## Reproduce

Requirements: Python 3.10 or later. No third-party packages are used.

Run both verification modes from the repository root:

```console
python -I verify_domb_lucas_counterexample.py
python -OO -I verify_domb_lucas_counterexample.py
```

Each command exits with status 0 and ends with

```text
VERIFIED: p=3 contradicts the claimed congruence modulo p^2.
```

The verifier independently:

1. checks that `p=3` is an odd prime;
2. evaluates both Legendre symbols with Euler's criterion and separately
   checks the elementary square certificate modulo 13;
3. recomputes every required Domb number from the printed binomial sum;
4. generates the Lucas values from the printed recurrence; and
5. checks the exact integer sum and its nonzero residue modulo 9.

Its checks use explicit failure conditions rather than Python `assert`, so
they remain active under `python -OO`. GitHub Actions runs both commands on
every push.

## Scope and caveat

This repository makes only the narrow claim supported by the finite
certificate: Conjecture 4.1(i) as actually printed in arXiv:2607.07638v3 is
false at `p=3`. A likely repair is to exclude this small prime, for example by
requiring `p>3`. This repository does not claim to refute that repaired
statement, any other intended formulation, or other claims in the paper.

The paper is a recent preprint. No author response or external peer review of
this counterexample is claimed here.

## License

The verification code and exposition in this repository are released under
the MIT License. The linked paper remains under its own license.
