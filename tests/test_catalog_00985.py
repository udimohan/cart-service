"""Tests for catalog_00985."""

import pytest

from cartservice.generated.catalog_00985 import (
    Product_00985,
    bucket_by_tag_00985,
    is_valid_sku_00985,
    price_with_tax_00985,
)


def test_price_with_tax_00985():
    assert price_with_tax_00985(1000, 500) == 1050


def test_price_with_tax_negative_00985():
    with pytest.raises(ValueError):
        price_with_tax_00985(1000, -1)


def test_is_valid_sku_00985():
    assert is_valid_sku_00985("abc123")
    assert not is_valid_sku_00985("")


def test_bucket_by_tag_00985():
    p = Product_00985("s1", 100, ["a"])
    assert bucket_by_tag_00985([p]) == {"a": ["s1"]}
