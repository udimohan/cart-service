"""Tests for catalog_00250."""

import pytest

from cartservice.generated.catalog_00250 import (
    Product_00250,
    bucket_by_tag_00250,
    is_valid_sku_00250,
    price_with_tax_00250,
)


def test_price_with_tax_00250():
    assert price_with_tax_00250(1000, 500) == 1050


def test_price_with_tax_negative_00250():
    with pytest.raises(ValueError):
        price_with_tax_00250(1000, -1)


def test_is_valid_sku_00250():
    assert is_valid_sku_00250("abc123")
    assert not is_valid_sku_00250("")


def test_bucket_by_tag_00250():
    p = Product_00250("s1", 100, ["a"])
    assert bucket_by_tag_00250([p]) == {"a": ["s1"]}
