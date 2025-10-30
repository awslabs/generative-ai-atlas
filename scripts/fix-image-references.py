# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.  
# SPDX-License-Identifier: MIT-0

import os
import re
import argparse
import sys
from typing import Optional

def process_markdown_file(file_path: str) -> Optional[str]:
    """
    Process a single markdown file to update image references.
    Returns error message if there's an error, None if successful.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except IOError as e:
        return f"Error reading file {file_path}: {str(e)}"
    except UnicodeDecodeError as e:
        return f"Error decoding file {file_path}: {str(e)}"

    try:
        # Regular expression to find markdown image references
        pattern = r'!\[(.*?)\]\((.*?)\)'
        
        def replace_image(match):
            alt_text = match.group(1)
            image_path = match.group(2)
            return f'<div style="margin:auto;text-align:center;width:100%;"><img src="{image_path}" alt="{alt_text}" width="800"/></div>'

        # Replace all image references
        new_content = re.sub(pattern, replace_image, content)

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
            
    except IOError as e:
        return f"Error writing to file {file_path}: {str(e)}"
    except Exception as e:
        return f"Unexpected error processing file {file_path}: {str(e)}"
    
    return None

def process_directory(directory: str) -> tuple[int, int]:
    """
    Process all markdown files in a directory recursively.
    Returns tuple of (success_count, error_count).
    """
    success_count = 0
    error_count = 0

    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    print(f"Processing: {file_path}")
                    
                    error = process_markdown_file(file_path)
                    if error:
                        print(f"Error: {error}", file=sys.stderr)
                        error_count += 1
                    else:
                        success_count += 1
                        
    except PermissionError as e:
        print(f"Permission denied accessing directory {directory}: {str(e)}", file=sys.stderr)
        return success_count, error_count + 1
    except Exception as e:
        print(f"Unexpected error accessing directory {directory}: {str(e)}", file=sys.stderr)
        return success_count, error_count + 1

    return success_count, error_count

def validate_directory(directory: str) -> Optional[str]:
    """
    Validate that the directory exists and is accessible.
    Returns error message if invalid, None if valid.
    """
    if not os.path.exists(directory):
        return f"Directory does not exist: {directory}"
    if not os.path.isdir(directory):
        return f"Path is not a directory: {directory}"
    if not os.access(directory, os.R_OK):
        return f"Directory is not readable: {directory}"
    return None

def main():
    parser = argparse.ArgumentParser(description="Process markdown files to update image references.")
    parser.add_argument('directory', nargs='?', default=os.getcwd(),
                      help="The directory to process (default: current directory)")
    args = parser.parse_args()

    # Validate directory
    error = validate_directory(args.directory)
    if error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    # Process files
    print(f"Starting to process markdown files in: {args.directory}")
    success_count, error_count = process_directory(args.directory)

    # Print summary
    print("\nProcessing complete!")
    print(f"Successfully processed files: {success_count}")
    if error_count > 0:
        print(f"Files with errors: {error_count}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
