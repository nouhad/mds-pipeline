"""Day 03 – Task 01 – Paths and Versions.

Practise using mds.paths, mds.versioning, and mds.io together to construct shot
paths, determine the next version, and round-trip JSON metadata – all without
needing a running Maya session.
"""

from pathlib import Path

import mds.paths as paths
import mds.versioning as versioning
import mds.io as io


def main() -> None:
    """Run the paths-and-versions exercise."""

    # ------------------------------------------------------------------
    # TODO 1: Construct the shot directory path for sequence "010",
    #         shot "0010" using mds.paths.shot_dir().
    #         Print the resulting path.
    # ------------------------------------------------------------------
    shot_path = paths.shot_dir("010", "0010")
    print(f"Shot directory: {shot_path}")

    # ------------------------------------------------------------------
    # TODO 2: Determine the next version from a list of existing versions.
    #         Pretend the following versions already exist on disk:
    #           existing = ["v001", "v002", "v003"]
    #         Use mds.versioning.next_version() and print the result.
    # ------------------------------------------------------------------
    existing_versions = ["v001", "v002", "v003"]
    next_ver = "TODO"  # replace with real call
    print(f"Next version: {next_ver}")

    # ------------------------------------------------------------------
    # TODO 3: Write a JSON file with scene metadata.
    #         Use mds.io.write_json() to save to:
    #           shot_path / next_ver / "metadata.json"
    #         The dict should include at least:
    #           {"sequence": "010", "shot": "0010", "version": next_ver}
    #         Note: the directory does not need to exist first –
    #         write_json() creates parent directories automatically.
    # ------------------------------------------------------------------
    metadata = {
        "sequence": "010",
        "shot": "0010",
        "version": next_ver,
    }
    output_path = shot_path / next_ver / "metadata.json"
    print(f"Would write to: {output_path}")
    # io.write_json(metadata, output_path)   # uncomment once next_ver is set

    # ------------------------------------------------------------------
    # TODO 4: Read the JSON file back and print its contents.
    #         Use mds.io.read_json() or mds.io.read_json_safe().
    # ------------------------------------------------------------------
    # loaded = io.read_json(output_path)
    # print("Loaded metadata:", loaded)
    print("TODO 4: uncomment the read_json lines above once write works")


if __name__ == "__main__":
    main()
