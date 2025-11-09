"""
Test suite for GitHub agents configuration validation.

This module tests:
- Agent configuration file structure
- Agent metadata and schema
- Agent description and documentation
"""

import os
import pytest
import yaml


# Get the repository root directory
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS_DIR = os.path.join(REPO_ROOT, '.github', 'agents')

# Minimum content length for agent descriptions
MIN_AGENT_BODY_LENGTH = 50


class TestAgentsDirectory:
    """Test cases for .github/agents directory structure."""
    
    def test_agents_directory_exists(self):
        """Test that .github/agents directory exists."""
        assert os.path.exists(AGENTS_DIR), ".github/agents directory should exist"
        assert os.path.isdir(AGENTS_DIR), ".github/agents should be a directory"
    
    def test_agents_directory_readable(self):
        """Test that .github/agents directory is readable."""
        assert os.access(AGENTS_DIR, os.R_OK), ".github/agents directory should be readable"
    
    def test_agents_directory_has_files(self):
        """Test that .github/agents directory contains agent configuration files."""
        files = os.listdir(AGENTS_DIR)
        # Filter out hidden files and directories
        agent_files = [f for f in files if not f.startswith('.')]
        assert len(agent_files) > 0, ".github/agents directory should contain agent configuration files"


class TestAgentConfiguration:
    """Test cases for agent configuration files."""
    
    def test_agent_config_files_are_markdown(self):
        """Test that agent configuration files use .md extension."""
        files = os.listdir(AGENTS_DIR)
        agent_files = [f for f in files if not f.startswith('.')]
        for agent_file in agent_files:
            assert agent_file.endswith('.md'), f"Agent configuration file {agent_file} should have .md extension"
    
    def test_agent_config_files_readable(self):
        """Test that all agent configuration files are readable."""
        files = os.listdir(AGENTS_DIR)
        agent_files = [f for f in files if not f.startswith('.') and f.endswith('.md')]
        for agent_file in agent_files:
            file_path = os.path.join(AGENTS_DIR, agent_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            assert content is not None, f"Agent file {agent_file} should be readable"
    
    def test_agent_config_has_frontmatter(self):
        """Test that agent configuration files have YAML frontmatter."""
        files = os.listdir(AGENTS_DIR)
        agent_files = [f for f in files if not f.startswith('.') and f.endswith('.md')]
        for agent_file in agent_files:
            file_path = os.path.join(AGENTS_DIR, agent_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            assert content.startswith('---'), f"Agent file {agent_file} should start with YAML frontmatter delimiter (---)"
            # Check for closing frontmatter delimiter
            parts = content.split('---', 2)
            assert len(parts) >= 3, f"Agent file {agent_file} should have properly closed YAML frontmatter"
    
    def test_agent_frontmatter_valid_yaml(self):
        """Test that agent frontmatter is valid YAML."""
        files = os.listdir(AGENTS_DIR)
        agent_files = [f for f in files if not f.startswith('.') and f.endswith('.md')]
        for agent_file in agent_files:
            file_path = os.path.join(AGENTS_DIR, agent_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1]
                    try:
                        yaml.safe_load(frontmatter)
                    except yaml.YAMLError as e:
                        pytest.fail(f"Agent file {agent_file} has invalid YAML frontmatter: {e}")
    
    def test_agent_has_name_field(self):
        """Test that agent configuration includes a 'name' field in frontmatter."""
        files = os.listdir(AGENTS_DIR)
        agent_files = [f for f in files if not f.startswith('.') and f.endswith('.md')]
        for agent_file in agent_files:
            file_path = os.path.join(AGENTS_DIR, agent_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract and parse frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    assert 'name' in frontmatter, f"Agent file {agent_file} should have 'name' field in frontmatter"
                    assert isinstance(frontmatter['name'], str), f"Agent name in {agent_file} should be a string"
                    assert len(frontmatter['name']) > 0, f"Agent name in {agent_file} should not be empty"
    
    def test_agent_has_description_field(self):
        """Test that agent configuration includes a 'description' field in frontmatter."""
        files = os.listdir(AGENTS_DIR)
        agent_files = [f for f in files if not f.startswith('.') and f.endswith('.md')]
        for agent_file in agent_files:
            file_path = os.path.join(AGENTS_DIR, agent_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract and parse frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    assert 'description' in frontmatter, f"Agent file {agent_file} should have 'description' field in frontmatter"
                    assert isinstance(frontmatter['description'], str), f"Agent description in {agent_file} should be a string"
                    assert len(frontmatter['description']) > 0, f"Agent description in {agent_file} should not be empty"


class TestAgentContent:
    """Test cases for agent configuration content."""
    
    def test_agent_has_body_content(self):
        """Test that agent configuration files have content beyond frontmatter."""
        files = os.listdir(AGENTS_DIR)
        agent_files = [f for f in files if not f.startswith('.') and f.endswith('.md')]
        for agent_file in agent_files:
            file_path = os.path.join(AGENTS_DIR, agent_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract body content (after frontmatter)
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    body = parts[2].strip()
                    assert len(body) > 0, f"Agent file {agent_file} should have body content after frontmatter"
    
    def test_agent_body_is_descriptive(self):
        """Test that agent body content is reasonably descriptive."""
        files = os.listdir(AGENTS_DIR)
        agent_files = [f for f in files if not f.startswith('.') and f.endswith('.md')]
        for agent_file in agent_files:
            file_path = os.path.join(AGENTS_DIR, agent_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract body content
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    body = parts[2].strip()
                    # Should have at least MIN_AGENT_BODY_LENGTH characters of meaningful content
                    assert len(body) > MIN_AGENT_BODY_LENGTH, f"Agent file {agent_file} should have descriptive body content (at least {MIN_AGENT_BODY_LENGTH} characters)"
    
    def test_agent_name_format(self):
        """Test that agent names follow a consistent format (lowercase with hyphens)."""
        files = os.listdir(AGENTS_DIR)
        agent_files = [f for f in files if not f.startswith('.') and f.endswith('.md')]
        for agent_file in agent_files:
            file_path = os.path.join(AGENTS_DIR, agent_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract and parse frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    if 'name' in frontmatter:
                        name = frontmatter['name']
                        # Check that name has no uppercase letters
                        assert name == name.lower(), \
                            f"Agent name '{name}' in {agent_file} should be all lowercase"
                        # Check no spaces
                        assert ' ' not in name, \
                            f"Agent name '{name}' in {agent_file} should not contain spaces"
