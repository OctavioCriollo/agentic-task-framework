"""
Tests for ProjectManager class.
"""

import pytest
from pathlib import Path
from core.project_manager import (
    ProjectManager,
    OutputNotFoundError,
    InvalidOutputError,
    DuplicateReportError
)


class TestProjectCreation:
    """Tests for project creation functionality."""

    def test_create_project_basic(self, project_manager):
        """Test basic project creation."""
        project = project_manager.create_project(
            name="Test Project",
            user_request="Test request",
            context="Test context"
        )

        assert project['name'] == "Test Project"
        assert project['user_request'] == "Test request"
        assert project['context'] == "Test context"
        assert 'id' in project
        assert 'created' in project
        assert project['status'] == 'in_progress'

    def test_create_project_structure(self, project_manager, sample_project):
        """Test that project directory structure is created."""
        project_id = sample_project['id']
        project_dir = project_manager.base_dir / project_id

        assert project_dir.exists()
        assert (project_dir / "project_info.json").exists()
        assert (project_dir / "context.md").exists()
        assert (project_dir / "tasks").exists()
        assert (project_dir / "synthesis").exists()


class TestTaskCreation:
    """Tests for task creation functionality."""

    def test_create_task_basic(self, project_manager, sample_project, valid_prompt):
        """Test basic task creation."""
        project_id = sample_project['id']

        task = project_manager.create_task(
            project_id=project_id,
            task_name="test-task",
            task_description="Test task description",
            prompt=valid_prompt
        )

        assert task['task_name'] == "test-task"
        assert task['description'] == "Test task description"
        assert task['status'] == 'in_progress'
        assert 'created' in task

    def test_create_task_structure_v22(self, project_manager, sample_project, valid_prompt):
        """Test that task follows v2.2 ORGANIZED structure."""
        project_id = sample_project['id']

        project_manager.create_task(
            project_id=project_id,
            task_name="test-task",
            task_description="Test",
            prompt=valid_prompt
        )

        task_dir = project_manager.base_dir / project_id / "tasks" / "test-task"

        # v2.2 ORGANIZED requirements
        assert (task_dir / "task_info.json").exists()
        assert (task_dir / "prompt.md").exists()
        assert (task_dir / "README.md").exists()
        assert (task_dir / "reports").exists()
        assert (task_dir / "reports").is_dir()

    def test_get_task_report_path_returns_reports_subdir(self, project_manager, sample_project, valid_prompt):
        """Test that get_task_report_path returns path in reports/ subdirectory."""
        project_id = sample_project['id']

        project_manager.create_task(
            project_id=project_id,
            task_name="test-task",
            task_description="Test",
            prompt=valid_prompt
        )

        report_path = project_manager.get_task_report_path(
            project_id=project_id,
            task_name="test-task",
            report_filename="test_report.md"
        )

        # Should return path in reports/ subdirectory
        assert "reports" in report_path
        assert report_path.endswith("test_report.md")


