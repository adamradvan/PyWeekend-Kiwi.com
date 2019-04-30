import argparse
import requests

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


class Airport:
    __slots__ = ("iata_code", "name", "city", "coordinates")

    def __init__(self, iata_code, name, city, coordinates):
        self.iata_code = iata_code
        self.name = name
        self.city = city
        self.coordinates = coordinates  # Tuple(latitude, longtitude)

    def pretty_print(self):
        pass


def parse_obtained_data(data_dict):
    airports = []
    for airport_data in data_dict["locations"]:
        airport = Airport(
            airport_data["code"],
            airport_data["name"],
            airport_data["city"]["name"],
            (airport_data["location"]["lat"], airport_data["location"]["lon"])
        )
        airports.append(airport)
    return airports


def obtain_parse_data_from_API():
    try:
        response = requests.get(
            "https://api.skypicker.com/locations?type=subentity&term=GB&locale=en-US&active_only=true&location_types=airport&limit=100&sort=name")
        response.raise_for_status()
        parse_obtained_data(response.json())
    except requests.exceptions.RequestException as e:
        print("Request to API was unsuccessful\n", e)


def create_JSON_file(airports_list):
    pass  # TODO: Create JSON file from list of Airport classes


def display_data(args, airports_list):
    pass  # TODO: Depending on args, display data about ariports, create Airport.pretty_print() method


if __name__ == "__main__":
    args = parser.parse_args()
    airports_list = obtain_parse_data_from_API()
    create_JSON_file(airports_list)
    display_data(args, airports_list)
