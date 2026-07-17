"""Tests for catalog_01645."""

import pytest

from cartservice.generated.catalog_01645 import (
    Product_01645,
    bucket_by_tag_01645,
    is_valid_sku_01645,
    price_with_tax_01645,
)


def test_price_with_tax_01645():
    assert price_with_tax_01645(1000, 500) == 1050


def test_price_with_tax_negative_01645():
    with pytest.raises(ValueError):
        price_with_tax_01645(1000, -1)


def test_is_valid_sku_01645():
    assert is_valid_sku_01645("abc123")
    assert not is_valid_sku_01645("")


def test_bucket_by_tag_01645():
    p = Product_01645("s1", 100, ["a"])
    assert bucket_by_tag_01645([p]) == {"a": ["s1"]}
