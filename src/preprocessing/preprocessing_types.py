from enum import StrEnum, Enum  # type: ignore
from collections import namedtuple


Regex = namedtuple("Regex", ["pattern", "type"])


RegexType = Enum("RegexType", ["REMOVE"])


class SpotType(StrEnum):
    PHONE = "phone"
    EMAIL = "email"
    SIN = "sin"
    ADDRESS = "address"
    STOPWORDS = "stopwords"
