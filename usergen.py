#!/usr/bin/env python3
# usergen.py — Generate username variations based on a list of names.
# Credits: made by fairalien
# No external dependencies; uses only Python standard library

import sys

USAGE = (
    "Usage: usergen.py <input_file> <output_file> <domain>\n"
    "  input_file  File with 'First Last' names, one per line\n"
    "  output_file File to write generated usernames\n"
    "  domain      Domain to append (include '@'), e.g. @example.com\n"
    "Example:\n"
    "  usergen.py names.txt users.txt @example.com"
)

# Parse command-line arguments manually
if len(sys.argv) != 4 or sys.argv[1] in ('-h', '--help'):
    sys.stdout.write(USAGE)
    sys.exit(1)

input_file, output_file, domain = sys.argv[1], sys.argv[2], sys.argv[3]

# Fixed patterns
patterns = [
    '{first}_{last}{domain}',
    '{first}.{last}{domain}',
    '{f}_{last}{domain}',
    '{f}.{last}{domain}',
]

# Read names
try:
    with open(input_file, 'r') as fin:
        lines = fin.readlines()
except Exception as e:
    sys.stderr.write(f"Error: Cannot open input file '{input_file}': {e}\n")
    sys.exit(1)

# Generate usernames
users = []
for line in lines:
    parts = line.strip().split()
    if len(parts) < 2:
        continue
    first = parts[0]
    last = parts[-1]
    f = first[0]
    for pat in patterns:
        users.append(pat.format(first=first, last=last, f=f, domain=domain).lower())

# Write output
try:
    with open(output_file, 'w') as fout:
        for user in users:
            fout.write(user + '\n')
except Exception as e:
    sys.stderr.write(f"Error: Cannot write to output file '{output_file}': {e}\n")
    sys.exit(1)

print(f"Generated {len(users)} usernames into '{output_file}'")
