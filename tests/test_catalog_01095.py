"""Tests for catalog_01095."""

import pytest

from cartservice.generated.catalog_01095 import (
    Product_01095,
    bucket_by_tag_01095,
    is_valid_sku_01095,
    price_with_tax_01095,
)


def test_price_with_tax_01095():
    assert price_with_tax_01095(1000, 500) == 1050


def test_price_with_tax_negative_01095():
    with pytest.raises(ValueError):
        price_with_tax_01095(1000, -1)


def test_is_valid_sku_01095():
    assert is_valid_sku_01095("abc123")
    assert not is_valid_sku_01095("")


def test_bucket_by_tag_01095():
    p = Product_01095("s1", 100, ["a"])
    assert bucket_by_tag_01095([p]) == {"a": ["s1"]}
