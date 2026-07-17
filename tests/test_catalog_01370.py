"""Tests for catalog_01370."""

import pytest

from cartservice.generated.catalog_01370 import (
    Product_01370,
    bucket_by_tag_01370,
    is_valid_sku_01370,
    price_with_tax_01370,
)


def test_price_with_tax_01370():
    assert price_with_tax_01370(1000, 500) == 1050


def test_price_with_tax_negative_01370():
    with pytest.raises(ValueError):
        price_with_tax_01370(1000, -1)


def test_is_valid_sku_01370():
    assert is_valid_sku_01370("abc123")
    assert not is_valid_sku_01370("")


def test_bucket_by_tag_01370():
    p = Product_01370("s1", 100, ["a"])
    assert bucket_by_tag_01370([p]) == {"a": ["s1"]}
