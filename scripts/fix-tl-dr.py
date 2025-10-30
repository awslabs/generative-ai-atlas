# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.  
# SPDX-License-Identifier: MIT-0

import os
import re
import sys

def standardize_tldr(content):
    # First, remove bold formatting and H3 headers from TL;DR
    content = re.sub(r'(?i)\*\*\s*tl;dr:?\s*\*\*', 'TL;DR:', content)
    content = re.sub(r'(?i)###\s*tl;dr:?\s*', 'TL;DR:', content)
    
    # Then, standardize all TL;DR variations
    pattern = r'(?i)(?:##?\s*)?tl;dr:?\s*'
    standardized = re.sub(pattern, '## TL;DR\n\n', content)
    return standardized

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
                    
                    modified_content = standardize_tldr(content)
                    
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
