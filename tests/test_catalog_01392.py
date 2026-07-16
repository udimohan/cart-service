"""Tests for catalog_01392."""

import pytest

from cartservice.generated.catalog_01392 import (
    Product_01392,
    bucket_by_tag_01392,
    is_valid_sku_01392,
    price_with_tax_01392,
)


def test_price_with_tax_01392():
    assert price_with_tax_01392(1000, 500) == 1050


def test_price_with_tax_negative_01392():
    with pytest.raises(ValueError):
        price_with_tax_01392(1000, -1)


def test_is_valid_sku_01392():
    assert is_valid_sku_01392("abc123")
    assert not is_valid_sku_01392("")


def test_bucket_by_tag_01392():
    p = Product_01392("s1", 100, ["a"])
    assert bucket_by_tag_01392([p]) == {"a": ["s1"]}
