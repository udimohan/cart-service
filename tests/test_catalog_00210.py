"""Tests for catalog_00210."""

import pytest

from cartservice.generated.catalog_00210 import (
    Product_00210,
    bucket_by_tag_00210,
    is_valid_sku_00210,
    price_with_tax_00210,
)


def test_price_with_tax_00210():
    assert price_with_tax_00210(1000, 500) == 1050


def test_price_with_tax_negative_00210():
    with pytest.raises(ValueError):
        price_with_tax_00210(1000, -1)


def test_is_valid_sku_00210():
    assert is_valid_sku_00210("abc123")
    assert not is_valid_sku_00210("")


def test_bucket_by_tag_00210():
    p = Product_00210("s1", 100, ["a"])
    assert bucket_by_tag_00210([p]) == {"a": ["s1"]}
