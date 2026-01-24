"""
Agentic Task Framework - Version Information

Single source of truth for framework version.
"""

__version__ = "2.2"
__version_name__ = "ORGANIZED"
__version_full__ = f"{__version__} {__version_name__}"

# Version history
VERSION_HISTORY = {
    "1.0": "Multi-window system with task_manager.py (deprecated)",
    "2.0": "Transition to Task tool based",
    "2.2": "ORGANIZED - Standardized structure with reports/ subdirectory"
}

def get_version():
    """Get current framework version."""
    return __version__

def get_version_full():
    """Get full version string with codename."""
    return __version_full__

def get_version_info():
    """Get complete version information."""
    return {
        "version": __version__,
        "codename": __version_name__,
        "full": __version_full__,
        "history": VERSION_HISTORY
    }
