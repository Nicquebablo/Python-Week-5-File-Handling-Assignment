try:
    # File Creation
    with open("C:\\Users\K-IMARA SOCIETY\PLP school\PLP projects\File Handling Assignment\my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("Nicholas\n")
        file.write("12345\n")
        file.write("Random Numbers: 9876\n")

    # File Reading and Display
    with open("C:\\Users\K-IMARA SOCIETY\PLP school\PLP projects\File Handling Assignment\my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of my_file.txt:")
        print(file.read())

    # File Appending
    with open("C:\\Users\K-IMARA SOCIETY\PLP school\PLP projects\File Handling Assignment\my_file.txt", "a") as file:
        # Append three additional lines of text to the file
        file.write("Growth Mindset.\n")
        file.write("Warm Heart!\n")
        file.write("Have grit.\n")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    print("Task completed.")