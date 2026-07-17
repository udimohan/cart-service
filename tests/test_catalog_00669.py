"""Tests for catalog_00669."""

import pytest

from cartservice.generated.catalog_00669 import (
    Product_00669,
    bucket_by_tag_00669,
    is_valid_sku_00669,
    price_with_tax_00669,
)


def test_price_with_tax_00669():
    assert price_with_tax_00669(1000, 500) == 1050


def test_price_with_tax_negative_00669():
    with pytest.raises(ValueError):
        price_with_tax_00669(1000, -1)


def test_is_valid_sku_00669():
    assert is_valid_sku_00669("abc123")
    assert not is_valid_sku_00669("")


def test_bucket_by_tag_00669():
    p = Product_00669("s1", 100, ["a"])
    assert bucket_by_tag_00669([p]) == {"a": ["s1"]}
