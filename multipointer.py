import builtins

class MultiPointer:
    def index(self, *index):
        if len(index) > 1:
            next = self[index[0]]
            if type(next).__name__ in globals() and "index" in globals()[type(next).__name__]().__dir__():
                return globals()[type(next).__name__](self[index[0]]).index(*index[1:])
        else:
            return self[index[0]]


class dict(builtins.dict):
    index = MultiPointer.index


class list(builtins.list):
    index = MultiPointer.index


class str(builtins.str):
    index = MultiPointer.index


class tuple(builtins.tuple):
    index = MultiPointer.index


class bytearray(builtins.bytearray):
    index = MultiPointer.index


class bytes(builtins.bytes):
    index = MultiPointer.index


class enumerate(builtins.enumerate):
    index = MultiPointer.index


class frozenset(builtins.frozenset):
    index = MultiPointer.index


class map(builtins.map):
    index = MultiPointer.index


class set(builtins.set):
    index = MultiPointer.index


class zip(builtins.zip):
    index = MultiPointer.index

def index(obj, *keys):
    return MultiPointer.index(obj, *keys)