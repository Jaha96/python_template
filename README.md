# Your Project Title

This is example README.md file for a typical Python project. It is a good idea to include the following sections in your README.md file.
Put your project description here.

## Requirements
 - Python 3.8+
 - pip 23.0+

## Installation

To setup environment and install the project dependencies run:

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment (Linux/Mac):
   ```bash
   source .venv/bin/activate
   ```

   On Windows:
   ```bash
   .\.venv\Scripts\activate
   ```

3. Upgrade pip to the latest version:
   ```bash
   python -m pip install --upgrade pip
   ```

4. Check the pip version:
   ```bash
   pip --version  # Example: pip 23.0.1
   ```

5. Check the Python version:
   ```bash
   python --version  # Example: Python 3.8.3
   ```

6. Install the required packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command:

```bash
put your command here
```

## Command line arguments

 Below is the example of the command line arguments that can be used with the script.

- `--help`
   - Type: `boolean`
   - Optional: `True`
   - Description: Show the help message and exit

## Example usage

```bash
put your example commands here
```

## Unit Test

To run unit tests, use the following command:

```bash
coverage run
```

Use `coverage report` to report on the results:

```bash
coverage report
```

For a nicer presentation, use `coverage html` to get annotated HTML listings detailing missed lines:

```bash
coverage html
```