class TestTaskReportRegistration:
    """Tests for task report registration with validation."""

    def test_register_report_validates_existence(self, project_manager, sample_project, valid_prompt):
        """Test that register_task_report validates file exists."""
        project_id = sample_project['id']

        project_manager.create_task(
            project_id=project_id,
            task_name="test-task",
            task_description="Test",
            prompt=valid_prompt
        )

        # Should raise OutputNotFoundError if file doesn't exist
        with pytest.raises(OutputNotFoundError):
            project_manager.register_task_report(
                project_id=project_id,
                task_name="test-task",
                report_filename="nonexistent.md"
            )

    def test_register_report_validates_content(self, project_manager, sample_project, valid_prompt):
        """Test that register_task_report validates content length."""
        project_id = sample_project['id']

        project_manager.create_task(
            project_id=project_id,
            task_name="test-task",
            task_description="Test",
            prompt=valid_prompt
        )

        # Create report with minimal content (< 100 chars)
        report_path_str = project_manager.get_task_report_path(
            project_id=project_id,
            task_name="test-task",
            report_filename="short.md"
        )
        Path(report_path_str).write_text("Too short", encoding='utf-8')

        # Should raise InvalidOutputError if content < 100 chars
        with pytest.raises(InvalidOutputError):
            project_manager.register_task_report(
                project_id=project_id,
                task_name="test-task",
                report_filename="short.md"
            )

    def test_register_report_detects_duplicates(self, project_manager, sample_project, valid_prompt):
        """Test that register_task_report detects duplicate registrations."""
        project_id = sample_project['id']

        project_manager.create_task(
            project_id=project_id,
            task_name="test-task",
            task_description="Test",
            prompt=valid_prompt
        )

        # Create valid report
        report_path_str = project_manager.get_task_report_path(
            project_id=project_id,
            task_name="test-task",
            report_filename="test.md"
        )
        Path(report_path_str).write_text("A" * 150, encoding='utf-8')

        # Register first time - should succeed
        project_manager.register_task_report(
            project_id=project_id,
            task_name="test-task",
            report_filename="test.md"
        )

        # Register second time - should raise DuplicateReportError
        with pytest.raises(DuplicateReportError):
            project_manager.register_task_report(
                project_id=project_id,
                task_name="test-task",
                report_filename="test.md"
            )

    def test_register_report_success(self, project_manager, sample_project, valid_prompt):
        """Test successful report registration."""
        project_id = sample_project['id']

        project_manager.create_task(
            project_id=project_id,
            task_name="test-task",
            task_description="Test",
            prompt=valid_prompt
        )

        # Create valid report
        report_path_str = project_manager.get_task_report_path(
            project_id=project_id,
            task_name="test-task",
            report_filename="test.md"
        )
        Path(report_path_str).write_text("A" * 150, encoding='utf-8')

        # Should succeed
        task_info = project_manager.register_task_report(
            project_id=project_id,
            task_name="test-task",
            report_filename="test.md"
        )

        assert "reports/test.md" in task_info['reports']


class TestTaskStatusManagement:
    """Tests for task status management."""

    def test_update_task_status(self, project_manager, sample_project, valid_prompt):
        """Test updating task status."""
        project_id = sample_project['id']

        project_manager.create_task(
            project_id=project_id,
            task_name="test-task",
            task_description="Test",
            prompt=valid_prompt
        )

        # Update to completed
        project_manager.update_task_status(
            project_id=project_id,
            task_name="test-task",
            status="completed"
        )

        # Verify status changed
        project_info = project_manager.get_project_info(project_id)
        assert project_info['tasks']['test-task']['status'] == 'completed'
        assert 'completed_at' in project_info['tasks']['test-task']

    def test_update_task_status_invalid(self, project_manager, sample_project, valid_prompt):
        """Test that invalid status raises ValueError."""
        project_id = sample_project['id']

        project_manager.create_task(
            project_id=project_id,
            task_name="test-task",
            task_description="Test",
            prompt=valid_prompt
        )

        # Should raise ValueError for invalid status
        with pytest.raises(ValueError):
            project_manager.update_task_status(
                project_id=project_id,
                task_name="test-task",
                status="invalid_status"
            )


