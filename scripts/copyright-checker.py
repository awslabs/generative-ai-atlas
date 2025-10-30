# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.  
# SPDX-License-Identifier: MIT-0

import os
import re
import sys

def get_desired_copyright():
    """Return the desired copyright statement"""
    return """<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->"""

def extract_existing_copyright(content):
    """Extract existing copyright comment from the beginning of the file"""
    # Look for HTML comment at the start of the file (allowing for whitespace)
    pattern = r'^\s*(<!--\s*\n?\s*Copyright.*?-->\s*\n?)'
    match = re.match(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def find_first_h1_position(content):
    """Find the position of the first H1 header"""
    # Look for first H1 header (# at start of line)
    pattern = r'^#\s+.+$'
    match = re.search(pattern, content, re.MULTILINE)
    if match:
        return match.start()
    return len(content)  # If no H1 found, add at the end

def add_or_replace_copyright(content):
    """Add or replace copyright statement in markdown content"""
    desired_copyright = get_desired_copyright()
    existing_copyright = extract_existing_copyright(content)
    
    # If copyright exists and matches desired format, no changes needed
    if existing_copyright:
        # Normalize whitespace for comparison
        existing_normalized = re.sub(r'\s+', ' ', existing_copyright.strip())
        desired_normalized = re.sub(r'\s+', ' ', desired_copyright.strip())
        
        if existing_normalized == desired_normalized:
            return content, False  # No changes needed
        
        # Remove existing copyright
        content = re.sub(r'^\s*<!--\s*\n?\s*Copyright.*?-->\s*\n?', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Find position to insert copyright (before first H1)
    h1_position = find_first_h1_position(content)
    
    # Insert copyright at the appropriate position
    if h1_position == 0:
        # First H1 is at the very beginning
        new_content = desired_copyright + '\n\n' + content
    elif h1_position == len(content):
        # No H1 found, add at the beginning
        new_content = desired_copyright + '\n\n' + content
    else:
        # Insert before the first H1
        before_h1 = content[:h1_position].rstrip()
        from_h1 = content[h1_position:]
        
        if before_h1:
            new_content = desired_copyright + '\n\n' + before_h1 + '\n\n' + from_h1
        else:
            new_content = desired_copyright + '\n\n' + from_h1
    
    return new_content, True

def process_markdown_files(path):
    """Process all markdown files in the given directory or single file"""
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        sys.exit(1)
    
    processed_count = 0
    total_count = 0
    
    # Handle single file
    if os.path.isfile(path) and path.lower().endswith('.md'):
        total_count = 1
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified_content, was_modified = add_or_replace_copyright(content)
            
            if was_modified:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                print(f"Updated copyright in: {path}")
                processed_count += 1
            else:
                print(f"Copyright already correct in: {path}")
                
        except Exception as e:
            print(f"Error processing {path}: {str(e)}")
    
    # Handle directory
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.md'):
                    total_count += 1
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        modified_content, was_modified = add_or_replace_copyright(content)
                        
                        if was_modified:
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(modified_content)
                            print(f"Updated copyright in: {file_path}")
                            processed_count += 1
                        else:
                            print(f"Copyright already correct in: {file_path}")
                        
                    except Exception as e:
                        print(f"Error processing {file_path}: {str(e)}")
    else:
        print(f"Error: '{path}' is not a markdown file or directory.")
        sys.exit(1)
    
    print(f"\nProcessing complete! Updated {processed_count} out of {total_count} markdown files.")

def main():
    """Main function"""
    path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    print(f"Processing markdown files in: {path}")
    print(f"Looking for copyright statement:\n{get_desired_copyright()}\n")
    process_markdown_files(path)

if __name__ == "__main__":
    main()