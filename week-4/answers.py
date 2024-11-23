def read_and_modify_file():
    # Ask the user for the filename
    input_filename = input("Please enter the filename to read: ")
    output_filename = "modified_" + input_filename  # Name for the new file

    try:
        # Attempt to open the file for reading
        with open(input_filename, 'r') as file:
            content = file.read()  # Read the entire content of the file
            
            # Modify the content (example: converting to uppercase)
            modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()