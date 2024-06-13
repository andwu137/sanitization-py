from enum import StrEnum
from collections import namedtuple


Regex = namedtuple("Regex", ["pattern", "type"])


RegexType = StrEnum("RegexType", ["Remove"])


class SpotType(StrEnum):
    PHONE = "phone"
    EMAIL = "email"
    SIN = "sin"
    ADDRESS = "address"
    STOPWORDS = "stopwords"

    PHONE = "phone"
    EMAIL = "email"
    SIN = "sin"
    ADDRESS = "address"
    STOPWORDS = "stopwords"
