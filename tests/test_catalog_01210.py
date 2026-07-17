"""Tests for catalog_01210."""

import pytest

from cartservice.generated.catalog_01210 import (
    Product_01210,
    bucket_by_tag_01210,
    is_valid_sku_01210,
    price_with_tax_01210,
)


def test_price_with_tax_01210():
    assert price_with_tax_01210(1000, 500) == 1050


def test_price_with_tax_negative_01210():
    with pytest.raises(ValueError):
        price_with_tax_01210(1000, -1)


def test_is_valid_sku_01210():
    assert is_valid_sku_01210("abc123")
    assert not is_valid_sku_01210("")


def test_bucket_by_tag_01210():
    p = Product_01210("s1", 100, ["a"])
    assert bucket_by_tag_01210([p]) == {"a": ["s1"]}
