"""Day 01 – Task 01 – Hello Maya.

Print the current scene name and Maya version to confirm the environment is set up
correctly and practice basic Maya command usage.

Run this script from Maya's Script Editor (Python tab) or send it via the Command Port.
"""

import sys

try:
    import maya.cmds as cmds  # type: ignore[import]
except ImportError:
    cmds = None  # type: ignore[assignment]

from mds.maya import scene


def main() -> None:
    """Entry point for the Hello Maya task."""

    # ------------------------------------------------------------------
    # TODO 1: Print a greeting that includes your own name.
    #         Example: "Hello from Maya! My name is Jane Smith."
    # ------------------------------------------------------------------
    print("TODO 1: replace this line with your greeting")

    # ------------------------------------------------------------------
    # TODO 2: Print the Maya version.
    #         Hint: cmds.about(version=True) returns the version string.
    #         Guard against cmds being None (outside Maya).
    # ------------------------------------------------------------------
    if cmds is not None:
        print("TODO 2: print the Maya version here")
    else:
        print("(Maya not available – running outside of Maya)")

    # ------------------------------------------------------------------
    # TODO 3: Print the current scene name using mds.maya.scene.
    #         Hint: call scene.get_scene_name()
    #         An empty string means no file is currently open.
    # ------------------------------------------------------------------
    print("TODO 3: print the scene name here")


if __name__ == "__main__":
    main()
