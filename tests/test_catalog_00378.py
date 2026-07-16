"""Tests for catalog_00378."""

import pytest

from cartservice.generated.catalog_00378 import (
    Product_00378,
    bucket_by_tag_00378,
    is_valid_sku_00378,
    price_with_tax_00378,
)


def test_price_with_tax_00378():
    assert price_with_tax_00378(1000, 500) == 1050


def test_price_with_tax_negative_00378():
    with pytest.raises(ValueError):
        price_with_tax_00378(1000, -1)


def test_is_valid_sku_00378():
    assert is_valid_sku_00378("abc123")
    assert not is_valid_sku_00378("")


def test_bucket_by_tag_00378():
    p = Product_00378("s1", 100, ["a"])
    assert bucket_by_tag_00378([p]) == {"a": ["s1"]}
