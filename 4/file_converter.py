import argparse
from typing import List
import pandas as pd


class FileHandler:
    def __init__(self, file_extension: str) -> None:
        self.file_extension = file_extension.lower()

    def can_handle(self, file_name: str) -> bool:
        return file_name.lower().endswith(self.file_extension)

    def read_file(self, file_name: str) -> pd.DataFrame:
        raise NotImplementedError


class CsvHandler(FileHandler):
    def __init__(self) -> None:
        super().__init__(file_extension=".csv")

    def read_file(self, file_name: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_name)
        except Exception as e:
            raise Exception(f"Error while reading CSV file: {e}")


class JsonHandler(FileHandler):
    def __init__(self) -> None:
        super().__init__(file_extension=".json")

    def read_file(self, file_name: str) -> pd.DataFrame:
        try:
            return pd.read_json(file_name)
        except Exception as e:
            raise Exception(f"Error while reading JSON file: {e}")


class FileProcessor:
    def __init__(self, handlers: List[FileHandler]) -> None:
        self.handlers = handlers

    def process_files(self, input_file: str, output_file: str) -> None:
        df = pd.DataFrame()
        with open(input_file, "r") as f:
            for file_name in f:
                for handler in self.handlers:
                    if handler.can_handle(file_name):
                        df = pd.concat([df, handler.read_file(file_name.strip())])
                        break
                else:
                    raise Exception(f"No handler found for file: {file_name.strip()}")
        df.to_csv(output_file, index=False)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Process some files.")
    parser.add_argument("input_file", type=str, help="Input file with list of file names to process")
    parser.add_argument("output_file", type=str, help="Output file to write processed data to")
    parser.add_argument("-c", "--csv", action="store_true", help="Include CSV files in processing")
    parser.add_argument("-j", "--json", action="store_true", help="Include JSON files in processing")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    handlers = []
    if args.csv:
        handlers.append(CsvHandler())
    if args.json:
        handlers.append(JsonHandler())

    processor = FileProcessor(handlers)
    processor.process_files(args.input_file, args.output_file)


if __name__ == "__main__":
    main()