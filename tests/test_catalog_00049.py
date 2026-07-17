"""Tests for catalog_00049."""

import pytest

from cartservice.generated.catalog_00049 import (
    Product_00049,
    bucket_by_tag_00049,
    is_valid_sku_00049,
    price_with_tax_00049,
)


def test_price_with_tax_00049():
    assert price_with_tax_00049(1000, 500) == 1050


def test_price_with_tax_negative_00049():
    with pytest.raises(ValueError):
        price_with_tax_00049(1000, -1)


def test_is_valid_sku_00049():
    assert is_valid_sku_00049("abc123")
    assert not is_valid_sku_00049("")


def test_bucket_by_tag_00049():
    p = Product_00049("s1", 100, ["a"])
    assert bucket_by_tag_00049([p]) == {"a": ["s1"]}
