"""Tests for catalog_01547."""

import pytest

from cartservice.generated.catalog_01547 import (
    Product_01547,
    bucket_by_tag_01547,
    is_valid_sku_01547,
    price_with_tax_01547,
)


def test_price_with_tax_01547():
    assert price_with_tax_01547(1000, 500) == 1050


def test_price_with_tax_negative_01547():
    with pytest.raises(ValueError):
        price_with_tax_01547(1000, -1)


def test_is_valid_sku_01547():
    assert is_valid_sku_01547("abc123")
    assert not is_valid_sku_01547("")


def test_bucket_by_tag_01547():
    p = Product_01547("s1", 100, ["a"])
    assert bucket_by_tag_01547([p]) == {"a": ["s1"]}
