"""Tests for catalog_01124."""

import pytest

from cartservice.generated.catalog_01124 import (
    Product_01124,
    bucket_by_tag_01124,
    is_valid_sku_01124,
    price_with_tax_01124,
)


def test_price_with_tax_01124():
    assert price_with_tax_01124(1000, 500) == 1050


def test_price_with_tax_negative_01124():
    with pytest.raises(ValueError):
        price_with_tax_01124(1000, -1)


def test_is_valid_sku_01124():
    assert is_valid_sku_01124("abc123")
    assert not is_valid_sku_01124("")


def test_bucket_by_tag_01124():
    p = Product_01124("s1", 100, ["a"])
    assert bucket_by_tag_01124([p]) == {"a": ["s1"]}
