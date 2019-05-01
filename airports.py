import argparse
import requests
import json
import csv


def parse_arguments():
    parser = argparse.ArgumentParser()

    # Group for --full and details_group, which contains other args
    group = parser.add_mutually_exclusive_group()
    details_group = group.add_mutually_exclusive_group()

    group.add_argument(
        "-f", "--full", action="store_true",
        help="Print all airports\' details")

    # Arguments that are mutually exclusive to --full argument
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

    return parser.parse_args()


class Airport:
    __slots__ = ("iata_code", "name", "city", "coordinates")

    def __init__(self, iata_code, name, city, coordinates):
        self.iata_code = iata_code
        self.name = name
        self.city = city
        self.coordinates = coordinates  # Tuple(latitude, longtitude)


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
            "https://api.skypicker.com/locations?type=subentity&term=GB&locale=en-US&active_only=true&location_types=airport&limit=10&sort=name")
        response.raise_for_status()
        # Returns list of Airport objects
        return parse_obtained_data(response.json())
    except requests.exceptions.RequestException as e:
        print("Request to API was unsuccessful\n", e)


def create_attribute_dict(args, airport):
    airport_dict = {}
    if args.iata or args.full:
        airport_dict["iata"] = airport.iata_code
    if args.names or args.full:
        airport_dict["name"] = airport.name
    if args.cities or args.full:
        airport_dict["city"] = airport.city
    if args.coords or args.full:
        airport_dict["coords"] = {
            "lat": airport.coordinates[0],
            "lon": airport.coordinates[1]
        }
    else:
        airport_dict["iata"] = airport.iata_code
        airport_dict["name"] = airport.name

    return airport_dict


def serialize_data(args, airports_list):
    airports_data = []
    for airport in airports_list:
        airports_data.append(create_attribute_dict(args, airport))

    # Standard output
    print(airports_data)

    # JSON File
    with open("airports_data.json", "w") as json_file:
        json.dump(airports_data, json_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    args = parse_arguments()
    airports_list = obtain_parse_data_from_API()
    serialize_data(args, airports_list)
