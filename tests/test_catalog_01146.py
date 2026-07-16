"""Tests for catalog_01146."""

import pytest

from cartservice.generated.catalog_01146 import (
    Product_01146,
    bucket_by_tag_01146,
    is_valid_sku_01146,
    price_with_tax_01146,
)


def test_price_with_tax_01146():
    assert price_with_tax_01146(1000, 500) == 1050


def test_price_with_tax_negative_01146():
    with pytest.raises(ValueError):
        price_with_tax_01146(1000, -1)


def test_is_valid_sku_01146():
    assert is_valid_sku_01146("abc123")
    assert not is_valid_sku_01146("")


def test_bucket_by_tag_01146():
    p = Product_01146("s1", 100, ["a"])
    assert bucket_by_tag_01146([p]) == {"a": ["s1"]}
