"""Tests for catalog_00021."""

import pytest

from cartservice.generated.catalog_00021 import (
    Product_00021,
    bucket_by_tag_00021,
    is_valid_sku_00021,
    price_with_tax_00021,
)


def test_price_with_tax_00021():
    assert price_with_tax_00021(1000, 500) == 1050


def test_price_with_tax_negative_00021():
    with pytest.raises(ValueError):
        price_with_tax_00021(1000, -1)


def test_is_valid_sku_00021():
    assert is_valid_sku_00021("abc123")
    assert not is_valid_sku_00021("")


def test_bucket_by_tag_00021():
    p = Product_00021("s1", 100, ["a"])
    assert bucket_by_tag_00021([p]) == {"a": ["s1"]}
