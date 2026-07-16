"""Tests for catalog_01572."""

import pytest

from cartservice.generated.catalog_01572 import (
    Product_01572,
    bucket_by_tag_01572,
    is_valid_sku_01572,
    price_with_tax_01572,
)


def test_price_with_tax_01572():
    assert price_with_tax_01572(1000, 500) == 1050


def test_price_with_tax_negative_01572():
    with pytest.raises(ValueError):
        price_with_tax_01572(1000, -1)


def test_is_valid_sku_01572():
    assert is_valid_sku_01572("abc123")
    assert not is_valid_sku_01572("")


def test_bucket_by_tag_01572():
    p = Product_01572("s1", 100, ["a"])
    assert bucket_by_tag_01572([p]) == {"a": ["s1"]}
