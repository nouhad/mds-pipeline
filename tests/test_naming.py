"""Tests for mds.naming."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from mds.naming import is_valid_name, build_name, tokenise_name


class TestIsValidName:
    def test_is_valid_name_valid(self):
        assert is_valid_name("geo_sphere_001") is True

    def test_is_valid_name_invalid_uppercase(self):
        assert is_valid_name("Geo_Sphere") is False

    def test_is_valid_name_invalid_start_digit(self):
        assert is_valid_name("1geo") is False

    def test_is_valid_name_empty(self):
        assert is_valid_name("") is False

    def test_is_valid_name_single_letter(self):
        assert is_valid_name("a") is True

    def test_is_valid_name_with_numbers(self):
        assert is_valid_name("geo001") is True

    def test_is_valid_name_with_spaces(self):
        assert is_valid_name("geo sphere") is False

    def test_is_valid_name_uppercase_only(self):
        assert is_valid_name("GEO") is False


class TestBuildName:
    def test_build_name_basic(self):
        assert build_name("geo", "sphere", 1) == "geo_sphere_001"

    def test_build_name_index_padding(self):
        assert build_name("geo", "sphere", 42) == "geo_sphere_042"

    def test_build_name_index_three_digits(self):
        assert build_name("geo", "sphere", 999) == "geo_sphere_999"

    def test_build_name_invalid_prefix(self):
        with pytest.raises(ValueError):
            build_name("GEO", "sphere", 1)

    def test_build_name_invalid_descriptor(self):
        with pytest.raises(ValueError):
            build_name("geo", "My Sphere", 1)

    def test_build_name_invalid_prefix_starts_digit(self):
        with pytest.raises(ValueError):
            build_name("1geo", "sphere", 1)


class TestTokeniseName:
    def test_tokenise_name(self):
        assert tokenise_name("geo_sphere_001") == ["geo", "sphere", "001"]

    def test_tokenise_name_single(self):
        assert tokenise_name("geo") == ["geo"]

    def test_tokenise_name_two_parts(self):
        assert tokenise_name("geo_sphere") == ["geo", "sphere"]
