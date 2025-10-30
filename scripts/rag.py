# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.  
# SPDX-License-Identifier: MIT-0

import os
import sys
import re
import hashlib
import shutil
import zipfile
import argparse
import json
from datetime import datetime
from git import Repo, InvalidGitRepositoryError

def get_h1_header(file_path):
    """Extract the first H1 header from a markdown file if present."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for # Header pattern
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                return match.group(1).strip()
    except Exception as e:
        print(f"Warning: Could not read header from {file_path}: {e}")
    return None

def get_content_level(file_path):
    """Extract the content-level from a markdown file if present."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Read only the first 30 lines to focus on the top of the document
            first_lines = ''.join([next(f) for _ in range(30) if f])
            
            # Try different patterns for content level
            patterns = [
                # Bold markdown syntax: **Content Level: 200**
                r'\*\*\s*Content\s*Level\s*:\s*(\d+)\s*\*\*',
                # Regular text with "content-level: 100"
                r'content-level\s*:\s*(\d+)',
                # Regular text with "Content Level: 100"
                r'Content\s*Level\s*:\s*(\d+)',
                # Just the level number after "level" or "level:"
                r'level\s*:?\s*(\d+)'
            ]
            
            for pattern in patterns:
                match = re.search(pattern, first_lines, re.IGNORECASE)
                if match:
                    return int(match.group(1))
    except Exception as e:
        print(f"Warning: Could not read content-level from {file_path}: {e}")
    
    # Default level if not found
    return 100

def sanitize_filename(name):
    """Convert spaces and non-alphanumeric chars to underscores."""
    if not name:
        return None
    # Replace non-alphanumeric characters with underscores
    return re.sub(r'[^a-zA-Z0-9]', '_', name)

def extract_numeric_prefix(directory_path, source_dir):
    """
    Extract numeric prefix from directory path.
    Starts from the top-level directory and works down to find the best numeric prefix.
    Returns the formatted numeric prefix (e.g., '2.3.4') with at least 2 numbers.
    """
    try:
        # Get the relative path from source_dir to the file's directory
        rel_path = os.path.relpath(directory_path, source_dir)
        if rel_path == '.':
            return None  # File is directly in source_dir, no directory structure to analyze
        
        # Split the path into components
        path_components = []
        current_dir = directory_path
        
        # Build the list of directory names from bottom to top
        while os.path.normpath(current_dir) != os.path.normpath(source_dir):
            path_components.insert(0, os.path.basename(current_dir))
            current_dir = os.path.dirname(current_dir)
        
        # Now process from top to bottom
        best_prefix = None
        best_num_count = 0
        
        for i in range(len(path_components)):
            # Build path up to this component
            current_path = path_components[:i+1]
            dir_name = current_path[-1]
            
            # Look for numeric patterns at the beginning of the directory name
            match = re.match(r'^(\d+[_\-\d]+)', dir_name)
            if match:
                # Extract the numeric part
                numeric_part = match.group(1)
                # Replace all non-alphanumeric characters with periods
                formatted_prefix = re.sub(r'[^0-9]', '.', numeric_part)
                
                # Count the number of numeric components
                num_count = formatted_prefix.count('.') + 1
                
                # Only consider prefixes with at least 2 numbers
                if num_count >= 2 and num_count >= best_num_count:
                    best_prefix = formatted_prefix
                    best_num_count = num_count
                # If we find fewer numbers than before, stop
                elif best_prefix and num_count < best_num_count:
                    break
        
        return best_prefix
    except Exception as e:
        print(f"Warning: Error extracting numeric prefix: {e}")
        return None

def hash_directory(directory):
    """Create a short hash of the directory path (fallback if no numeric prefix)."""
    return hashlib.sha256(directory.encode('utf-8')).hexdigest()[:8]

def get_git_last_modified(file_path):
    """
    Get the last modified date of a file from git history.
    Returns the date in ISO 8601 format, or None if git info is unavailable.
    """
    try:
        # Find the git repository for this file
        repo = Repo(file_path, search_parent_directories=True)
        
        # Get the relative path from the repo root
        repo_root = repo.working_dir
        rel_path = os.path.relpath(file_path, repo_root)
        
        # Get commits that modified this file
        commits = list(repo.iter_commits(paths=rel_path, max_count=1))
        
        if commits:
            # Get the most recent commit that modified this file
            last_commit = commits[0]
            # Convert commit date to ISO 8601 format
            commit_date = datetime.fromtimestamp(last_commit.authored_date)
            return commit_date.strftime('%Y-%m-%dT%H:%M:%S+00:00')
        else:
            # File has no git history (new/untracked file)
            return None
            
    except (InvalidGitRepositoryError, Exception) as e:
        # File is not in a git repository or other git-related error
        print(f"Warning: Could not get git info for {file_path}: {e}")
        return None

