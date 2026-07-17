"""Tests for catalog_01081."""

import pytest

from cartservice.generated.catalog_01081 import (
    Product_01081,
    bucket_by_tag_01081,
    is_valid_sku_01081,
    price_with_tax_01081,
)


def test_price_with_tax_01081():
    assert price_with_tax_01081(1000, 500) == 1050


def test_price_with_tax_negative_01081():
    with pytest.raises(ValueError):
        price_with_tax_01081(1000, -1)


def test_is_valid_sku_01081():
    assert is_valid_sku_01081("abc123")
    assert not is_valid_sku_01081("")


def test_bucket_by_tag_01081():
    p = Product_01081("s1", 100, ["a"])
    assert bucket_by_tag_01081([p]) == {"a": ["s1"]}
