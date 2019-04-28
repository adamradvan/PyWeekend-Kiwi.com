import argparse

parser = argparse.ArgumentParser()

# Group for --full and details_group, which contains other args
group = parser.add_mutually_exclusive_group()
details_group = group.add_mutually_exclusive_group()

group.add_argument(
    "-f", "--full", action="store_true",
    help="Print all airports\' details")

# Arguments that are mutually exclusive to -f/--full argument
details_group.add_argument(
    "-c", "--cities", action="store_true",
    help="Print cities\' names")
details_group.add_argument(
    "-i", "--iata", action="store_true",
    help="Print IATA codes")
details_group.add_argument(
    "-co", "--coords", action="store_true",
    help="Print airports\' coordinates")
details_group.add_argument(
    "-n", "--names", action="store_true",
    help="Print airports\' names")

args = parser.parse_args()
