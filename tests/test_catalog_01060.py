"""Tests for catalog_01060."""

import pytest

from cartservice.generated.catalog_01060 import (
    Product_01060,
    bucket_by_tag_01060,
    is_valid_sku_01060,
    price_with_tax_01060,
)


def test_price_with_tax_01060():
    assert price_with_tax_01060(1000, 500) == 1050


def test_price_with_tax_negative_01060():
    with pytest.raises(ValueError):
        price_with_tax_01060(1000, -1)


def test_is_valid_sku_01060():
    assert is_valid_sku_01060("abc123")
    assert not is_valid_sku_01060("")


def test_bucket_by_tag_01060():
    p = Product_01060("s1", 100, ["a"])
    assert bucket_by_tag_01060([p]) == {"a": ["s1"]}
