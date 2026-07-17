"""Tests for catalog_00145."""

import pytest

from cartservice.generated.catalog_00145 import (
    Product_00145,
    bucket_by_tag_00145,
    is_valid_sku_00145,
    price_with_tax_00145,
)


def test_price_with_tax_00145():
    assert price_with_tax_00145(1000, 500) == 1050


def test_price_with_tax_negative_00145():
    with pytest.raises(ValueError):
        price_with_tax_00145(1000, -1)


def test_is_valid_sku_00145():
    assert is_valid_sku_00145("abc123")
    assert not is_valid_sku_00145("")


def test_bucket_by_tag_00145():
    p = Product_00145("s1", 100, ["a"])
    assert bucket_by_tag_00145([p]) == {"a": ["s1"]}
