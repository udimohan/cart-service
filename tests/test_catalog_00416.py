"""Tests for catalog_00416."""

import pytest

from cartservice.generated.catalog_00416 import (
    Product_00416,
    bucket_by_tag_00416,
    is_valid_sku_00416,
    price_with_tax_00416,
)


def test_price_with_tax_00416():
    assert price_with_tax_00416(1000, 500) == 1050


def test_price_with_tax_negative_00416():
    with pytest.raises(ValueError):
        price_with_tax_00416(1000, -1)


def test_is_valid_sku_00416():
    assert is_valid_sku_00416("abc123")
    assert not is_valid_sku_00416("")


def test_bucket_by_tag_00416():
    p = Product_00416("s1", 100, ["a"])
    assert bucket_by_tag_00416([p]) == {"a": ["s1"]}
