"""Tests for catalog_00764."""

import pytest

from cartservice.generated.catalog_00764 import (
    Product_00764,
    bucket_by_tag_00764,
    is_valid_sku_00764,
    price_with_tax_00764,
)


def test_price_with_tax_00764():
    assert price_with_tax_00764(1000, 500) == 1050


def test_price_with_tax_negative_00764():
    with pytest.raises(ValueError):
        price_with_tax_00764(1000, -1)


def test_is_valid_sku_00764():
    assert is_valid_sku_00764("abc123")
    assert not is_valid_sku_00764("")


def test_bucket_by_tag_00764():
    p = Product_00764("s1", 100, ["a"])
    assert bucket_by_tag_00764([p]) == {"a": ["s1"]}
