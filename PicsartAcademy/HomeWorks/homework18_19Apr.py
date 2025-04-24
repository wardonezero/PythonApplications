# 18 /19 April 2025

import os

#Write a program to open the file in read mode and print each line, stripping any leading or trailing whitespace.
with open('notes.txt', 'r') as file:
    for line in file:
        print(line.strip())
file.close()

#write the text "Python is fun!" into it. Close the file and reopen it to verify its content.
with open('notes.txt', 'w') as file:
    file.write("Python is fun!")
file.close()
with open('notes.txt', 'r') as file:
    content = file.read()
    print(content)
file.close()

#Open the file notes.txt in append mode and add the text "Remember to review file handling in Python!" as a new line at the end. If the file does not exist, create it.
with open('notes.txt', 'a') as file:
    file.write("\nRemember to review file handling in Python!")
file.close()

#Write a program to open the file story.txt, read its content, and count the total number of words in the file. Display the count to the user.
with open('notes.txt', 'r') as file:
    content = file.read()
    word_count = len(content.split())
    print(f"Total number of words in the file: {word_count}")
file.close()

#Write a program to copy the content of source.txt into destination.txt. If the destination file already exists, overwrite its content.
with open('notes.txt', 'r') as source_file:
    content = source_file.read()
with open('destination.txt', 'w') as destination_file:
    destination_file.write(content)
destination_file.close()
source_file.close()

#Write a program to remove all blank lines from data.txt and save the cleaned content to cleaned_data.txt.
with open('notes.txt', 'r') as source_file:
    lines = source_file.readlines()
with open('cleaned_data.txt', 'w') as destination_file:
    for line in lines:
        if line.strip():
            destination_file.write(line)
destination_file.close()
source_file.close()

#Write a program to copy the content of a binary file image.jpg into a new file copy_image.jpg. Ensure that the copied file is identical to the original.
with open('image.jpg', 'rb') as source_file:
    content = source_file.read()
with open('copy_image.jpg', 'wb') as destination_file:
    destination_file.write(content)
destination_file.close()
source_file.close()

#Write a program to analyze a log file log.txt and generate a report of the total number of occurrences for each log level (INFO, WARNING, ERROR) in a new file summary.txt.
log_levels = ['INFO', 'WARNING', 'ERROR']
log_counts = {level: 0 for level in log_levels}
with open('log.txt', 'r') as log_file:
    for line in log_file:
        for level in log_levels:
            if level in line:
                log_counts[level] += 1
with open('summary.txt', 'w') as summary_file:
    for level, count in log_counts.items():
        summary_file.write(f"{level}: {count}\n")
summary_file.close()
log_file.close()

#Wreate a new text file named relative_output.txt in a folder called relative_files (located relative to your script's directory). Write "This is a file created using a relative path." into the file.
# Check if the relative_files directory exists. If not, create it.
if not os.path.exists('relative_files'):
    os.makedirs('relative_files')
with open('relative_files/relative_output.txt', 'w') as file:
    file.write("This is a file created using a relative path.")
file.close()
with open('relative_files/relative_output.txt', 'r') as file:
    content = file.read()
    print(content)
file.close()

#Open the file example_data.txt located in the data_files folder (relative to the script directory). Print its content to the console.
# Ensure that the folder data_files exists and contains the file example_data.txt.

if not os.path.exists('data_files'):
    os.makedirs('data_files')
with open('data_files/example_data.txt', 'w') as file:
    file.write("This is an example data file.")
file.close()
with open('data_files/example_data.txt', 'r') as file:
    content = file.read()
    print(content)
file.close()

#Write a program to determine and print the absolute path of the file settings.json, which is located in the config folder relative to the script directory.
config_folder = os.path.join(os.path.dirname(__file__), 'config')
settings_file = os.path.join(config_folder, 'settings.json')
absolute_path = os.path.abspath(settings_file)
print(f"Absolute path of settings.json: {absolute_path}")

#Write a program to create a new file named exclusive_file.txt using the x mode and write the text "This file is created using x mode." into it. Ensure the program handles errors gracefully if the file already exists.
# Use a try...except block to catch the FileExistsError if the file already exists.
try:
    with open('exclusive_file.txt', 'x') as file:
        file.write("This file is created using x mode.")
except FileExistsError:
    print("File already exists. Please choose a different name or delete the existing file.")

#Write a program that prompts the user to input a file name. Create a new file with that name using x mode and write "File <filename> created successfully." into it. If the file already exists, notify the user.
# Catch FileExistsError and notify the user if the file exists.
file_name = input("Enter the file name: ")
try:
    with open(f"{file_name}.txt", 'x') as file:
        file.write(f"File {file_name} created successfully.")
except FileExistsError:
    print(f"File {file_name} already exists. Please choose a different name.")


