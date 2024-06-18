from charting import *
from logger import *
from preprocessing import constants, sanitize, sensitive_info_regexes


def main():
    s = sanitize.Spotter(Logger("run.log", debugEnabled=True))
    print("output:", s.process_line("name@gmail.com"))


if __name__ == "__main__":
    main()
