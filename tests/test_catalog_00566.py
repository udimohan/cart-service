"""Tests for catalog_00566."""

import pytest

from cartservice.generated.catalog_00566 import (
    Product_00566,
    bucket_by_tag_00566,
    is_valid_sku_00566,
    price_with_tax_00566,
)


def test_price_with_tax_00566():
    assert price_with_tax_00566(1000, 500) == 1050


def test_price_with_tax_negative_00566():
    with pytest.raises(ValueError):
        price_with_tax_00566(1000, -1)


def test_is_valid_sku_00566():
    assert is_valid_sku_00566("abc123")
    assert not is_valid_sku_00566("")


def test_bucket_by_tag_00566():
    p = Product_00566("s1", 100, ["a"])
    assert bucket_by_tag_00566([p]) == {"a": ["s1"]}
