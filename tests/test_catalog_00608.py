"""Tests for catalog_00608."""

import pytest

from cartservice.generated.catalog_00608 import (
    Product_00608,
    bucket_by_tag_00608,
    is_valid_sku_00608,
    price_with_tax_00608,
)


def test_price_with_tax_00608():
    assert price_with_tax_00608(1000, 500) == 1050


def test_price_with_tax_negative_00608():
    with pytest.raises(ValueError):
        price_with_tax_00608(1000, -1)


def test_is_valid_sku_00608():
    assert is_valid_sku_00608("abc123")
    assert not is_valid_sku_00608("")


def test_bucket_by_tag_00608():
    p = Product_00608("s1", 100, ["a"])
    assert bucket_by_tag_00608([p]) == {"a": ["s1"]}
