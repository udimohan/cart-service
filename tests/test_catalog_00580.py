"""Tests for catalog_00580."""

import pytest

from cartservice.generated.catalog_00580 import (
    Product_00580,
    bucket_by_tag_00580,
    is_valid_sku_00580,
    price_with_tax_00580,
)


def test_price_with_tax_00580():
    assert price_with_tax_00580(1000, 500) == 1050


def test_price_with_tax_negative_00580():
    with pytest.raises(ValueError):
        price_with_tax_00580(1000, -1)


def test_is_valid_sku_00580():
    assert is_valid_sku_00580("abc123")
    assert not is_valid_sku_00580("")


def test_bucket_by_tag_00580():
    p = Product_00580("s1", 100, ["a"])
    assert bucket_by_tag_00580([p]) == {"a": ["s1"]}
