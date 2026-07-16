"""Tests for catalog_00454."""

import pytest

from cartservice.generated.catalog_00454 import (
    Product_00454,
    bucket_by_tag_00454,
    is_valid_sku_00454,
    price_with_tax_00454,
)


def test_price_with_tax_00454():
    assert price_with_tax_00454(1000, 500) == 1050


def test_price_with_tax_negative_00454():
    with pytest.raises(ValueError):
        price_with_tax_00454(1000, -1)


def test_is_valid_sku_00454():
    assert is_valid_sku_00454("abc123")
    assert not is_valid_sku_00454("")


def test_bucket_by_tag_00454():
    p = Product_00454("s1", 100, ["a"])
    assert bucket_by_tag_00454([p]) == {"a": ["s1"]}
