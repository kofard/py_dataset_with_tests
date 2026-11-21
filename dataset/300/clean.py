"""Semantic version parser, precedence comparison and range matching."""

import re
from functools import total_ordering


_SEMVER = re.compile(
    r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?"
)


@total_ordering
class Version:
    def __init__(self, text: str) -> None:
        if not isinstance(text, str):
            raise TypeError("version must be a string")
        matched = _SEMVER.fullmatch(text)
        if matched is None:
            raise ValueError(f"invalid semantic version: {text!r}")
        self.major, self.minor, self.patch = map(int, matched.group(1, 2, 3))
        self.prerelease = tuple(matched.group(4).split(".")) if matched.group(4) else ()
        self.build = matched.group(5) or ""
        for part in self.prerelease:
            if part.isdigit() and len(part) > 1 and part.startswith("0"):
                raise ValueError("numeric prerelease identifiers may not have leading zeroes")
        self.text = text

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return f"Version({self.text!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return (
            self.major, self.minor, self.patch, self.prerelease
        ) == (
            other.major, other.minor, other.patch, other.prerelease
        )

    def __lt__(self, other: "Version") -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        left = self.major, self.minor, self.patch
        right = other.major, other.minor, other.patch
        if left != right:
            return left < right
        if not self.prerelease:
            return False
        if not other.prerelease:
            return True

        for a, b in zip(self.prerelease, other.prerelease):
            if a == b:
                continue
            a_is_number = a.isdigit()
            b_is_number = b.isdigit()
            if a_is_number and b_is_number:
                return int(a) < int(b)
            if a_is_number != b_is_number:
                return a_is_number
            return a < b
        return len(self.prerelease) < len(other.prerelease)


def _upper_bound(version: Version, operator: str) -> Version:
    """Find the exclusive upper bound for ^ and ~ constraints."""
    if operator == "~":
        return Version(f"{version.major}.{version.minor + 1}.0")
    if version.major > 0:
        return Version(f"{version.major + 1}.0.0")
    if version.minor > 0:
        return Version(f"0.{version.minor + 1}.0")
    return Version(f"0.0.{version.patch + 1}")


def satisfies(version: str | Version, requirements: str) -> bool:
    """Evaluate comma-separated comparators, plus caret and tilde ranges.

    Prereleases follow comparison precedence. This deliberately does not
    implement npm's extra prerelease-exclusion rules.
    """
    candidate = Version(version) if isinstance(version, str) else version
    if not isinstance(candidate, Version) or not isinstance(requirements, str):
        raise TypeError("expected a Version and a requirement string")
    if not requirements.strip():
        return True

    for clause in requirements.split(","):
        clause = clause.strip()
        if not clause:
            raise ValueError("empty version range clause")
        operation = next((op for op in (">=", "<=", "!=", "==", ">", "<", "^", "~")
                          if clause.startswith(op)), "==")
        raw_target = clause[len(operation):].strip() if clause.startswith(operation) else clause
        target = Version(raw_target)

        if operation in ("^", "~"):
            allowed = target <= candidate < _upper_bound(target, operation)
        elif operation == ">=":
            allowed = candidate >= target
        elif operation == "<=":
            allowed = candidate <= target
        elif operation == ">":
            allowed = candidate > target
        elif operation == "<":
            allowed = candidate < target
        elif operation == "!=":
            allowed = candidate != target
        else:
            allowed = candidate == target
        if not allowed:
            return False
    return True
