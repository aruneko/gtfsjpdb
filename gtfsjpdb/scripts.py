import argparse

from gtfsjpdb.models.base import Base


sorted_class_names = [
    "Agency",
    "AgencyJP",
    "Stop",
    "Route",
    "RouteJP",
    "Service",
    "ServiceDate",
    "Shape",
    "Office",
    "Trip",
    "StopTime",
    "FareAttribute",
    "FareRule",
    "Frequency",
    "Transfer",
    "FeedInfo",
    "Translation",
]


def gtfsjpdb_load() -> None:
    args = get_args()

    subclasses = Base.__subclasses__()
    print(args.database_url)


def get_args():
    parser = argparse.ArgumentParser(
        prog="gtfsjpdb-load", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("file", help="URL or local path to GTFSJP zip FILE")
    parser.add_argument(
        "--database_url", "-d", help="DATABASE URL with appropriate privileges"
    )
    parser.add_argument("--schema", "-s", default="public", help="Database SCHEMA name")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    gtfsjpdb_load()
