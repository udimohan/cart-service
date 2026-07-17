"""Tests for catalog_01219."""

import pytest

from cartservice.generated.catalog_01219 import (
    Product_01219,
    bucket_by_tag_01219,
    is_valid_sku_01219,
    price_with_tax_01219,
)


def test_price_with_tax_01219():
    assert price_with_tax_01219(1000, 500) == 1050


def test_price_with_tax_negative_01219():
    with pytest.raises(ValueError):
        price_with_tax_01219(1000, -1)


def test_is_valid_sku_01219():
    assert is_valid_sku_01219("abc123")
    assert not is_valid_sku_01219("")


def test_bucket_by_tag_01219():
    p = Product_01219("s1", 100, ["a"])
    assert bucket_by_tag_01219([p]) == {"a": ["s1"]}
