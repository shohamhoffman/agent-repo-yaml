# Test Suite Documentation

## Overview

This repository now includes a comprehensive test suite to validate the structure, content, and configuration of the agent-repo-yaml project.

## Test Structure

The test suite is organized into three main test modules:

### 1. `test_yaml_files.py` - YAML File Validation
Tests the YAML files in the `yamls/` directory:

- **TestYAMLFiles**: Basic file existence and content validation
  - Verifies `yamls/` directory exists and is not empty
  - Checks that the `first` file exists and is readable
  - Validates file content and encoding (UTF-8)
  - Ensures files are not empty

- **TestYAMLSyntax**: YAML syntax and parsing validation
  - Validates that files can be parsed as valid YAML
  - Checks parsed YAML structure and data types
  - Ensures YAML content matches expected format

- **TestYAMLFileStructure**: File structure and permissions
  - Validates directory and file permissions
  - Checks for hidden files
  - Ensures file sizes are reasonable

### 2. `test_repository_structure.py` - Repository Structure Validation
Tests the overall repository organization:

- **TestRepositoryStructure**: Core repository structure
  - Verifies README.md exists and is readable
  - Checks yamls/ directory exists
  - Validates .github/ directory structure
  - Ensures UTF-8 encoding for all text files

- **TestREADMEContent**: README content validation
  - Checks README has actual content
  - Validates text format (not binary)
  - Ensures minimum content requirements

- **TestDirectoryStructure**: Directory organization
  - Validates expected top-level items exist
  - Checks for unexpected files
  - Ensures proper directory permissions

- **TestFilePermissions**: File accessibility
  - Validates read permissions on critical files
  - Ensures directories are accessible

### 3. `test_agents_config.py` - Agent Configuration Validation
Tests GitHub agents configuration:

- **TestAgentsDirectory**: Agent directory structure
  - Verifies .github/agents/ directory exists
  - Checks directory is readable and contains files

- **TestAgentConfiguration**: Agent config file validation
  - Ensures agent files use .md extension
  - Validates YAML frontmatter structure
  - Checks for required fields (name, description)
  - Verifies frontmatter is valid YAML

- **TestAgentContent**: Agent content validation
  - Ensures agents have descriptive content
  - Validates agent naming conventions
  - Checks content length requirements

## Running Tests

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test Module
```bash
pytest tests/test_yaml_files.py -v
pytest tests/test_repository_structure.py -v
pytest tests/test_agents_config.py -v
```

### Run Tests with Coverage
```bash
pytest tests/ --cov=. --cov-report=html --cov-report=term
```

### Run Tests for Specific Test Class
```bash
pytest tests/test_yaml_files.py::TestYAMLFiles -v
```

### Run a Single Test
```bash
pytest tests/test_yaml_files.py::TestYAMLFiles::test_first_yaml_file_exists -v
```

## Continuous Integration

The repository includes a GitHub Actions workflow (`.github/workflows/test.yml`) that:
- Runs tests automatically on push and pull requests
- Tests against multiple Python versions (3.9, 3.10, 3.11, 3.12)
- Generates coverage reports
- Uploads coverage to Codecov (if configured)

## Test Coverage

The current test suite includes **40 comprehensive tests** covering:
- YAML file validation and parsing
- Repository structure and organization
- Agent configuration and metadata
- File permissions and accessibility
- Content encoding and format
- Directory structure compliance

## Adding New Tests

When adding new tests, follow these guidelines:

1. **Organize by concern**: Place tests in the appropriate module
2. **Use descriptive names**: Test names should clearly describe what they validate
3. **Include docstrings**: Every test should have a clear docstring
4. **Test one thing**: Each test should validate a single concern
5. **Be deterministic**: Tests should always produce the same result
6. **Be isolated**: Tests should not depend on each other

### Example Test Structure
```python
def test_descriptive_name(self):
    """Test that [specific behavior] works as expected."""
    # Arrange
    setup_code()
    
    # Act
    result = perform_action()
    
    # Assert
    assert result == expected, "Descriptive failure message"
```

## Dependencies

- **pytest** (>=7.4.0): Test framework
- **pyyaml** (>=6.0): YAML parsing and validation
- **pytest-cov** (>=4.1.0): Coverage reporting

## Test Configuration

Tests are configured in `pytest.ini`:
- Test discovery patterns
- Output verbosity
- Test markers (unit, integration, structure)
- Traceback format

## Missing Tests (Potential Future Additions)

While the current test suite is comprehensive for the existing repository content, consider adding:

1. **Performance tests**: Validate operation speed for large YAML files
2. **Schema validation tests**: If YAML files should follow a specific schema
3. **Integration tests**: If the repository interacts with external systems
4. **Security tests**: Validate no sensitive data in files
5. **Linting tests**: If code style/format standards are defined
6. **End-to-end tests**: If there are workflows to test
7. **API tests**: If the repository provides an API

These would be added as the repository grows and requirements become clearer.
