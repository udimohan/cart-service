"""Tests for catalog_00564."""

import pytest

from cartservice.generated.catalog_00564 import (
    Product_00564,
    bucket_by_tag_00564,
    is_valid_sku_00564,
    price_with_tax_00564,
)


def test_price_with_tax_00564():
    assert price_with_tax_00564(1000, 500) == 1050


def test_price_with_tax_negative_00564():
    with pytest.raises(ValueError):
        price_with_tax_00564(1000, -1)


def test_is_valid_sku_00564():
    assert is_valid_sku_00564("abc123")
    assert not is_valid_sku_00564("")


def test_bucket_by_tag_00564():
    p = Product_00564("s1", 100, ["a"])
    assert bucket_by_tag_00564([p]) == {"a": ["s1"]}
