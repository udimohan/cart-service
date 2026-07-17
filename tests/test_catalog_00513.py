"""Tests for catalog_00513."""

import pytest

from cartservice.generated.catalog_00513 import (
    Product_00513,
    bucket_by_tag_00513,
    is_valid_sku_00513,
    price_with_tax_00513,
)


def test_price_with_tax_00513():
    assert price_with_tax_00513(1000, 500) == 1050


def test_price_with_tax_negative_00513():
    with pytest.raises(ValueError):
        price_with_tax_00513(1000, -1)


def test_is_valid_sku_00513():
    assert is_valid_sku_00513("abc123")
    assert not is_valid_sku_00513("")


def test_bucket_by_tag_00513():
    p = Product_00513("s1", 100, ["a"])
    assert bucket_by_tag_00513([p]) == {"a": ["s1"]}
