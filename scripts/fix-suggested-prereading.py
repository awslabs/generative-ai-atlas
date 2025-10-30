# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.  
# SPDX-License-Identifier: MIT-0

import os
import re
import sys

def standardize_prereading(content):
    # Handle each pattern separately with proper escaping
    replacements = [
        # Headers (H1-H4)
        (r'(?im)^#{1,4}\s*suggested\s+(pre-reading|prereading):?\s*$', '## Suggested Pre-Reading\n'),
        
        # Bold with asterisks or underscores
        (r'(?im)^\*\*\s*suggested\s+(pre-reading|prereading):?\s*\*\*\s*$', '## Suggested Pre-Reading\n'),
        (r'(?im)^__\s*suggested\s+(pre-reading|prereading):?\s*__\s*$', '## Suggested Pre-Reading\n'),
        
        # Italic with asterisk or underscore
        (r'(?im)^\*\s*suggested\s+(pre-reading|prereading):?\s*\*\s*$', '## Suggested Pre-Reading\n'),
        (r'(?im)^_\s*suggested\s+(pre-reading|prereading):?\s*_\s*$', '## Suggested Pre-Reading\n'),
        
        # Plain text
        (r'(?im)^suggested\s+(pre-reading|prereading):?\s*$', '## Suggested Pre-Reading\n')
    ]

    # Apply each replacement pattern
    modified_content = content
    for pattern, replacement in replacements:
        modified_content = re.sub(pattern, replacement, modified_content)

    # Ensure proper spacing after header
    modified_content = re.sub(r'(## Suggested Pre-Reading\n)(?!\n)', r'\1\n', modified_content)

    return modified_content

def process_markdown_files(directory):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    modified_content = standardize_prereading(content)
                    
                    if modified_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(modified_content)
                        print(f"Processed: {file_path}")
                    
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")

def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    process_markdown_files(directory)
    print("Processing complete!")

if __name__ == "__main__":
    main()
