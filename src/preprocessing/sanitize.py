# External Imports
from typing import Optional
import re

# Internal Imports
from .preprocessing_types import Regex, RegexType, SpotType


# Classes
class Spotter:
    defaultRegexes: dict[SpotType, Regex] = {
        SpotType.EMAIL: Regex(
            r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""",
            RegexType.REMOVE,
        ),
        SpotType.PHONE: Regex(
            r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}",
            RegexType.REMOVE,
        ),
        # "creditcard-visa": Regex(r"4[0-9]{12}(?:[0-9]{3})?", RegexType.REMOVE),
        # "creditcard-mastercard": Regex(
        #     r"(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}",
        #     RegexType.REMOVE,
        # ),
        # "creditcard-americanexpress": Regex(
        #     r"3[47][0-9]{13}", RegexType.REMOVE
        # ),
        # "creditcard-dinersclub": Regex(
        #     r"3(?:0[0-5]|[68][0-9])[0-9]{11}", RegexType.REMOVE
        # ),
        # "creditcard-discover": Regex(
        #     r"6(?:011|5[0-9]{2})[0-9]{12}", RegexType.REMOVE
        # ),
        # "creditcard-jcb": Regex(
        #     r"(?:2131|1800|35\d{3})\d{11}", RegexType.REMOVE
        # ),
    }

    def __init__(
        self, logger, regexes: Optional[dict[SpotType, Regex]] = None
    ):
        self.logger = logger
        self.regexes: dict[SpotType, Regex] = regexes or self.defaultRegexes
        self.regexes = {
            name: Regex(re.compile(regex.pattern, re.IGNORECASE), regex.type)
            for name, regex in self.regexes.items()
        }

    def process_line(self, line: str) -> str:
        self.logger.debug(f"Begining process for line: '{line}'")
        for id, regex in self.regexes.items():
            line, caught = runRegex(regex, line)
            self.logger.debug(f"{{{line},{caught}}}")
        self.logger.log(f"Finished process for line; Result: '{line}'")
        return line

    def process_file(self, inputFile: str, outputFile: str) -> None:
        with open(inputFile, "r") as inp, open(outputFile, "w") as out:
            for line in map(self.process_line, inp):
                self.logger.log(line)
                out.write(line)


# Functions
def runRegex(reg, line) -> tuple[str, str]:
    matches = ""

    def get_matches(m) -> str:
        nonlocal matches
        matches = m
        return ""

    match reg.type:
        case RegexType.REMOVE:
            newLine: str = reg.pattern.sub(get_matches, line)
            return (newLine, matches)
        case _:
            raise NotImplementedError()
