"""Tests for catalog_00120."""

import pytest

from cartservice.generated.catalog_00120 import (
    Product_00120,
    bucket_by_tag_00120,
    is_valid_sku_00120,
    price_with_tax_00120,
)


def test_price_with_tax_00120():
    assert price_with_tax_00120(1000, 500) == 1050


def test_price_with_tax_negative_00120():
    with pytest.raises(ValueError):
        price_with_tax_00120(1000, -1)


def test_is_valid_sku_00120():
    assert is_valid_sku_00120("abc123")
    assert not is_valid_sku_00120("")


def test_bucket_by_tag_00120():
    p = Product_00120("s1", 100, ["a"])
    assert bucket_by_tag_00120([p]) == {"a": ["s1"]}
