"""LZW compression of byte strings with a bounded dictionary."""


class LZWCodec:
    def __init__(self, maximum_codes: int = 4096) -> None:
        if not isinstance(maximum_codes, int) or isinstance(maximum_codes, bool):
            raise TypeError("maximum_codes must be an integer")
        if not 257 <= maximum_codes <= 65536:
            raise ValueError("maximum_codes must lie in [257, 65536]")
        self.maximum_codes = maximum_codes

    @staticmethod
    def _check_data(data: bytes) -> bytes:
        if not isinstance(data, bytes):
            raise TypeError("expected a byte string")
        return data

    def compress(self, data: bytes) -> list[int]:
        source = self._check_data(data)
        if not source:
            return []

        dictionary = {bytes((value,)): value for value in range(256)}
        next_code = 256
        buffer = bytes((source[0],))
        result: list[int] = []

        for value in source[1:]:
            extended = buffer + bytes((value,))
            if extended in dictionary:
                buffer = extended
                continue
            result.append(dictionary[buffer])
            if next_code < self.maximum_codes:
                dictionary[extended] = next_code
                next_code += 1
            buffer = bytes((value,))

        result.append(dictionary[buffer])
        return result

    def decompress(self, codes: list[int]) -> bytes:
        if not isinstance(codes, (list, tuple)):
            raise TypeError("codes must be a list or tuple")
        if not codes:
            return b""
        if any(not isinstance(code, int) or isinstance(code, bool) for code in codes):
            raise TypeError("all codes must be integers")
        if not 0 <= codes[0] < 256:
            raise ValueError("invalid initial LZW code")

        dictionary = {number: bytes((number,)) for number in range(256)}
        next_code = 256
        previous = dictionary[codes[0]]
        result = bytearray(previous)

        for code in codes[1:]:
            if code in dictionary:
                entry = dictionary[code]
            elif code == next_code and next_code < self.maximum_codes:
                entry = previous + previous[:1]
            else:
                raise ValueError(f"invalid LZW code: {code}")

            result.extend(entry)
            if next_code < self.maximum_codes:
                dictionary[next_code] = previous + entry[:1]
                next_code += 1
            previous = entry
        return bytes(result)

    def pack(self, codes: list[int]) -> bytes:
        """Store codes as unsigned two-byte big-endian integers."""
        if any(not isinstance(code, int) or isinstance(code, bool)
               or not 0 <= code < self.maximum_codes for code in codes):
            raise ValueError("code is outside the configured dictionary")
        return b"".join(code.to_bytes(2, "big") for code in codes)

    def unpack(self, data: bytes) -> list[int]:
        payload = self._check_data(data)
        if len(payload) % 2:
            raise ValueError("packed code stream must have an even byte count")
        codes = [int.from_bytes(payload[index:index + 2], "big")
                 for index in range(0, len(payload), 2)]
        if any(code >= self.maximum_codes for code in codes):
            raise ValueError("code exceeds the maximum dictionary size")
        return codes
