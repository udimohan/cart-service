"""Tests for catalog_01189."""

import pytest

from cartservice.generated.catalog_01189 import (
    Product_01189,
    bucket_by_tag_01189,
    is_valid_sku_01189,
    price_with_tax_01189,
)


def test_price_with_tax_01189():
    assert price_with_tax_01189(1000, 500) == 1050


def test_price_with_tax_negative_01189():
    with pytest.raises(ValueError):
        price_with_tax_01189(1000, -1)


def test_is_valid_sku_01189():
    assert is_valid_sku_01189("abc123")
    assert not is_valid_sku_01189("")


def test_bucket_by_tag_01189():
    p = Product_01189("s1", 100, ["a"])
    assert bucket_by_tag_01189([p]) == {"a": ["s1"]}
