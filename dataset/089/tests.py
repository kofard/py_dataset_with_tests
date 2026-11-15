import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert swap_endianness_16(0x1234) == 13330
    assert hex(swap_endianness_16(0x1234)) == '0x3412'
    assert swap_endianness_16(0xABCD) == 52651
    assert hex(swap_endianness_16(0xABCD)) == '0xcdab'
    assert swap_endianness_16(0) == 0
    assert swap_endianness_16(0xFFFF) == 65535
    assert swap_endianness_32(0x12345678) == 2018915346
    assert hex(swap_endianness_32(0x12345678)) == '0x78563412'
    assert swap_endianness_32(0xDEADBEEF) == 4022250974
    assert hex(swap_endianness_32(0xDEADBEEF)) == '0xefbeadde'
    assert swap_endianness_32(0) == 0
    assert swap_endianness_32(0xFFFFFFFF) == 4294967295
    assert swap_endianness_32(0x01020304) == 67305985
    assert swap_endianness_64(0x0123456789ABCDEF) == 17279655951921914625
    assert hex(swap_endianness_64(0x0123456789ABCDEF)) == '0xefcdab8967452301'
    assert swap_endianness_64(0xFEDCBA9876543210) == 1167088121787636990
    assert hex(swap_endianness_64(0xFEDCBA9876543210)) == '0x1032547698badcfe'
    assert swap_endianness_64(0) == 0
    assert swap_endianness_64(0xFFFFFFFFFFFFFFFF) == 18446744073709551615
    assert bytes_to_int_little(b'\x78\x56\x34\x12') == 305419896
    assert hex(bytes_to_int_little(b'\x78\x56\x34\x12')) == '0x12345678'
    assert bytes_to_int_little(b'\x01\x02') == 513
    assert bytes_to_int_little(b'\xff') == 255
    assert bytes_to_int_little(b'\x00\x00\x00\x01') == 16777216
    assert bytes_to_int_big(b'\x12\x34\x56\x78') == 305419896
    assert hex(bytes_to_int_big(b'\x12\x34\x56\x78')) == '0x12345678'
    assert bytes_to_int_big(b'\x01\x02') == 258
    assert bytes_to_int_big(b'\xff') == 255
    assert bytes_to_int_big(b'\x00\x00\x00\x01') == 1
    assert int_to_bytes_little(0x12345678, 4) == b'xV4\x12'
    assert int_to_bytes_little(513, 2) == b'\x01\x02'
    assert int_to_bytes_little(255, 1) == b'\xff'
    assert int_to_bytes_little(16777216, 4) == b'\x00\x00\x00\x01'
    assert int_to_bytes_big(0x12345678, 4) == b'\x124Vx'
    assert int_to_bytes_big(258, 2) == b'\x01\x02'
    assert int_to_bytes_big(255, 1) == b'\xff'
    assert int_to_bytes_big(1, 4) == b'\x00\x00\x00\x01'
