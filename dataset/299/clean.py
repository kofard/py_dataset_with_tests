"""Deterministic Bloom filter with serialization and set operations."""

import hashlib
import math


class BloomFilter:
    def __init__(self, bit_count: int, hash_count: int = 4) -> None:
        if (not isinstance(bit_count, int) or isinstance(bit_count, bool)
                or not isinstance(hash_count, int) or isinstance(hash_count, bool)
                or bit_count <= 0 or hash_count <= 0):
            raise ValueError("bit_count and hash_count must be positive integers")
        self.bit_count = bit_count
        self.hash_count = hash_count
        self.inserts = 0
        self._bits = bytearray((bit_count + 7) // 8)

    @staticmethod
    def _encode(value: str | bytes) -> bytes:
        if isinstance(value, str):
            return b"s" + value.encode("utf-8")
        if isinstance(value, bytes):
            return b"b" + value
        raise TypeError("Bloom filter values must be str or bytes")

    def _indexes(self, value: str | bytes):
        digest = hashlib.sha256(self._encode(value)).digest()
        first = int.from_bytes(digest[:16], "big")
        second = int.from_bytes(digest[16:], "big") | 1
        for step in range(self.hash_count):
            yield (first + step * second + step * step) % self.bit_count

    def add(self, value: str | bytes) -> None:
        for index in self._indexes(value):
            self._bits[index // 8] |= 1 << (index % 8)
        self.inserts += 1

    def might_contain(self, value: str | bytes) -> bool:
        """False guarantees absence; True means possible membership."""
        return all(self._bits[index // 8] & (1 << (index % 8))
                   for index in self._indexes(value))

    def _ensure_compatible(self, other: "BloomFilter") -> None:
        if not isinstance(other, BloomFilter) or (
            self.bit_count, self.hash_count
        ) != (other.bit_count, other.hash_count):
            raise ValueError("Bloom filters have incompatible parameters")

    def union(self, other: "BloomFilter") -> "BloomFilter":
        self._ensure_compatible(other)
        combined = BloomFilter(self.bit_count, self.hash_count)
        combined._bits = bytearray(a | b for a, b in zip(self._bits, other._bits))
        combined.inserts = self.inserts + other.inserts
        return combined

    def intersection(self, other: "BloomFilter") -> "BloomFilter":
        self._ensure_compatible(other)
        combined = BloomFilter(self.bit_count, self.hash_count)
        combined._bits = bytearray(a & b for a, b in zip(self._bits, other._bits))
        # The intersection's true cardinality cannot be deduced from bitsets.
        combined.inserts = min(self.inserts, other.inserts)
        return combined

    def expected_false_positive_rate(self) -> float:
        return (1 - math.exp(-self.hash_count * self.inserts / self.bit_count)) ** self.hash_count

    def to_bytes(self) -> bytes:
        return bytes(self._bits)

    @classmethod
    def from_bytes(cls, bit_count: int, hash_count: int, payload: bytes) -> "BloomFilter":
        result = cls(bit_count, hash_count)
        if not isinstance(payload, bytes) or len(payload) != len(result._bits):
            raise ValueError("invalid Bloom filter payload length")
        result._bits[:] = payload
        return result
