# KeePass Usergen

Generate username variations from a list of "First Last" names, with flexible input, output, and domain settings.

**Credits:** made by fairalien

---

## Description

`usergen.py` reads a text file of names (one "First Last" per line) and produces a list of potential usernames using four fixed patterns:

* `first_last@domain`
* `first.last@domain`
* `f_last@domain` (first initial)
* `f.last@domain`

The script requires no external dependencies, using only Python's standard library.

## Features

* **No dependencies**: only Python ≥3.6 required.
* **Configurable**: choose your input file, output file, and domain via command-line arguments.
* **Built-in help**: run with `-h` or `--help` to see usage instructions.
* **Batch generation**: handles large name lists efficiently.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/alaeddine03/usergen.git
   cd usergen
   ```
2. Make the script executable:

   ```bash
   chmod +x usergen.py
   ```
3. (Optional) Add to your PATH:

   ```bash
   sudo ln -s $(pwd)/usergen.py /usr/local/bin/usergen
   ```

## Usage

```bash
./usergen.py <input_file> <output_file> <domain>
```

* `<input_file>`: Text file with one name per line ("First Last").
* `<output_file>`: Destination file to write generated usernames.
* `<domain>`: Domain to append (include `@`), e.g. `@example.com`.

### Examples

Generate users for `names.txt` into `users.txt` using the default domain:

```bash
./usergen.py names.txt users.txt @example.com
```

If you installed globally:

```bash
usergen names.txt staff_users.txt @company.com
```

## Help

```bash
./usergen.py -h
```

Displays the usage instructions.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---

*Happy user generation!*
