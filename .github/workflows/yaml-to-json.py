import sys
import yaml
import json
from os import path


def main(argv):
    if len(argv) < 2:
        print("Error: Expected input YAML file")
        print("Usage: python yaml-to-json.py <yaml input file> <json output file>")
        sys.exit(1)
    if len(argv) < 3:
        print("Error: Expected output JSON file")
        print("Usage: python yaml-to-json.py <yaml input file> <json output file>")
        sys.exit(1)

    root_dir = path.join(path.dirname(__file__), "../..")
    yaml_file_path = path.join(root_dir, argv[1])
    json_file_path = path.join(root_dir, argv[2])

    with open(yaml_file_path, "r") as yaml_in, open(json_file_path, "w") as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object, json_out)


main(sys.argv)
