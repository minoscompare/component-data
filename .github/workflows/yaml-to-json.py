import sys
import yaml
import json

def main(argv):
	if len(argv) < 2:
		print("Error: Expected input YAML file")
		print("Usage: python yaml-to-json.py <yaml input file> <json output file>")
		sys.exit(1)
	if len(argv) < 3:
		print("Error: Expected output JSON file")
		print("Usage: python yaml-to-json.py <yaml input file> <json output file>")
		sys.exit(1)
	with open(argv[1], 'r') as yaml_in, open(argv[2], "w") as json_out:
		yaml_object = yaml.safe_load(yaml_in)
		json.dump(yaml_object, json_out)

main(sys.argv)
