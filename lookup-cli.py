import argparse
import yaml
import sys

# Function to load YAML file
def load_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print("Error: YAML file not found.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse YAML file - {e}")
        sys.exit(1)

# Function to perform the lookup
def lookup(data, name, output_field):
    for record in data:
        if record.get("name") == name:
            return record.get(output_field, "Field not found")
    return "Name not found"

# Main function
def main():
    parser = argparse.ArgumentParser(
        description="Lookup CLI Tool: Find values by name and field from a YAML file."
    )
    parser.add_argument("name", nargs="?", help="The name to lookup")
    parser.add_argument("output_field", nargs="?", help="The field to return")
    args = parser.parse_args()

    # If arguments are missing, print usage instructions
    if not args.name or not args.output_field:
        print("Usage: lookup-cli <name> <output_field>")
        sys.exit(0)

    # Load YAML file
    yaml_file = "data.yaml"  # Replace with the actual file path
    data = load_yaml_file(yaml_file)

    # Perform lookup
    result = lookup(data, args.name, args.output_field)
    print(result)

if __name__ == "__main__":
    main()
