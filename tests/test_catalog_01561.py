"""Tests for catalog_01561."""

import pytest

from cartservice.generated.catalog_01561 import (
    Product_01561,
    bucket_by_tag_01561,
    is_valid_sku_01561,
    price_with_tax_01561,
)


def test_price_with_tax_01561():
    assert price_with_tax_01561(1000, 500) == 1050


def test_price_with_tax_negative_01561():
    with pytest.raises(ValueError):
        price_with_tax_01561(1000, -1)


def test_is_valid_sku_01561():
    assert is_valid_sku_01561("abc123")
    assert not is_valid_sku_01561("")


def test_bucket_by_tag_01561():
    p = Product_01561("s1", 100, ["a"])
    assert bucket_by_tag_01561([p]) == {"a": ["s1"]}