class TestInputValidation:
    """Test suite for input parameter validation (SECURITY FIX)."""

    # Project creation validation
    def test_reject_empty_project_name(self, project_manager):
        """Reject empty project name."""
        with pytest.raises(ValueError, match="cannot be empty"):
            project_manager.create_project(name="", user_request="test")

    def test_reject_whitespace_only_project_name(self, project_manager):
        """Reject whitespace-only project name."""
        with pytest.raises(ValueError, match="cannot be empty"):
            project_manager.create_project(name="   ", user_request="test")

    def test_reject_empty_user_request(self, project_manager):
        """Reject empty user request."""
        with pytest.raises(ValueError, match="cannot be empty"):
            project_manager.create_project(name="test", user_request="")

    def test_reject_forbidden_chars_in_project_name(self, project_manager):
        """Reject forbidden characters in project name."""
        with pytest.raises(ValueError, match="forbidden characters"):
            project_manager.create_project(
                name="test<script>",
                user_request="test request"
            )

    def test_reject_forbidden_chars_in_user_request(self, project_manager):
        """Reject forbidden characters in user request."""
        forbidden_chars = ['<', '>', '|', ':', '"', '*', '?']
        for char in forbidden_chars:
            with pytest.raises(ValueError, match="forbidden characters"):
                project_manager.create_project(
                    name="Valid Name",
                    user_request=f"test{char}request"
                )

    def test_reject_too_long_project_name(self, project_manager):
        """Reject project names exceeding max length."""
        with pytest.raises(ValueError, match="too long"):
            project_manager.create_project(
                name="x" * 300,
                user_request="test"
            )

    def test_reject_too_long_user_request(self, project_manager):
        """Reject user requests exceeding max length."""
        with pytest.raises(ValueError, match="too long"):
            project_manager.create_project(
                name="test",
                user_request="x" * 3000
            )

    def test_reject_too_long_context(self, project_manager):
        """Reject context exceeding max length."""
        with pytest.raises(ValueError, match="too long"):
            project_manager.create_project(
                name="test",
                user_request="test request",
                context="x" * 15000
            )

    def test_reject_control_characters_in_project_name(self, project_manager):
        """Reject control characters in project name."""
        with pytest.raises(ValueError, match="control characters"):
            project_manager.create_project(
                name="test\x00name",
                user_request="test request"
            )

    # Task creation validation
    def test_reject_empty_task_name(self, project_manager, sample_project, valid_prompt):
        """Reject empty task name."""
        with pytest.raises(ValueError, match="cannot be empty"):
            project_manager.create_task(
                project_id=sample_project['id'],
                task_name="",
                task_description="test",
                prompt=valid_prompt
            )

    def test_reject_empty_task_description(self, project_manager, sample_project, valid_prompt):
        """Reject empty task description."""
        with pytest.raises(ValueError, match="cannot be empty"):
            project_manager.create_task(
                project_id=sample_project['id'],
                task_name="test-task",
                task_description="",
                prompt=valid_prompt
            )

    def test_reject_forbidden_chars_in_task_name(self, project_manager, sample_project, valid_prompt):
        """Reject forbidden characters in task name."""
        with pytest.raises(ValueError, match="forbidden characters"):
            project_manager.create_task(
                project_id=sample_project['id'],
                task_name="test<task>",
                task_description="test",
                prompt=valid_prompt
            )

    def test_reject_too_long_task_name(self, project_manager, sample_project, valid_prompt):
        """Reject task names exceeding max length."""
        with pytest.raises(ValueError, match="too long"):
            project_manager.create_task(
                project_id=sample_project['id'],
                task_name="x" * 300,
                task_description="test",
                prompt=valid_prompt
            )

    def test_reject_too_long_task_description(self, project_manager, sample_project, valid_prompt):
        """Reject task descriptions exceeding max length."""
        with pytest.raises(ValueError, match="too long"):
            project_manager.create_task(
                project_id=sample_project['id'],
                task_name="test-task",
                task_description="x" * 1500,
                prompt=valid_prompt
            )

    # Success cases
    def test_accept_valid_project_inputs(self, project_manager):
        """Accept valid project inputs."""
        project = project_manager.create_project(
            name="Valid Project Name",
            user_request="This is a valid user request"
        )
        assert project['name'] == "Valid Project Name"

    def test_accept_valid_task_inputs(self, project_manager, sample_project, valid_prompt):
        """Accept valid task inputs."""
        task = project_manager.create_task(
            project_id=sample_project['id'],
            task_name="valid-task-name",
            task_description="Valid task description",
            prompt=valid_prompt
        )
        assert task['task_name'] == "valid-task-name"

    def test_accept_special_chars_in_names(self, project_manager):
        """Accept special characters that are safe."""
        # These should be sanitized but not rejected
        # Note: Forbidden chars (<>|:"/\*?) are correctly rejected
        project = project_manager.create_project(
            name="Project (2024) - Phase 1",
            user_request="Test request with safe chars like .,!@#$%&()-+=[]{}';~"
        )
        assert project is not None


