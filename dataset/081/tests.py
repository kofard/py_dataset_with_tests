import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    alice = DiffieHellman()
    bob = DiffieHellman()
    alice_private = alice.get_private_key()
    alice_public = alice.generate_public_key()
    bob_private = bob.get_private_key()
    bob_public = bob.generate_public_key()
    alice_shared = alice.generate_shared_key(bob_public)
    bob_shared = bob.generate_shared_key(alice_public)
    assert alice_shared == bob_shared
    alice_shared = DiffieHellman.generate_shared_key_static(
    alice_private, bob_public
)
    bob_shared = DiffieHellman.generate_shared_key_static(
    bob_private, alice_public
)
    assert alice_shared == bob_shared
