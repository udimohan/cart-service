"""Tests for catalog_00124."""

import pytest

from cartservice.generated.catalog_00124 import (
    Product_00124,
    bucket_by_tag_00124,
    is_valid_sku_00124,
    price_with_tax_00124,
)


def test_price_with_tax_00124():
    assert price_with_tax_00124(1000, 500) == 1050


def test_price_with_tax_negative_00124():
    with pytest.raises(ValueError):
        price_with_tax_00124(1000, -1)


def test_is_valid_sku_00124():
    assert is_valid_sku_00124("abc123")
    assert not is_valid_sku_00124("")


def test_bucket_by_tag_00124():
    p = Product_00124("s1", 100, ["a"])
    assert bucket_by_tag_00124([p]) == {"a": ["s1"]}
