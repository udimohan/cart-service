"""Tests for catalog_01518."""

import pytest

from cartservice.generated.catalog_01518 import (
    Product_01518,
    bucket_by_tag_01518,
    is_valid_sku_01518,
    price_with_tax_01518,
)


def test_price_with_tax_01518():
    assert price_with_tax_01518(1000, 500) == 1050


def test_price_with_tax_negative_01518():
    with pytest.raises(ValueError):
        price_with_tax_01518(1000, -1)


def test_is_valid_sku_01518():
    assert is_valid_sku_01518("abc123")
    assert not is_valid_sku_01518("")


def test_bucket_by_tag_01518():
    p = Product_01518("s1", 100, ["a"])
    assert bucket_by_tag_01518([p]) == {"a": ["s1"]}
