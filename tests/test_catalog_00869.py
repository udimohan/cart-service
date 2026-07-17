"""Tests for catalog_00869."""

import pytest

from cartservice.generated.catalog_00869 import (
    Product_00869,
    bucket_by_tag_00869,
    is_valid_sku_00869,
    price_with_tax_00869,
)


def test_price_with_tax_00869():
    assert price_with_tax_00869(1000, 500) == 1050


def test_price_with_tax_negative_00869():
    with pytest.raises(ValueError):
        price_with_tax_00869(1000, -1)


def test_is_valid_sku_00869():
    assert is_valid_sku_00869("abc123")
    assert not is_valid_sku_00869("")


def test_bucket_by_tag_00869():
    p = Product_00869("s1", 100, ["a"])
    assert bucket_by_tag_00869([p]) == {"a": ["s1"]}
