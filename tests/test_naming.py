"""Tests for mds.naming."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from mds.naming import isValidName, buildName, tokeniseName


class TestIsValidName:
    def test_is_valid_name_valid(self):
        assert isValidName("geo_sphere_001") is True

    def test_is_valid_name_invalid_uppercase(self):
        assert isValidName("Geo_Sphere") is False

    def test_is_valid_name_invalid_start_digit(self):
        assert isValidName("1geo") is False

    def test_is_valid_name_empty(self):
        assert isValidName("") is False

    def test_is_valid_name_single_letter(self):
        assert isValidName("a") is True

    def test_is_valid_name_with_numbers(self):
        assert isValidName("geo001") is True

    def test_is_valid_name_with_spaces(self):
        assert isValidName("geo sphere") is False

    def test_is_valid_name_uppercase_only(self):
        assert isValidName("GEO") is False


class TestBuildName:
    def test_build_name_basic(self):
        assert buildName("geo", "sphere", 1) == "geo_sphere_001"

    def test_build_name_index_padding(self):
        assert buildName("geo", "sphere", 42) == "geo_sphere_042"

    def test_build_name_index_three_digits(self):
        assert buildName("geo", "sphere", 999) == "geo_sphere_999"

    def test_build_name_invalid_prefix(self):
        with pytest.raises(ValueError):
            buildName("GEO", "sphere", 1)

    def test_build_name_invalid_descriptor(self):
        with pytest.raises(ValueError):
            buildName("geo", "My Sphere", 1)

    def test_build_name_invalid_prefix_starts_digit(self):
        with pytest.raises(ValueError):
            buildName("1geo", "sphere", 1)


class TestTokeniseName:
    def test_tokenise_name(self):
        assert tokeniseName("geo_sphere_001") == ["geo", "sphere", "001"]

    def test_tokenise_name_single(self):
        assert tokeniseName("geo") == ["geo"]

    def test_tokenise_name_two_parts(self):
        assert tokeniseName("geo_sphere") == ["geo", "sphere"]
