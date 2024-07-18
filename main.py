#!/usr/bin/env python3

class Foo:
    def __init__(self, a: int):
        self.a = a
    def foo_meth(self) -> str:
        return str(self.a)


class Bar:
    def __init__(self, b: str):
        self.b = b

    def bar_meth(self) -> int:
        try:
            return int(self.b)
        except ValueError:
            return -1

