"""Tests for catalog_00095."""

import pytest

from cartservice.generated.catalog_00095 import (
    Product_00095,
    bucket_by_tag_00095,
    is_valid_sku_00095,
    price_with_tax_00095,
)


def test_price_with_tax_00095():
    assert price_with_tax_00095(1000, 500) == 1050


def test_price_with_tax_negative_00095():
    with pytest.raises(ValueError):
        price_with_tax_00095(1000, -1)


def test_is_valid_sku_00095():
    assert is_valid_sku_00095("abc123")
    assert not is_valid_sku_00095("")


def test_bucket_by_tag_00095():
    p = Product_00095("s1", 100, ["a"])
    assert bucket_by_tag_00095([p]) == {"a": ["s1"]}
