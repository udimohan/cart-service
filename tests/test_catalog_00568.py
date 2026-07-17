"""Tests for catalog_00568."""

import pytest

from cartservice.generated.catalog_00568 import (
    Product_00568,
    bucket_by_tag_00568,
    is_valid_sku_00568,
    price_with_tax_00568,
)


def test_price_with_tax_00568():
    assert price_with_tax_00568(1000, 500) == 1050


def test_price_with_tax_negative_00568():
    with pytest.raises(ValueError):
        price_with_tax_00568(1000, -1)


def test_is_valid_sku_00568():
    assert is_valid_sku_00568("abc123")
    assert not is_valid_sku_00568("")


def test_bucket_by_tag_00568():
    p = Product_00568("s1", 100, ["a"])
    assert bucket_by_tag_00568([p]) == {"a": ["s1"]}
