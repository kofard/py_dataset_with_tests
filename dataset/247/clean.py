"""
Implementation of SHA256 Hash function in a Python class and provides utilities
to find hash of string or hash of text from a file.

Usage: python sha256.py --string "Hello World!!"
       python sha256.py --file "hello_world.txt"
       When run without any arguments,
       it prints the hash of the string "Hello World!! Welcome to Cryptography"

References:
https://qvault.io/cryptography/how-sha-2-works-step-by-step-sha-256/
https://en.wikipedia.org/wiki/SHA-2
"""
import argparse
import struct
import unittest

class SHA256:
    """Class to contain the entire pipeline for SHA1 Hashing Algorithm"""

    def __init__(self, data: bytes) -> None:
        self.data = data
        self.hashes = [1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225]
        self.round_constants = [1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298]
        self.preprocessed_data = self.preprocessing(self.data)
        self.final_hash()

    @staticmethod
    def preprocessing(data: bytes) -> bytes:
        padding = b'\x80' + b'\x00' * (63 - (len(data) + 8) % 64)
        big_endian_integer = struct.pack('>Q', len(data) * 8)
        return data + padding + big_endian_integer

    def final_hash(self) -> None:
        self.blocks = [self.preprocessed_data[x:x + 64] for x in range(0, len(self.preprocessed_data), 64)]
        for block in self.blocks:
            words = list(struct.unpack('>16L', block))
            words += [0] * 48
            a, b, c, d, e, f, g, h = self.hashes
            for index in range(64):
                if index > 15:
                    s0 = self.ror(words[index - 15], 7) ^ self.ror(words[index - 15], 18) ^ words[index - 15] >> 3
                    s1 = self.ror(words[index - 2], 17) ^ self.ror(words[index - 2], 19) ^ words[index - 2] >> 10
                    words[index] = (words[index - 16] + s0 + words[index - 7] + s1) % 4294967296
                s1 = self.ror(e, 6) ^ self.ror(e, 11) ^ self.ror(e, 25)
                ch = e & f ^ ~e & 4294967295 & g
                temp1 = (h + s1 + ch + self.round_constants[index] + words[index]) % 4294967296
                s0 = self.ror(a, 2) ^ self.ror(a, 13) ^ self.ror(a, 22)
                maj = a & b ^ a & c ^ b & c
                temp2 = (s0 + maj) % 4294967296
                h, g, f, e, d, c, b, a = (g, f, e, (d + temp1) % 4294967296, c, b, a, (temp1 + temp2) % 4294967296)
            mutated_hash_values = [a, b, c, d, e, f, g, h]
            self.hashes = [(element + mutated_hash_values[index]) % 4294967296 for index, element in enumerate(self.hashes)]
        self.hash = ''.join([hex(value)[2:].zfill(8) for value in self.hashes])

    def ror(self, value: int, rotations: int) -> int:
        """
        Right rotate a given unsigned number by a certain amount of rotations
        """
        return 4294967295 & value << 32 - rotations | value >> rotations

class SHA256HashTest(unittest.TestCase):
    """
    Test class for the SHA256 class. Inherits the TestCase class from unittest
    """

    def test_match_hashes(self) -> None:
        import hashlib
        msg = bytes('Test String', 'utf-8')
        assert SHA256(msg).hash == hashlib.sha256(msg).hexdigest()

def main() -> None:
    """
    Provides option 'string' or 'file' to take input
    and prints the calculated SHA-256 hash
    """
    import doctest
    doctest.testmod()
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--string', dest='input_string', default='Hello World!! Welcome to Cryptography', help='Hash the string')
    parser.add_argument('-f', '--file', dest='input_file', help='Hash contents of a file')
    args = parser.parse_args()
    input_string = args.input_string
    if args.input_file:
        with open(args.input_file, 'rb') as f:
            hash_input = f.read()
    else:
        hash_input = bytes(input_string, 'utf-8')
    print(SHA256(hash_input).hash)