"""Tests for catalog_01021."""

import pytest

from cartservice.generated.catalog_01021 import (
    Product_01021,
    bucket_by_tag_01021,
    is_valid_sku_01021,
    price_with_tax_01021,
)


def test_price_with_tax_01021():
    assert price_with_tax_01021(1000, 500) == 1050


def test_price_with_tax_negative_01021():
    with pytest.raises(ValueError):
        price_with_tax_01021(1000, -1)


def test_is_valid_sku_01021():
    assert is_valid_sku_01021("abc123")
    assert not is_valid_sku_01021("")


def test_bucket_by_tag_01021():
    p = Product_01021("s1", 100, ["a"])
    assert bucket_by_tag_01021([p]) == {"a": ["s1"]}