class TestPathTraversalPrevention:
    """Test suite for path traversal vulnerability prevention (SECURITY FIX)."""

    def test_reject_parent_directory_traversal(self, project_manager, sample_project, sample_task):
        """Reject report filenames with ../ sequences."""
        with pytest.raises(ValueError, match="contains '..'"):
            project_manager.register_task_report(
                project_id=sample_project['id'],
                task_name=sample_task['task_name'],
                report_filename="../../../etc/passwd"
            )

    def test_reject_absolute_path(self, project_manager, sample_project, sample_task):
        """Reject absolute paths in report filename."""
        with pytest.raises(ValueError, match="absolute path"):
            project_manager.register_task_report(
                project_id=sample_project['id'],
                task_name=sample_task['task_name'],
                report_filename="/etc/passwd"
            )

    def test_reject_windows_absolute_path(self, project_manager, sample_project, sample_task):
        """Reject Windows-style absolute paths."""
        with pytest.raises(ValueError, match="absolute path"):
            project_manager.register_task_report(
                project_id=sample_project['id'],
                task_name=sample_task['task_name'],
                report_filename="\\etc\\passwd"
            )

    def test_reject_path_separators(self, project_manager, sample_project, sample_task):
        """Reject filenames containing path separators."""
        with pytest.raises(ValueError, match="path separators"):
            project_manager.register_task_report(
                project_id=sample_project['id'],
                task_name=sample_task['task_name'],
                report_filename="subdir/report.md"
            )

    def test_reject_windows_path_separators(self, project_manager, sample_project, sample_task):
        """Reject filenames containing Windows path separators."""
        with pytest.raises(ValueError, match="path separators"):
            project_manager.register_task_report(
                project_id=sample_project['id'],
                task_name=sample_task['task_name'],
                report_filename="subdir\\report.md"
            )

    def test_reject_invalid_extension(self, project_manager, sample_project, sample_task):
        """Reject invalid file extensions."""
        with pytest.raises(ValueError, match="Invalid file extension"):
            project_manager.register_task_report(
                project_id=sample_project['id'],
                task_name=sample_task['task_name'],
                report_filename="malicious.exe"
            )

    def test_reject_empty_filename(self, project_manager, sample_project, sample_task):
        """Reject empty filenames."""
        with pytest.raises(ValueError, match="cannot be empty"):
            project_manager.register_task_report(
                project_id=sample_project['id'],
                task_name=sample_task['task_name'],
                report_filename=""
            )

    def test_reject_whitespace_only_filename(self, project_manager, sample_project, sample_task):
        """Reject whitespace-only filenames."""
        with pytest.raises(ValueError, match="cannot be empty"):
            project_manager.register_task_report(
                project_id=sample_project['id'],
                task_name=sample_task['task_name'],
                report_filename="   "
            )

    def test_reject_too_long_filename(self, project_manager, sample_project, sample_task):
        """Reject filenames exceeding 255 characters."""
        long_filename = "a" * 300 + ".md"
        with pytest.raises(ValueError, match="too long"):
            project_manager.register_task_report(
                project_id=sample_project['id'],
                task_name=sample_task['task_name'],
                report_filename=long_filename
            )

    def test_accept_valid_filename(self, project_manager, sample_project, sample_task):
        """Accept valid report filename."""
        # Setup: create actual report file
        report_path = project_manager.get_task_report_path(
            sample_project['id'],
            sample_task['task_name'],
            "valid_report.md"
        )
        Path(report_path).write_text("A" * 150, encoding='utf-8')

        # Should succeed
        project_manager.register_task_report(
            project_id=sample_project['id'],
            task_name=sample_task['task_name'],
            report_filename="valid_report.md"
        )

    def test_accept_all_valid_extensions(self, project_manager, sample_project, sample_task):
        """Accept all whitelisted file extensions."""
        valid_extensions = ['.md', '.txt', '.json', '.csv', '.html']

        for ext in valid_extensions:
            filename = f"report{ext}"
            # Create the file
            report_path = project_manager.get_task_report_path(
                sample_project['id'],
                sample_task['task_name'],
                filename
            )
            Path(report_path).write_text("A" * 150, encoding='utf-8')

            # Should succeed
            project_manager.register_task_report(
                project_id=sample_project['id'],
                task_name=sample_task['task_name'],
                report_filename=filename
            )
