#!/usr/bin/python3

class MyInt(int):
    def __eq__(self, i):
        return super().__ne__(i)

    def __ne__(self, i):
        return super().__eq__(i)
