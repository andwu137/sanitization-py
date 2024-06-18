# External Imports
from typing import Optional
import re

# Internal Imports
from constants import Regex, RegexType, SpotType


# Classes
class Spotter:
    defaultRegexes: dict[SpotType, Regex] = {}

    def __init__(self, regexes: Optional[dict[SpotType, Regex]] = None):
        self.regexes: dict[SpotType, Regex] = regexes or self.defaultRegexes
        self.regexes = {
            name: Regex(re.compile(regex.pattern, re.IGNORECASE), regex.type)
            for name, regex in self.regexes.items()
        }

    def process_line(self, line: str) -> str:
        for id, regex in self.regexes.items():
            line, caught = runRegex(regex, line)
        return line

    def process_file(self, inputFile: str, outputFile: str) -> None:
        with open(inputFile, "r") as inp, open(outputFile, "w") as out:
            for line in map(self.process_line, inp):
                out.write(line)


# Functions
def runRegex(reg, line) -> tuple[str, str]:
    matches = ""

    def get_matches(m) -> str:
        nonlocal matches
        matches = m
        return ""

    match reg.type:
        case RegexType.Remove:
            newLine: str = reg.pattern.sub(get_matches, line)
            return (newLine, matches)
        case _:
            raise NotImplementedError()


def main():
    pass


if __name__ == "__main__":
    main()