def create_metadata_file(md_file_path, metadata_file_path, title, source_dir):
    """Create a metadata file for the corresponding markdown file."""
    # Get content level
    level = get_content_level(md_file_path)
    
    # Get last modified date from git, fallback to current date
    created_at = get_git_last_modified(md_file_path)
    if created_at is None:
        # Fallback to current date if git info is unavailable
        created_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')
        creation_date = datetime.now().strftime('%Y-%m-%d')
    else:
        # Extract date part from created_at for creation_date (YYYY-MM-DD format)
        creation_date = created_at[:10]  # Extract YYYY-MM-DD from YYYY-MM-DDTHH:MM:SS+00:00

    # Get the filename and change extension from .md to .html
    md_filename = os.path.basename(md_file_path)
    html_filename = os.path.splitext(md_filename)[0] + ".html"
    
    # Create source URI from directory structure
    rel_path = os.path.relpath(os.path.dirname(md_file_path), source_dir)
    
    # Base URI without topics
    base_uri = "https://awslabs.github.io/generative-ai-atlas/topics"
    
    if rel_path == '.':
        source_uri = f"{base_uri}/{html_filename}"
    else:
        # Replace backslashes with forward slashes for Windows compatibility
        rel_path = rel_path.replace('\\', '/')
        
        # Check if rel_path already starts with "topics/" and remove it if it does
        if rel_path.startswith("topics/"):
            rel_path = rel_path[7:]  # Remove "topics/" prefix
            
        source_uri = f"{base_uri}/{rel_path}/{html_filename}"
    
    # Create metadata object with the new structure
    metadata = {
        "Title": title if title else os.path.splitext(os.path.basename(md_file_path))[0],
        "ContentType": "MD",
        "Attributes": {
            "type": "Other code repo",
            "creation_date": creation_date,
            "_version": 1,
            "level": f"level-{level}",
            "_source_uri": source_uri,
            "_created_at": created_at
        }
    }
    
    # Write metadata to file
    with open(metadata_file_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Created metadata: {metadata_file_path}")
        
def main():
    parser = argparse.ArgumentParser(description='Consolidate markdown files into a rag directory and zip them.')
    parser.add_argument('directory', nargs='?', default=os.getcwd(),
                        help='Directory to search for .md files (default: current directory)')
    parser.add_argument('zip_destination', nargs='?', default=os.getcwd(),
                        help='Directory where the zip file will be saved (default: current directory)')
    args = parser.parse_args()
    
    source_dir = args.directory
    zip_dest = args.zip_destination
    
    # Ensure source directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: {source_dir} is not a valid directory")
        sys.exit(1)
    
    # Create zip destination directory if it doesn't exist
    if not os.path.exists(zip_dest):
        print(f"Creating zip destination directory: {zip_dest}")
        os.makedirs(zip_dest)
    
    # Create rag directory if it doesn't exist, or clean it if it does
    rag_dir = os.path.join(os.getcwd(), "rag")
    if os.path.exists(rag_dir):
        print(f"Cleaning existing rag directory: {rag_dir}")
        # Remove all files in the rag directory
        for item in os.listdir(rag_dir):
            item_path = os.path.join(rag_dir, item)
            if os.path.isfile(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
    else:
        print(f"Creating rag directory: {rag_dir}")
        os.makedirs(rag_dir)
    
    # Find all .md files
    md_files = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    if not md_files:
        print(f"No .md files found in {source_dir}")
        sys.exit(0)
    
    print(f"Found {len(md_files)} markdown files")
    
    # Process each file
    used_filenames = set()
    for file_path in md_files:
        # Get numeric prefix from directory structure
        dir_path = os.path.dirname(file_path)
        numeric_prefix = extract_numeric_prefix(dir_path, source_dir)
        
        # Try to get H1 header for filename
        h1_header = get_h1_header(file_path)
        if h1_header:
            base_name = sanitize_filename(h1_header)
        else:
            # Use original filename if no H1 header
            base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Create unique filename with numeric prefix if available, otherwise use hash
        if numeric_prefix:
            # Ensure there's no trailing period before the underscore
            if numeric_prefix.endswith('.'):
                numeric_prefix = numeric_prefix[:-1]
            new_filename = f"{numeric_prefix}_{base_name}.md"
        else:
            # Fallback to using hash if no numeric prefix found
            dir_hash = hash_directory(os.path.dirname(file_path))
            new_filename = f"{dir_hash}_{base_name}.md"
        
        # Ensure filename is unique
        counter = 1
        test_filename = new_filename
        while test_filename in used_filenames:
            test_filename = f"{os.path.splitext(new_filename)[0]}_{counter}.md"
            counter += 1
        
        new_filename = test_filename
        used_filenames.add(new_filename)
        
        # Copy file to rag directory
        dest_path = os.path.join(rag_dir, new_filename)
        shutil.copy2(file_path, dest_path)
        print(f"Copied: {file_path} -> {dest_path}")
        
        # Create metadata file
        metadata_filename = os.path.splitext(new_filename)[0] + ".md.metadata.json"
        metadata_path = os.path.join(rag_dir, metadata_filename)
        create_metadata_file(file_path, metadata_path, h1_header, source_dir)
    
    # Create zip file in the specified destination
    zip_path = os.path.join(zip_dest, "rag.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(rag_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Add file to zip with relative path
                zipf.write(file_path, os.path.relpath(file_path, os.path.dirname(rag_dir)))
    
    print(f"\nProcess complete!")
    print(f"- {len(used_filenames)} files consolidated in: {rag_dir}")
    print(f"- {len(used_filenames)} metadata files created")
    print(f"- All files zipped to: {zip_path}")

if __name__ == "__main__":
    main()
