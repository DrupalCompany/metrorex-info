import argparse

from lib.parse import CardInfo
from lib.utils import read_file, hex_to_bytes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""Metrorex info: get last timestamp from card.""",
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        "file",
        help="Card dump file in hexadecimal format.",
        type=argparse.FileType('r'),
        default='-')

    args = parser.parse_args()
    return args


def run(args=None):
    card = CardInfo(hex_to_bytes(read_file(args.file)))

    print(card.get_timestamp())


def main():
    run(parse_args())


if __name__ == "__main__":
    main()
