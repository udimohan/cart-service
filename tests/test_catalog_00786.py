"""Tests for catalog_00786."""

import pytest

from cartservice.generated.catalog_00786 import (
    Product_00786,
    bucket_by_tag_00786,
    is_valid_sku_00786,
    price_with_tax_00786,
)


def test_price_with_tax_00786():
    assert price_with_tax_00786(1000, 500) == 1050


def test_price_with_tax_negative_00786():
    with pytest.raises(ValueError):
        price_with_tax_00786(1000, -1)


def test_is_valid_sku_00786():
    assert is_valid_sku_00786("abc123")
    assert not is_valid_sku_00786("")


def test_bucket_by_tag_00786():
    p = Product_00786("s1", 100, ["a"])
    assert bucket_by_tag_00786([p]) == {"a": ["s1"]}
