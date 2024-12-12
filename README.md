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

--------------------------------------------------------------------------------------------
# Software Engineer Code Test

## Task

Write a command-line tool in a language of your choice that runs like `lookup-cli <name> <output_field>`. The script should:

1. Read a YAML file that is stored somewhere on a File System.
2. Return the corresponding column by name, or display a message whenever applicable.
3. If input is missing, display a user manual for this CLI.

### YAML File

The YAML file contains the following data:

```yaml
- name: Alice
  age: 18
  occupation: student
- name: Bob
  age: 33
  occupation: unemployed
- name: Charlie
  age: 65
- name: David
  age: 25
  occupation: software engineer
```

### Requirements

1. **Script Name**: `lookup-cli`
2. **Input Parameters**:
   - `<name>`: The name to lookup in the YAML file.
   - `<output_field>`: The field to return for the given name (e.g., `age`, `occupation`).
3. **Output**:
   - If both `<name>` and `<output_field>` are provided and valid, return the value of the `<output_field>` for the given `<name>`.
   - If `<name>` is not found, display a message: `Name not found`.
   - If `<output_field>` is not found for the given `<name>`, display a message: `Field not found`.
   - If input is missing, display a user manual for this CLI.

### Example Usage

```bash
$ lookup-cli Alice age
18

$ lookup-cli Bob occupation
unemployed

$ lookup-cli Charlie occupation
Field not found

$ lookup-cli Eve age
Name not found

$ lookup-cli
Usage: lookup-cli <name> <output_field>
```

### Submission

- Submit your work via Github or any other means you prefer. 
- Include a README file with instructions on how to run your script.
- Prove that your script works in a Docker container, you can pick an image that suits your needs.
