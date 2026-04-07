# 3D2G04A_3DScripting: Day 03
# Task 01: Paths and Versions
# Description: Use mds.paths, mds.versioning, and mds.io to build a shot path, get the next version, and round-trip a JSON metadata file.

import mds.paths as paths
import mds.versioning as versioning
import mds.io as io


# Task 1: Construct the shot directory path.
shot_path = paths.shotDir("010", "0010")
print(f"Shot directory: {shot_path}")

# Task 2: Get the next version from a list of existing versions.
existing_versions = ["v001", "v002", "v003"]
next_ver = versioning.nextVersion(existing_versions)
print(f"Next version: {next_ver}")

# Task 3: Write a JSON metadata file to the versioned shot path.
metadata = {"sequence": "010", "shot": "0010", "version": next_ver}
output_path = shot_path / next_ver / "metadata.json"
io.writeJson(metadata, output_path)
print(f"Wrote metadata to: {output_path}")

# Task 4: Read the JSON back and print its contents.
loaded = io.readJson(output_path)
print("Loaded metadata:", loaded)

