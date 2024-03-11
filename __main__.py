# Imports necessary modules for handling file paths and parsing command line arguments
from pathlib import Path
import argparse
# Imports the process_inputfile function from prepostfix.py in the current directory
from .prepostfix import process_inputfile


def main():
    """
    Executes the program using command line arguments to specify input and output files.
    Utilizes argparse for easy CLI interactions, and pathlib for OS-independent file path handling.
    Reads prefix expressions from the input file, processes each line, converts them to postfix,
    and writes to the output file. Each converted line is echoed to the console.
    """
    # Sets up command line argument parsing
    arg_parser = argparse.ArgumentParser(description="Converts prefix expressions to postfix.")
    arg_parser.add_argument("in_file", type=str, help="Input file path with prefix expressions")
    arg_parser.add_argument("out_file", type=str, help="Output file path for postfix expressions")
    args = arg_parser.parse_args()

    # Defines file paths using pathlib for compatibility
    in_path = Path(args.in_file)
    out_path = Path(args.out_file)

    # Opens the input and output files, and processes each line
    with in_path.open('r') as input_file, out_path.open('w') as output_file:
        process_inputfile(input_file, output_file)


if __name__ == "__main__":
    main()
