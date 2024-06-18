from datetime import datetime


class Logger:
    def __init__(self, file_path: str, debugEnabled: bool = False):
        self.file_path = file_path
        self.debugEnabled = debugEnabled

    def log(self, msg):
        with open(self.file_path, "a") as file:
            file.write(f"{datetime.now()} - {msg}\n")

    def debug(self, msg):
        if self.debugEnabled:
            self.log(msg)

    def log_start(self, obj, **args):
        self.log(f"Began process {obj.getSpotterUID()} on file blank\n")

    def log_removal(self, obj, data):
        # DATETIME SPOTTERUID REMOVED THIS STRING: ------
        self.log(f"Spotter {obj.getSpotterUID()} removed {data}\n")

    def log_end(self, obj, num):
        self.log(
            f"Spotter {obj.getSpotterUID()} ended process with {num} removals.\n"
        )

    def log_error(self, obj, error, msg):
        self.log(f"{error} - Spotter {obj.getSpotterUID()}: {msg} \n")
