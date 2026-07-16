"""Tests for catalog_00309."""

import pytest

from cartservice.generated.catalog_00309 import (
    Product_00309,
    bucket_by_tag_00309,
    is_valid_sku_00309,
    price_with_tax_00309,
)


def test_price_with_tax_00309():
    assert price_with_tax_00309(1000, 500) == 1050


def test_price_with_tax_negative_00309():
    with pytest.raises(ValueError):
        price_with_tax_00309(1000, -1)


def test_is_valid_sku_00309():
    assert is_valid_sku_00309("abc123")
    assert not is_valid_sku_00309("")


def test_bucket_by_tag_00309():
    p = Product_00309("s1", 100, ["a"])
    assert bucket_by_tag_00309([p]) == {"a": ["s1"]}
