"""Tests for catalog_00557."""

import pytest

from cartservice.generated.catalog_00557 import (
    Product_00557,
    bucket_by_tag_00557,
    is_valid_sku_00557,
    price_with_tax_00557,
)


def test_price_with_tax_00557():
    assert price_with_tax_00557(1000, 500) == 1050


def test_price_with_tax_negative_00557():
    with pytest.raises(ValueError):
        price_with_tax_00557(1000, -1)


def test_is_valid_sku_00557():
    assert is_valid_sku_00557("abc123")
    assert not is_valid_sku_00557("")


def test_bucket_by_tag_00557():
    p = Product_00557("s1", 100, ["a"])
    assert bucket_by_tag_00557([p]) == {"a": ["s1"]}
