"""Tests for mds.paths."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from pathlib import Path
from mds.paths import shotDir, playblastDir, cacheDir, getProjectRoot, ensureDir


class TestShotDir:
    def test_shot_dir_structure(self):
        result = shotDir("010", "0010")
        parts = result.parts
        assert "sq010" in parts
        assert "sh0010" in parts
        # sq010 must be a direct parent of sh0010
        sq_idx = parts.index("sq010")
        sh_idx = parts.index("sh0010")
        assert sh_idx == sq_idx + 1

    def test_shot_dir_ends_with_expected_suffix(self):
        result = shotDir("010", "0010")
        assert str(result).endswith("sq010/sh0010") or str(result).endswith(
            r"sq010\sh0010"
        )


class TestPlayblastDir:
    def test_playblast_dir_structure(self):
        result = playblastDir("010", "0010", "v001")
        assert "playblasts" in result.parts
        assert "v001" in result.parts
        assert result.parts[-1] == "v001"
        assert result.parts[-2] == "playblasts"

    def test_playblast_dir_contains_outputs(self):
        result = playblastDir("010", "0010", "v001")
        assert "outputs" in result.parts


class TestCacheDir:
    def test_cache_dir_structure(self):
        result = cacheDir("010", "0010", "v001")
        assert "cache" in result.parts
        assert "v001" in result.parts
        assert result.parts[-1] == "v001"
        assert result.parts[-2] == "cache"


class TestGetProjectRoot:
    def test_custom_project_root(self, monkeypatch, tmp_path):
        custom_root = str(tmp_path / "custom_root")
        monkeypatch.setenv("MDS_PROJECT_ROOT", custom_root)
        result = getProjectRoot()
        assert result == Path(custom_root)

    def test_default_project_root_when_env_not_set(self, monkeypatch):
        monkeypatch.delenv("MDS_PROJECT_ROOT", raising=False)
        result = getProjectRoot()
        # Should be a Path (the default), not None
        assert isinstance(result, Path)


class TestEnsureDir:
    def test_ensure_dir_creates(self, tmp_path):
        target = tmp_path / "new" / "nested" / "dir"
        assert not target.exists()
        returned = ensureDir(target)
        assert target.exists()
        assert returned == target

    def test_ensure_dir_idempotent(self, tmp_path):
        target = tmp_path / "already_here"
        target.mkdir()
        # Should not raise on a directory that already exists
        returned = ensureDir(target)
        assert returned == target
