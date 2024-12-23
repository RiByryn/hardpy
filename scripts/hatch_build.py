"""Custom build script for hatch backend."""  # noqa: INP001

import os
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface  # type: ignore


class CustomHook(BuildHookInterface):
    """A custom build hook for nbconvert."""

    def initialize(self, version: str, build_data: dict) -> None:  # noqa: ARG002
        """Initialize the hook."""
        if self.target_name not in ["sdist"]:
            return

        build_dir = Path.cwd()
        os.chdir("hardpy/hardpy_panel/frontend")

        exit_code = os.system("yarn")  # noqa: S605, S607
        if exit_code:
            msg = "Yarn init failed"
            raise OSError(msg)
        exit_code = os.system("yarn build")  # noqa: S605, S607
        if exit_code:
            msg = "Yarn build failed"
            raise OSError(msg)
        os.chdir(build_dir)
