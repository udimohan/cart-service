"""Tests for catalog_00816."""

import pytest

from cartservice.generated.catalog_00816 import (
    Product_00816,
    bucket_by_tag_00816,
    is_valid_sku_00816,
    price_with_tax_00816,
)


def test_price_with_tax_00816():
    assert price_with_tax_00816(1000, 500) == 1050


def test_price_with_tax_negative_00816():
    with pytest.raises(ValueError):
        price_with_tax_00816(1000, -1)


def test_is_valid_sku_00816():
    assert is_valid_sku_00816("abc123")
    assert not is_valid_sku_00816("")


def test_bucket_by_tag_00816():
    p = Product_00816("s1", 100, ["a"])
    assert bucket_by_tag_00816([p]) == {"a": ["s1"]}
