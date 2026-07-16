"""Tests for catalog_01029."""

import pytest

from cartservice.generated.catalog_01029 import (
    Product_01029,
    bucket_by_tag_01029,
    is_valid_sku_01029,
    price_with_tax_01029,
)


def test_price_with_tax_01029():
    assert price_with_tax_01029(1000, 500) == 1050


def test_price_with_tax_negative_01029():
    with pytest.raises(ValueError):
        price_with_tax_01029(1000, -1)


def test_is_valid_sku_01029():
    assert is_valid_sku_01029("abc123")
    assert not is_valid_sku_01029("")


def test_bucket_by_tag_01029():
    p = Product_01029("s1", 100, ["a"])
    assert bucket_by_tag_01029([p]) == {"a": ["s1"]}
