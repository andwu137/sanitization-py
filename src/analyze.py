from preprocessing import sanitize


def main():
    s = sanitize.Spotter()
    print("output:", s.process_line("name@gmail.com"))


if __name__ == "__main__":
    main()
