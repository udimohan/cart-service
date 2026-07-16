"""Tests for catalog_00209."""

import pytest

from cartservice.generated.catalog_00209 import (
    Product_00209,
    bucket_by_tag_00209,
    is_valid_sku_00209,
    price_with_tax_00209,
)


def test_price_with_tax_00209():
    assert price_with_tax_00209(1000, 500) == 1050


def test_price_with_tax_negative_00209():
    with pytest.raises(ValueError):
        price_with_tax_00209(1000, -1)


def test_is_valid_sku_00209():
    assert is_valid_sku_00209("abc123")
    assert not is_valid_sku_00209("")


def test_bucket_by_tag_00209():
    p = Product_00209("s1", 100, ["a"])
    assert bucket_by_tag_00209([p]) == {"a": ["s1"]}
