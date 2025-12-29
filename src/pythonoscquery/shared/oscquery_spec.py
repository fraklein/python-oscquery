import enum
from enum import Enum


class OSCQueryAttribute(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    FULL_PATH = enum.auto()
    DESCRIPTION = enum.auto()
    VALUE = enum.auto()
    TYPE = enum.auto()
    CONTENTS = enum.auto()
    ACCESS = enum.auto()
    HOST_INFO = enum.auto()
    RANGE = enum.auto()
