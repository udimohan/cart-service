"""Tests for catalog_00572."""

import pytest

from cartservice.generated.catalog_00572 import (
    Product_00572,
    bucket_by_tag_00572,
    is_valid_sku_00572,
    price_with_tax_00572,
)


def test_price_with_tax_00572():
    assert price_with_tax_00572(1000, 500) == 1050


def test_price_with_tax_negative_00572():
    with pytest.raises(ValueError):
        price_with_tax_00572(1000, -1)


def test_is_valid_sku_00572():
    assert is_valid_sku_00572("abc123")
    assert not is_valid_sku_00572("")


def test_bucket_by_tag_00572():
    p = Product_00572("s1", 100, ["a"])
    assert bucket_by_tag_00572([p]) == {"a": ["s1"]}
