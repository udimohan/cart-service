"""Tests for catalog_01256."""

import pytest

from cartservice.generated.catalog_01256 import (
    Product_01256,
    bucket_by_tag_01256,
    is_valid_sku_01256,
    price_with_tax_01256,
)


def test_price_with_tax_01256():
    assert price_with_tax_01256(1000, 500) == 1050


def test_price_with_tax_negative_01256():
    with pytest.raises(ValueError):
        price_with_tax_01256(1000, -1)


def test_is_valid_sku_01256():
    assert is_valid_sku_01256("abc123")
    assert not is_valid_sku_01256("")


def test_bucket_by_tag_01256():
    p = Product_01256("s1", 100, ["a"])
    assert bucket_by_tag_01256([p]) == {"a": ["s1"]}
