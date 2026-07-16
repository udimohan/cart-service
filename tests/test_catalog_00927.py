"""Tests for catalog_00927."""

import pytest

from cartservice.generated.catalog_00927 import (
    Product_00927,
    bucket_by_tag_00927,
    is_valid_sku_00927,
    price_with_tax_00927,
)


def test_price_with_tax_00927():
    assert price_with_tax_00927(1000, 500) == 1050


def test_price_with_tax_negative_00927():
    with pytest.raises(ValueError):
        price_with_tax_00927(1000, -1)


def test_is_valid_sku_00927():
    assert is_valid_sku_00927("abc123")
    assert not is_valid_sku_00927("")


def test_bucket_by_tag_00927():
    p = Product_00927("s1", 100, ["a"])
    assert bucket_by_tag_00927([p]) == {"a": ["s1"]}
