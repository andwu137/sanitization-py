# External Imports
from typing import Optional
from collections import namedtuple
import re

# Internal Imports


# Classes
Regex = namedtuple("Regex", ["pattern", "type"])


class Spotter:
    defaultRegexes: dict[str, Regex] = {}

    def __init__(self, regexes: Optional[dict[str, Regex]] = None):
        self.regexes: dict[str, Regex] = regexes or self.defaultRegexes
        self.regexes = {
            name: Regex(re.compile(regex.pattern, re.IGNORECASE), regex.type)
            for name, regex in self.regexes.items()
        }

    @staticmethod
    def runRegex(reg, line) -> str:
        raise NotImplementedError()
        if reg.type == "":
            return reg.pattern.sub("", line)
        return ""

    def process_line(self, line: str) -> str:
        raise NotImplementedError()
        for id, regex in self.regexes.items():
            line = self.runRegex(regex, line)
        return line


# Functions
def main():
    pass


if __name__ == "__main__":
    main()
