"""Tests for catalog_00955."""

import pytest

from cartservice.generated.catalog_00955 import (
    Product_00955,
    bucket_by_tag_00955,
    is_valid_sku_00955,
    price_with_tax_00955,
)


def test_price_with_tax_00955():
    assert price_with_tax_00955(1000, 500) == 1050


def test_price_with_tax_negative_00955():
    with pytest.raises(ValueError):
        price_with_tax_00955(1000, -1)


def test_is_valid_sku_00955():
    assert is_valid_sku_00955("abc123")
    assert not is_valid_sku_00955("")


def test_bucket_by_tag_00955():
    p = Product_00955("s1", 100, ["a"])
    assert bucket_by_tag_00955([p]) == {"a": ["s1"]}
