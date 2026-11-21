"""RFC 6901 JSON Pointer navigation and controlled document updates."""


class JSONPointer:
    def __init__(self, pointer: str) -> None:
        if not isinstance(pointer, str):
            raise TypeError("pointer must be a string")
        if pointer and not pointer.startswith("/"):
            raise ValueError("non-empty JSON Pointers must begin with /")
        self.tokens = tuple(self._decode(part) for part in pointer.split("/")[1:]) if pointer else ()

    @staticmethod
    def _decode(token: str) -> str:
        index = 0
        while index < len(token):
            if token[index] == "~":
                if index + 1 >= len(token) or token[index + 1] not in "01":
                    raise ValueError("invalid JSON Pointer escape")
                index += 2
            else:
                index += 1
        return token.replace("~1", "/").replace("~0", "~")

    @staticmethod
    def _index(token: str, length: int, allow_append: bool = False) -> int:
        if allow_append and token == "-":
            return length
        if not token.isascii() or not token.isdigit() or (len(token) > 1 and token[0] == "0"):
            raise IndexError(f"invalid JSON array index: {token!r}")
        index = int(token)
        if index >= length and not (allow_append and index == length):
            raise IndexError(f"array index out of range: {index}")
        return index

    @classmethod
    def _advance(cls, current: object, token: str) -> object:
        if isinstance(current, dict):
            return current[token]
        if isinstance(current, list):
            return current[cls._index(token, len(current))]
        raise TypeError("cannot descend into a scalar JSON value")

    def get(self, document: object) -> object:
        current = document
        for token in self.tokens:
            current = self._advance(current, token)
        return current

    def _parent(self, document: object) -> tuple[object, str]:
        if not self.tokens:
            raise ValueError("the root pointer has no parent")
        current = document
        for token in self.tokens[:-1]:
            current = self._advance(current, token)
        return current, self.tokens[-1]

    def set(self, document: object, value: object) -> object:
        """Replace a map key/list item, or append to a list with '/-'."""
        if not self.tokens:
            return value
        parent, token = self._parent(document)
        if isinstance(parent, dict):
            parent[token] = value
        elif isinstance(parent, list):
            if token == "-":
                parent.append(value)
            else:
                parent[self._index(token, len(parent))] = value
        else:
            raise TypeError("parent is not a JSON container")
        return document

    def remove(self, document: object) -> object:
        """Delete and return one existing value, without deleting the root."""
        parent, token = self._parent(document)
        if isinstance(parent, dict):
            return parent.pop(token)
        if isinstance(parent, list):
            return parent.pop(self._index(token, len(parent)))
        raise TypeError("parent is not a JSON container")
