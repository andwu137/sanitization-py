from datetime import datetime


class Logger:
    file_path = ""

    @staticmethod
    def log(msg):
        with open(Logger.file_path, "w") as file:
            file.write(f"{datetime.now()} - {msg}")
        file.close()

    @staticmethod
    def log_start(obj, **args):
        string = f"Began process {obj.getSpotterUID()} on file blank\n"
        Logger.log(string)

    @staticmethod
    def log_removal(obj, data):
        # DATETIME SPOTTERUID REMOVED THIS STRING: ------
        string = f"Spotter {obj.getSpotterUID()} removed {data}\n"
        Logger.log(string)

    @staticmethod
    def log_end(obj, num):
        string = f"Spotter {obj.getSpotterUID()} ended process with {num} removals.\n"
        Logger.log(string)

    @staticmethod
    def log_error(obj, error, msg):
        string = f"{error} - Spotter {obj.getSpotterUID()}: {msg} \n"
        Logger.log(string)
