"""Tests for catalog_00131."""

import pytest

from cartservice.generated.catalog_00131 import (
    Product_00131,
    bucket_by_tag_00131,
    is_valid_sku_00131,
    price_with_tax_00131,
)


def test_price_with_tax_00131():
    assert price_with_tax_00131(1000, 500) == 1050


def test_price_with_tax_negative_00131():
    with pytest.raises(ValueError):
        price_with_tax_00131(1000, -1)


def test_is_valid_sku_00131():
    assert is_valid_sku_00131("abc123")
    assert not is_valid_sku_00131("")


def test_bucket_by_tag_00131():
    p = Product_00131("s1", 100, ["a"])
    assert bucket_by_tag_00131([p]) == {"a": ["s1"]}
