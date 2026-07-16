"""Tests for catalog_01488."""

import pytest

from cartservice.generated.catalog_01488 import (
    Product_01488,
    bucket_by_tag_01488,
    is_valid_sku_01488,
    price_with_tax_01488,
)


def test_price_with_tax_01488():
    assert price_with_tax_01488(1000, 500) == 1050


def test_price_with_tax_negative_01488():
    with pytest.raises(ValueError):
        price_with_tax_01488(1000, -1)


def test_is_valid_sku_01488():
    assert is_valid_sku_01488("abc123")
    assert not is_valid_sku_01488("")


def test_bucket_by_tag_01488():
    p = Product_01488("s1", 100, ["a"])
    assert bucket_by_tag_01488([p]) == {"a": ["s1"]}
