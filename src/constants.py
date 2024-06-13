from enum import StrEnum  # type: ignore


class SpotType(StrEnum):
    PHONE = "phone"
    EMAIL = "email"
    SIN = "sin"
    ADDRESS = "address"
    STOPWORDS = "stopwords"
