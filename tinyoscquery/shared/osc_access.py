from enum import IntEnum


class OSCAccess(IntEnum):
    NO_VALUE = 0
    READONLY_VALUE = 1
    WRITEONLY_VALUE = 2
    READWRITE_VALUE = 3
