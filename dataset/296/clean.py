"""IPv4 longest-prefix route lookup with stable metric tie breaking."""

from ipaddress import IPv4Address, IPv4Network, ip_network


class Route:
    def __init__(self, prefix: IPv4Network, gateway: IPv4Address, metric: int) -> None:
        self.prefix = prefix
        self.gateway = gateway
        self.metric = metric

    def as_tuple(self) -> tuple[str, str, int]:
        return str(self.prefix), str(self.gateway), self.metric


class RoutingTable:
    def __init__(self) -> None:
        self._routes: list[Route] = []

    @staticmethod
    def _network(cidr: str) -> IPv4Network:
        network = ip_network(cidr, strict=False)
        if not isinstance(network, IPv4Network):
            raise ValueError("only IPv4 routes are supported")
        return network

    def add(self, cidr: str, gateway: str, metric: int = 0) -> None:
        """Add a route; equal prefixes can have different gateways."""
        prefix = self._network(cidr)
        next_hop = IPv4Address(gateway)
        if not isinstance(metric, int) or isinstance(metric, bool) or metric < 0:
            raise ValueError("metric must be a non-negative integer")
        self._routes.append(Route(prefix, next_hop, metric))

    def best_route(self, destination: str) -> tuple[str, str, int] | None:
        """Prefer longest prefix, then lowest metric, then insertion order."""
        target = IPv4Address(destination)
        best: Route | None = None
        for candidate in self._routes:
            if target not in candidate.prefix:
                continue
            if best is None:
                best = candidate
                continue
            if candidate.prefix.prefixlen > best.prefix.prefixlen:
                best = candidate
            elif (candidate.prefix.prefixlen == best.prefix.prefixlen
                  and candidate.metric < best.metric):
                best = candidate
        return best.as_tuple() if best is not None else None

    def lookup(self, destination: str) -> str | None:
        route = self.best_route(destination)
        return route[1] if route is not None else None

    def remove(self, cidr: str, gateway: str | None = None) -> int:
        """Remove routes with the given prefix and optional gateway."""
        prefix = self._network(cidr)
        next_hop = IPv4Address(gateway) if gateway is not None else None
        old_count = len(self._routes)
        self._routes = [
            route for route in self._routes
            if not (route.prefix == prefix and
                    (next_hop is None or route.gateway == next_hop))
        ]
        return old_count - len(self._routes)

    def __len__(self) -> int:
        return len(self._routes)
