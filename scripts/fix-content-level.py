# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.  
# SPDX-License-Identifier: MIT-0

import os
import re

def is_standard_level(number):
    """Check if the number is a standard content level."""
    return number.strip() in {'100', '200', '300', '400'}

def check_content_levels(numbers_str, file_path):
    """Check if all numbers in the string are standard levels."""
    numbers = numbers_str.split('/')
    non_standard = [num for num in numbers if not is_standard_level(num)]
    if non_standard:
        print(f"WARNING in {file_path}:")
        print(f"  Non-standard content level(s) found: {', '.join(non_standard)}")
        print(f"  Expected values are: 100, 200, 300, 400")
        print(f"  Full content level string: {numbers_str}\n")

def process_markdown_file(file_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression pattern to match various forms of "Content Level"
    # Including existing markdown formatting
    pattern = r'([#\-]*\s*)(\*{0,2})(content[-\s]?level:?[\s]*)((?:\d+(?:\/\d+)*))(\*{0,2})'
    
    # Replace function to format the match
    def replace_format(match):
        level_numbers = match.group(4)
        check_content_levels(level_numbers, file_path)
        return f'\n\n**Content Level: {level_numbers}**\n'

    # Perform the replacement (case insensitive)
    modified_content = re.sub(pattern, replace_format, content, flags=re.IGNORECASE)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

def process_directory(directory):
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory):
        # Process each file with .md extension
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                try:
                    process_markdown_file(file_path)
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Get the current directory
    current_directory = os.getcwd()
    
    # Process all markdown files in the current directory and its subdirectories
    process_directory(current_directory)
    print("\nProcessing complete!")
