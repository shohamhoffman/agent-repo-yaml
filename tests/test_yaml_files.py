"""
Test suite for YAML file validation in the agent-repo-yaml repository.

This module tests:
- YAML file syntax and format validation
- YAML content structure
- File existence and accessibility
"""

import os
import pytest
import yaml


# Get the repository root directory
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YAMLS_DIR = os.path.join(REPO_ROOT, 'yamls')


class TestYAMLFiles:
    """Test cases for YAML files in the repository."""
    
    def test_yamls_directory_exists(self):
        """Test that the yamls directory exists."""
        assert os.path.exists(YAMLS_DIR), "yamls directory should exist"
        assert os.path.isdir(YAMLS_DIR), "yamls should be a directory"
    
    def test_yamls_directory_not_empty(self):
        """Test that the yamls directory contains files."""
        files = os.listdir(YAMLS_DIR)
        assert len(files) > 0, "yamls directory should not be empty"
    
    def test_first_yaml_file_exists(self):
        """Test that the 'first' YAML file exists."""
        first_file = os.path.join(YAMLS_DIR, 'first')
        assert os.path.exists(first_file), "'first' file should exist in yamls directory"
        assert os.path.isfile(first_file), "'first' should be a file, not a directory"
    
    def test_first_yaml_file_readable(self):
        """Test that the 'first' YAML file is readable."""
        first_file = os.path.join(YAMLS_DIR, 'first')
        with open(first_file, 'r') as f:
            content = f.read()
        assert content is not None, "'first' file should have readable content"
    
    def test_first_yaml_file_not_empty(self):
        """Test that the 'first' YAML file is not empty."""
        first_file = os.path.join(YAMLS_DIR, 'first')
        with open(first_file, 'r') as f:
            content = f.read().strip()
        assert len(content) > 0, "'first' file should not be empty"
    
    def test_first_yaml_content(self):
        """Test that the 'first' YAML file contains expected content."""
        first_file = os.path.join(YAMLS_DIR, 'first')
        with open(first_file, 'r') as f:
            content = f.read().strip()
        assert content == 'test', "'first' file should contain 'test'"
    
    def test_yaml_files_have_valid_encoding(self):
        """Test that YAML files can be read with UTF-8 encoding."""
        first_file = os.path.join(YAMLS_DIR, 'first')
        try:
            with open(first_file, 'r', encoding='utf-8') as f:
                content = f.read()
            assert True, "File should be readable with UTF-8 encoding"
        except UnicodeDecodeError:
            pytest.fail("File should be readable with UTF-8 encoding")


class TestYAMLSyntax:
    """Test cases for YAML syntax validation."""
    
    def test_first_file_yaml_parseable(self):
        """Test that the 'first' file can be parsed as YAML (plain text is valid YAML)."""
        first_file = os.path.join(YAMLS_DIR, 'first')
        with open(first_file, 'r') as f:
            try:
                data = yaml.safe_load(f)
                # Plain text 'test' should be parsed as a string
                assert data is not None, "YAML content should parse successfully"
            except yaml.YAMLError as e:
                pytest.fail(f"File should be valid YAML: {e}")
    
    def test_yaml_structure_type(self):
        """Test that parsed YAML has expected type."""
        first_file = os.path.join(YAMLS_DIR, 'first')
        with open(first_file, 'r') as f:
            data = yaml.safe_load(f)
        # 'test' as plain text YAML should parse as a string
        assert isinstance(data, str), "Parsed YAML should be a string"
        assert data == 'test', "Parsed YAML should equal 'test'"


class TestYAMLFileStructure:
    """Test cases for YAML directory and file structure."""
    
    def test_yamls_directory_permissions(self):
        """Test that the yamls directory has read permissions."""
        assert os.access(YAMLS_DIR, os.R_OK), "yamls directory should be readable"
    
    def test_first_file_permissions(self):
        """Test that the 'first' file has read permissions."""
        first_file = os.path.join(YAMLS_DIR, 'first')
        assert os.access(first_file, os.R_OK), "'first' file should be readable"
    
    def test_no_hidden_files_in_yamls(self):
        """Test that there are no hidden files in yamls directory."""
        files = os.listdir(YAMLS_DIR)
        hidden_files = [f for f in files if f.startswith('.')]
        assert len(hidden_files) == 0, "yamls directory should not contain hidden files"
    
    def test_yaml_file_size_reasonable(self):
        """Test that YAML files are not unreasonably large."""
        first_file = os.path.join(YAMLS_DIR, 'first')
        size = os.path.getsize(first_file)
        # Assuming YAML files should be less than 1MB
        assert size < 1024 * 1024, "YAML file should be less than 1MB"
