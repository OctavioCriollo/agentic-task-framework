"""
Pytest configuration and fixtures for test suite.
"""

import pytest
import tempfile
import shutil
from pathlib import Path
from core.project_manager import ProjectManager


@pytest.fixture
def temp_projects_dir():
    """Create temporary directory for test projects."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    # Cleanup after test
    shutil.rmtree(temp_dir)


@pytest.fixture
def project_manager(temp_projects_dir):
    """Create ProjectManager instance with temporary directory."""
    return ProjectManager(base_dir=str(temp_projects_dir), log_level='ERROR')


@pytest.fixture
def sample_project(project_manager):
    """Create a sample project for testing."""
    project = project_manager.create_project(
        name="Test Project",
        user_request="Test user request",
        context="Test context"
    )
    return project


@pytest.fixture
def valid_prompt():
    """Generate a valid 2-layer prompt for testing (> 500 chars)."""
    return """# Test Task

## Layer 1: Conversational Context

The user has requested a test investigation as part of testing the Agentic Task Framework v2.2.
This is a controlled test environment for validating the framework's functionality.

**Context:**
- Test project created for validation purposes
- Supervised test execution
- Academic testing framework
- No real-world impact

This test is designed to verify that the framework correctly handles task creation,
report generation, and validation workflows. All outputs should be validated against
the v2.2 ORGANIZED standard.

## Layer 2: Technical Task

**Objective:** Generate a test report validating framework functionality.

**Methodology:**
1. Verify task structure creation
2. Generate report in reports/ subdirectory
3. Validate metadata registration
4. Ensure v2.2 ORGANIZED compliance

**Expected Outputs:**
- Test report in Markdown format
- Minimum 150 characters content
- Located in reports/ subdirectory

**Success Criteria:**
- Report file created successfully
- Content meets minimum length requirements
- Metadata correctly registered
- No validation errors
"""


@pytest.fixture
def sample_task(project_manager, sample_project, valid_prompt):
    """Create a sample task for testing."""
    task = project_manager.create_task(
        project_id=sample_project['id'],
        task_name="test-task",
        task_description="Test task description",
        prompt=valid_prompt
    )
    return task
