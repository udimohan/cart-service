"""Tests for catalog_01049."""

import pytest

from cartservice.generated.catalog_01049 import (
    Product_01049,
    bucket_by_tag_01049,
    is_valid_sku_01049,
    price_with_tax_01049,
)


def test_price_with_tax_01049():
    assert price_with_tax_01049(1000, 500) == 1050


def test_price_with_tax_negative_01049():
    with pytest.raises(ValueError):
        price_with_tax_01049(1000, -1)


def test_is_valid_sku_01049():
    assert is_valid_sku_01049("abc123")
    assert not is_valid_sku_01049("")


def test_bucket_by_tag_01049():
    p = Product_01049("s1", 100, ["a"])
    assert bucket_by_tag_01049([p]) == {"a": ["s1"]}
