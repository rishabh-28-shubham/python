import argparse

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="A simple command-line argument example.")

    # Define command-line arguments
    parser.add_argument("-f", "--file", help="Specify a file to process.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode.")
    parser.add_argument("input", help="Input data.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the argument values
    file_to_process = args.file
    verbose_mode = args.verbose
    input_data = args.input

    # Perform actions based on the arguments
    if verbose_mode:
        print("Verbose mode enabled.")
    
    print(f"Input data: {input_data}")
    
    if file_to_process:
        print(f"Processing file: {file_to_process}")

if __name__ == "__main__":
    main()
