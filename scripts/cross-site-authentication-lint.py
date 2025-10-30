# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.  
# SPDX-License-Identifier: MIT-0

import os
import sys
from bs4 import BeautifulSoup
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

class LintLevel(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"

@dataclass
class LintIssue:
    file: Path
    href: str
    message: str
    level: LintLevel
    line_number: Optional[int] = None

class HTMLAnchorLinter:
    def __init__(self, directory: str):
        self.directory = Path(directory)
        self.html_extensions = {'.html', '.htm'}
        self.issues: List[LintIssue] = []
        self.files_processed = 0
        self.files_with_issues = 0

    def lint_anchors(self, html_content: str, file_path: Path) -> List[LintIssue]:
        """Analyze HTML content and detect anchor tag issues."""
        issues = []
        soup = BeautifulSoup(html_content, 'html.parser')
        
        for anchor in soup.find_all('a', href=True):
            href = anchor.get('href')
            
            if href.startswith(('http://', 'https://')):
                # Check target attribute
                if anchor.get('target') != '_blank':
                    issues.append(LintIssue(
                        file=file_path,
                        href=href,
                        message='External link missing target="_blank"',
                        level=LintLevel.WARNING
                    ))
                
                # Check rel attribute
                rel = anchor.get('rel', [])
                rel = rel if isinstance(rel, list) else rel.split()
                if not ('noopener' in rel and 'noreferrer' in rel):
                    issues.append(LintIssue(
                        file=file_path,
                        href=href,
                        message='External link missing rel="noopener noreferrer"',
                        level=LintLevel.ERROR  # Security issue, so mark as error
                    ))
        
        return issues

    def lint_file(self, file_path: Path) -> None:
        """Lint a single HTML file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            self.files_processed += 1
            file_issues = self.lint_anchors(html_content, file_path)
            
            if file_issues:
                self.files_with_issues += 1
                self.issues.extend(file_issues)
                    
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}", file=sys.stderr)

    def lint_directory(self, directory: Path) -> None:
        """Recursively lint HTML files in the directory."""
        try:
            for item in directory.iterdir():
                if item.is_file() and item.suffix.lower() in self.html_extensions:
                    self.lint_file(item)
                elif item.is_dir():
                    self.lint_directory(item)
                    
        except Exception as e:
            print(f"Error accessing directory {directory}: {str(e)}", file=sys.stderr)

    def print_report(self) -> None:
        """Print lint results in a formatted report."""
        print("\nHTML Anchor Lint Report")
        print("=" * 50)
        print(f"Files processed: {self.files_processed}")
        print(f"Files with issues: {self.files_with_issues}")
        print(f"Total issues found: {len(self.issues)}")
        print("=" * 50)

        if self.issues:
            current_file = None
            for issue in sorted(self.issues, key=lambda x: (x.file, x.level.value)):
                if current_file != issue.file:
                    current_file = issue.file
                    print(f"\n{issue.file}:")
                print(f"  [{issue.level.value.upper()}] {issue.message}")
                print(f"    at href: {issue.href}")

    def run(self) -> int:
        """Main execution method. Returns exit code."""
        if not self.directory.exists() or not self.directory.is_dir():
            print("The provided path is not a valid directory.", file=sys.stderr)
            return 1
            
        print(f"Linting HTML files in: {self.directory}")
        self.lint_directory(self.directory)
        
        has_errors = any(issue.level == LintLevel.ERROR for issue in self.issues)
        
        # Always print the full report if there are any errors
        if has_errors:
            self.print_report()
            return 1
        else:
            print("No errors found.")
            return 0


def main():
    if len(sys.argv) < 2:
        print("Please provide a directory path.")
        print("Usage: python html_anchor_lint.py /path/to/directory")
        return 1
    
    linter = HTMLAnchorLinter(sys.argv[1])
    return linter.run()


if __name__ == "__main__":
    sys.exit(main())
