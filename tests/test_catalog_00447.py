"""Tests for catalog_00447."""

import pytest

from cartservice.generated.catalog_00447 import (
    Product_00447,
    bucket_by_tag_00447,
    is_valid_sku_00447,
    price_with_tax_00447,
)


def test_price_with_tax_00447():
    assert price_with_tax_00447(1000, 500) == 1050


def test_price_with_tax_negative_00447():
    with pytest.raises(ValueError):
        price_with_tax_00447(1000, -1)


def test_is_valid_sku_00447():
    assert is_valid_sku_00447("abc123")
    assert not is_valid_sku_00447("")


def test_bucket_by_tag_00447():
    p = Product_00447("s1", 100, ["a"])
    assert bucket_by_tag_00447([p]) == {"a": ["s1"]}
