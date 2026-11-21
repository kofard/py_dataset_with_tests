import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})


def test_solution():
    routes = RoutingTable()
    assert routes.lookup("10.0.0.1") is None
    assert routes.best_route("8.8.8.8") is None
    routes.add("0.0.0.0/0", "192.0.2.1", metric=100)
    routes.add("10.0.0.0/8", "192.0.2.2", metric=50)
    routes.add("10.20.0.0/16", "192.0.2.3", metric=20)
    routes.add("10.20.30.0/24", "192.0.2.4", metric=10)
    assert len(routes) == 4
    assert routes.lookup("8.8.8.8") == "192.0.2.1"
    assert routes.lookup("10.9.1.1") == "192.0.2.2"
    assert routes.lookup("10.20.9.10") == "192.0.2.3"
    assert routes.lookup("10.20.30.255") == "192.0.2.4"
    assert routes.best_route("10.20.30.17") == ("10.20.30.0/24", "192.0.2.4", 10)

    routes.add("10.20.30.0/24", "192.0.2.5", metric=2)
    assert routes.lookup("10.20.30.17") == "192.0.2.5"
    routes.add("10.20.30.0/24", "192.0.2.6", metric=2)
    assert routes.lookup("10.20.30.17") == "192.0.2.5"
    assert routes.remove("10.20.30.0/24", "192.0.2.5") == 1
    assert routes.lookup("10.20.30.17") == "192.0.2.6"
    assert routes.remove("10.20.30.0/24") == 2
    assert routes.lookup("10.20.30.17") == "192.0.2.3"
    assert routes.remove("198.51.100.0/24") == 0

    routes.add("172.16.33.123/16", "192.0.2.10")
    assert routes.best_route("172.16.1.1")[0] == "172.16.0.0/16"
    for cidr, gateway, metric in (("::/0", "192.0.2.1", 0),
                                   ("10.0.0.0/8", "192.0.2.1", -1),
                                   ("10.0.0.0/8", "192.0.2.1", True)):
        try:
            routes.add(cidr, gateway, metric)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid route was accepted")
