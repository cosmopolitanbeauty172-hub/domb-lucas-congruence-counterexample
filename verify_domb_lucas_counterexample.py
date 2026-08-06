#!/usr/bin/env python3
"""Verify the p=3 counterexample to arXiv:2607.07638v3, Conjecture 4.1(i).

Only the definitions printed in the paper are used.  Domb numbers are
recomputed from their binomial sum, not copied from the paper's value table.
"""

from math import comb


def require(condition: bool, message: str) -> None:
    """Keep every verification active even when Python optimization is enabled."""
    if not condition:
        raise AssertionError(message)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % divisor for divisor in range(2, int(n**0.5) + 1))


def domb(n: int) -> int:
    return sum(
        comb(n, k) ** 2 * comb(2 * k, k) * comb(2 * (n - k), n - k)
        for k in range(n + 1)
    )


def lucas_u(through: int) -> list[int]:
    values = [0, 1]
    while len(values) <= through:
        values.append(11 * values[-1] - values[-2])
    return values[: through + 1]


def legendre_symbol(a: int, odd_prime: int) -> int:
    residue = a % odd_prime
    if residue == 0:
        return 0
    euler = pow(residue, (odd_prime - 1) // 2, odd_prime)
    if euler == 1:
        return 1
    if euler == odd_prime - 1:
        return -1
    raise AssertionError("denominator is not an odd prime")


def main() -> None:
    p = 3
    require(is_prime(p) and p % 2 == 1, "p must be an odd prime")

    d = [domb(k) for k in range(p)]
    u = lucas_u(p - 1)
    symbol_p_over_3 = legendre_symbol(p, 3)
    symbol_p_over_13 = legendre_symbol(p, 13)
    total = sum(d[k] * u[k] for k in range(p))
    residue = total % (p * p)

    # Scope check: one of the two symbols is 1, exactly as required by
    # Conjecture 4.1(i).  The square 4^2 = 16 = 3 (mod 13) is an even more
    # elementary certificate for the second equality.
    require(symbol_p_over_3 == 0, "(3/3) must equal 0")
    require(symbol_p_over_13 == 1, "(3/13) must equal 1")
    require((4 * 4) % 13 == p, "4^2 must certify that 3 is a square mod 13")

    require(d == [1, 4, 28], "Domb values disagree with the defining sum")
    require(u == [0, 1, 11], "Lucas values disagree with the recurrence")
    require(total == 312, "weighted sum must equal 312")
    require(residue == 6, "312 mod 9 must equal 6")
    require(residue != 0, "the conjectured congruence unexpectedly holds")

    print("arXiv:2607.07638v3, Conjecture 4.1(i)")
    print(f"p={p} is an odd prime")
    print(f"(p/3)={symbol_p_over_3}; (p/13)={symbol_p_over_13}")
    print("scope witness: 4^2 = 3 (mod 13), so (3/13)=1")
    print(f"D(0..2)={d}")
    print(f"u(0..2)={u}")
    print(f"sum(D(k)*u_k, k=0..2)={total}")
    print(f"{total} mod {p*p} = {residue} != 0")
    print("VERIFIED: p=3 contradicts the claimed congruence modulo p^2.")


if __name__ == "__main__":
    main()
