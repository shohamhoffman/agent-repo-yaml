"""
Test suite for repository structure and configuration files.

This module tests:
- Repository file structure
- README file existence and basic content
- Directory organization
"""

import os
import pytest


# Get the repository root directory
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestRepositoryStructure:
    """Test cases for repository structure and organization."""
    
    def test_readme_exists(self):
        """Test that README.md file exists in the repository root."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        assert os.path.exists(readme_path), "README.md should exist in repository root"
    
    def test_readme_is_file(self):
        """Test that README.md is a file, not a directory."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        assert os.path.isfile(readme_path), "README.md should be a file"
    
    def test_readme_readable(self):
        """Test that README.md is readable."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        with open(readme_path, 'r') as f:
            content = f.read()
        assert content is not None, "README.md should be readable"
    
    def test_readme_not_empty(self):
        """Test that README.md is not empty."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        with open(readme_path, 'r') as f:
            content = f.read().strip()
        assert len(content) > 0, "README.md should not be empty"
    
    def test_readme_utf8_encoding(self):
        """Test that README.md uses UTF-8 encoding."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
            assert True, "README.md should be readable with UTF-8 encoding"
        except UnicodeDecodeError:
            pytest.fail("README.md should use UTF-8 encoding")
    
    def test_yamls_directory_exists(self):
        """Test that yamls directory exists."""
        yamls_dir = os.path.join(REPO_ROOT, 'yamls')
        assert os.path.exists(yamls_dir), "yamls directory should exist"
        assert os.path.isdir(yamls_dir), "yamls should be a directory"
    
    def test_github_directory_exists(self):
        """Test that .github directory exists."""
        github_dir = os.path.join(REPO_ROOT, '.github')
        assert os.path.exists(github_dir), ".github directory should exist"
        assert os.path.isdir(github_dir), ".github should be a directory"


class TestREADMEContent:
    """Test cases for README.md content validation."""
    
    def test_readme_has_content(self):
        """Test that README.md contains some text content."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        with open(readme_path, 'r') as f:
            content = f.read()
        # Should have at least some characters
        assert len(content.strip()) > 0, "README should have content"
    
    def test_readme_content_is_text(self):
        """Test that README.md contains text (not binary data)."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        with open(readme_path, 'rb') as f:
            content = f.read()
        try:
            content.decode('utf-8')
            assert True, "README should be text, not binary"
        except UnicodeDecodeError:
            pytest.fail("README should contain valid text")
    
    def test_readme_line_count(self):
        """Test that README.md has at least one line."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        with open(readme_path, 'r') as f:
            lines = f.readlines()
        assert len(lines) > 0, "README should have at least one line"


class TestDirectoryStructure:
    """Test cases for directory organization."""
    
    def test_root_contains_expected_items(self):
        """Test that repository root contains expected files and directories."""
        expected_items = ['README.md', 'yamls', '.github']
        for item in expected_items:
            item_path = os.path.join(REPO_ROOT, item)
            assert os.path.exists(item_path), f"{item} should exist in repository root"
    
    def test_no_unexpected_top_level_files(self):
        """Test that there are no unexpected files in the repository root."""
        # Get all items in root
        items = os.listdir(REPO_ROOT)
        # Filter out .git and other expected items
        unexpected = [
            item for item in items 
            if item not in ['.git', '.github', 'README.md', 'yamls', 'requirements.txt', 'tests', '__pycache__', '.pytest_cache', 'pytest.ini', '.gitignore', 'TESTING.md', '.coverage', 'htmlcov', 'coverage.xml']
        ]
        # Note: This is a loose test - adjust based on actual repository needs
        assert len(unexpected) == 0 or all(item.startswith('.') for item in unexpected), \
            f"Unexpected files in repository root: {unexpected}"
    
    def test_directory_permissions(self):
        """Test that directories have proper read/execute permissions."""
        directories = [
            os.path.join(REPO_ROOT, 'yamls'),
            os.path.join(REPO_ROOT, '.github'),
        ]
        for directory in directories:
            if os.path.exists(directory):
                assert os.access(directory, os.R_OK), f"{directory} should be readable"
                assert os.access(directory, os.X_OK), f"{directory} should be executable (accessible)"


class TestFilePermissions:
    """Test cases for file permissions and accessibility."""
    
    def test_readme_permissions(self):
        """Test that README.md has read permissions."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        assert os.access(readme_path, os.R_OK), "README.md should be readable"
    
    def test_yaml_directory_accessible(self):
        """Test that yamls directory is accessible."""
        yamls_dir = os.path.join(REPO_ROOT, 'yamls')
        assert os.access(yamls_dir, os.R_OK), "yamls directory should be readable"
        assert os.access(yamls_dir, os.X_OK), "yamls directory should be accessible"
