import re

# Open the binary file ("ch1.bin" should be replaced by the file you want to open) in read mode
with open("ch1.bin", "rb") as bin_file: 
    byte_content = bin_file.read()
    strings = re.findall(b"[ -~]{4,}", byte_content)  # Extract readable ASCII strings of length >= 4

# Write extracted strings to a text file
with open("extracted_strings.txt", "w") as output_file:
    for s in strings:
        output_file.write(s.decode("ascii") + "\n")  # Write each string on a new line

print("Strings have been successfully written to extracted_strings.txt!")

