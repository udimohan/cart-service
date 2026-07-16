"""Tests for catalog_00211."""

import pytest

from cartservice.generated.catalog_00211 import (
    Product_00211,
    bucket_by_tag_00211,
    is_valid_sku_00211,
    price_with_tax_00211,
)


def test_price_with_tax_00211():
    assert price_with_tax_00211(1000, 500) == 1050


def test_price_with_tax_negative_00211():
    with pytest.raises(ValueError):
        price_with_tax_00211(1000, -1)


def test_is_valid_sku_00211():
    assert is_valid_sku_00211("abc123")
    assert not is_valid_sku_00211("")


def test_bucket_by_tag_00211():
    p = Product_00211("s1", 100, ["a"])
    assert bucket_by_tag_00211([p]) == {"a": ["s1"]}
