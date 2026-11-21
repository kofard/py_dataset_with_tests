"""Aho-Corasick search for multiple patterns in one pass over a text."""

from collections import deque


class AhoCorasick:
    def __init__(self, patterns: list[str]) -> None:
        if not isinstance(patterns, (list, tuple)) or not patterns:
            raise ValueError("patterns must be a non-empty sequence")
        if any(not isinstance(pattern, str) or not pattern for pattern in patterns):
            raise ValueError("every pattern must be a non-empty string")

        self.patterns = tuple(patterns)
        self._edges: list[dict[str, int]] = [{}]
        self._failure: list[int] = [0]
        self._outputs: list[list[int]] = [[]]

        for pattern_id, pattern in enumerate(patterns):
            node = 0
            for character in pattern:
                following = self._edges[node].get(character)
                if following is None:
                    following = len(self._edges)
                    self._edges[node][character] = following
                    self._edges.append({})
                    self._failure.append(0)
                    self._outputs.append([])
                node = following
            self._outputs[node].append(pattern_id)

        pending = deque(self._edges[0].values())
        while pending:
            state = pending.popleft()
            for character, child in self._edges[state].items():
                pending.append(child)
                suffix = self._failure[state]
                while suffix and character not in self._edges[suffix]:
                    suffix = self._failure[suffix]
                self._failure[child] = self._edges[suffix].get(character, 0)
                self._outputs[child].extend(self._outputs[self._failure[child]])

    def find_all(self, text: str) -> list[tuple[int, int, str]]:
        """Return (start, exclusive_end, pattern), including overlaps."""
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        result: list[tuple[int, int, str, int]] = []
        state = 0
        for end, character in enumerate(text, start=1):
            while state and character not in self._edges[state]:
                state = self._failure[state]
            state = self._edges[state].get(character, 0)
            for pattern_id in self._outputs[state]:
                pattern = self.patterns[pattern_id]
                result.append((end - len(pattern), end, pattern, pattern_id))
        result.sort(key=lambda item: (item[0], item[1], item[3]))
        return [(start, end, pattern) for start, end, pattern, _ in result]

    def count_by_pattern(self, text: str) -> dict[str, int]:
        """Count occurrences; duplicate input patterns share a dictionary key."""
        counts = dict.fromkeys(self.patterns, 0)
        for _, _, pattern in self.find_all(text):
            counts[pattern] += 1
        return counts

    def first_match(self, text: str) -> tuple[int, int, str] | None:
        matches = self.find_all(text)
        return matches[0] if matches else None
