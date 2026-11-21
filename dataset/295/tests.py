import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})


def test_solution():
    codec = LZWCodec()
    samples = [b"", b"A", b"AAAAAA", b"ABABABABABABA", b"TOBEORNOTTOBEORTOBEORNOT", bytes(range(256))]
    for source in samples:
        codes = codec.compress(source)
        assert codec.decompress(codes) == source
        assert codec.unpack(codec.pack(codes)) == codes
        assert codec.decompress(codec.unpack(codec.pack(codes))) == source

    assert codec.compress(b"") == []
    assert codec.decompress([]) == b""
    assert codec.compress(b"AB") == [65, 66]
    assert codec.decompress([65, 66]) == b"AB"
    assert any(code >= 256 for code in codec.compress(b"AAAAAAA"))

    small = LZWCodec(257)
    sample = bytes(range(40)) * 10
    assert small.decompress(small.compress(sample)) == sample
    assert LZWCodec(65536).decompress(LZWCodec(65536).compress(sample)) == sample

    for invalid in (0, 256, 65537):
        try:
            LZWCodec(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid code limit was accepted")

    for invalid_codes in ([256], [65, 300], [65, -1], [65, 999999]):
        try:
            codec.decompress(invalid_codes)
        except ValueError:
            pass
        else:
            raise AssertionError("bad LZW stream was accepted")
    try:
        codec.unpack(b"a")
    except ValueError:
        pass
    else:
        raise AssertionError("odd-length stream was accepted")
