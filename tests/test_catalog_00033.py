"""Tests for catalog_00033."""

import pytest

from cartservice.generated.catalog_00033 import (
    Product_00033,
    bucket_by_tag_00033,
    is_valid_sku_00033,
    price_with_tax_00033,
)


def test_price_with_tax_00033():
    assert price_with_tax_00033(1000, 500) == 1050


def test_price_with_tax_negative_00033():
    with pytest.raises(ValueError):
        price_with_tax_00033(1000, -1)


def test_is_valid_sku_00033():
    assert is_valid_sku_00033("abc123")
    assert not is_valid_sku_00033("")


def test_bucket_by_tag_00033():
    p = Product_00033("s1", 100, ["a"])
    assert bucket_by_tag_00033([p]) == {"a": ["s1"]}
