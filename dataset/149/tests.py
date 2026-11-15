import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    token = Token(1, 2, "c")
    assert repr(token) == '(1, 2, c)'
    assert str(token) == '(1, 2, c)'
    lz77_compressor = LZ77Compressor()
    assert str(lz77_compressor.compress("ababcbababaa")) == '[(0, 0, a), (0, 0, b), (2, 2, c), (4, 3, a), (2, 2, a)]'
    assert str(lz77_compressor.compress("aacaacabcabaaac")) == '[(0, 0, a), (1, 1, c), (3, 4, b), (3, 3, a), (1, 2, c)]'
    lz77_compressor = LZ77Compressor()
    assert lz77_compressor.decompress([Token(0, 0, 'c'), Token(0, 0, 'a'),
Token(0, 0, 'b'), Token(0, 0, 'r'), Token(3, 1, 'c'),
Token(2, 1, 'd'), Token(7, 4, 'r'), Token(3, 5, 'd')]) == 'cabracadabrarrarrad'
    assert lz77_compressor.decompress([Token(0, 0, 'a'), Token(0, 0, 'b'),
Token(2, 2, 'c'), Token(4, 3, 'a'), Token(2, 2, 'a')]) == 'ababcbababaa'
    assert lz77_compressor.decompress([Token(0, 0, 'a'), Token(1, 1, 'c'),
Token(3, 4, 'b'), Token(3, 3, 'a'), Token(1, 2, 'c')]) == 'aacaacabcabaaac'
    lz77_compressor = LZ77Compressor()
    assert lz77_compressor._find_encoding_token("abrarrarrad", "abracad").offset == 7
    assert lz77_compressor._find_encoding_token("adabrarrarrad", "cabrac").length == 1
    assert lz77_compressor._find_encoding_token("abc", "xyz").offset == 0
    assert lz77_compressor._find_encoding_token("abc", "").offset == 0
    lz77_compressor = LZ77Compressor(13, 6)
    assert lz77_compressor._match_length_from_index("rarrad", "adabrar", 0, 4) == 5
    assert lz77_compressor._match_length_from_index("adabrarrarrad",
    "cabrac", 0, 1) == 1
