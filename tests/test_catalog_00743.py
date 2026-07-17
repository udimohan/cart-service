"""Tests for catalog_00743."""

import pytest

from cartservice.generated.catalog_00743 import (
    Product_00743,
    bucket_by_tag_00743,
    is_valid_sku_00743,
    price_with_tax_00743,
)


def test_price_with_tax_00743():
    assert price_with_tax_00743(1000, 500) == 1050


def test_price_with_tax_negative_00743():
    with pytest.raises(ValueError):
        price_with_tax_00743(1000, -1)


def test_is_valid_sku_00743():
    assert is_valid_sku_00743("abc123")
    assert not is_valid_sku_00743("")


def test_bucket_by_tag_00743():
    p = Product_00743("s1", 100, ["a"])
    assert bucket_by_tag_00743([p]) == {"a": ["s1"]}
