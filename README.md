# Lookup CLI Tool

## Description

This tool allows you to lookup values from a YAML file based on a given name and field.

## Requirements

- Python 3.10+
- `pyyaml` library

## How to Run

### Locally

1. Install dependencies:
   ```bash
   pip install pyyaml
   ```

### Example Usage

bash
$ python3 lookup-cli.py Alice age
18

$ python3 lookup-cli.py Bob occupation
unemployed

$ python3 lookup-cli.py Charlie occupation
Field not found

$ python3 lookup-cli.py Eve age
Name not found

$ python3 lookup-cli.py
Usage: lookup-cli <name> <output_field>
