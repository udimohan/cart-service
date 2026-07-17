"""Tests for catalog_01729."""

import pytest

from cartservice.generated.catalog_01729 import (
    Product_01729,
    bucket_by_tag_01729,
    is_valid_sku_01729,
    price_with_tax_01729,
)


def test_price_with_tax_01729():
    assert price_with_tax_01729(1000, 500) == 1050


def test_price_with_tax_negative_01729():
    with pytest.raises(ValueError):
        price_with_tax_01729(1000, -1)


def test_is_valid_sku_01729():
    assert is_valid_sku_01729("abc123")
    assert not is_valid_sku_01729("")


def test_bucket_by_tag_01729():
    p = Product_01729("s1", 100, ["a"])
    assert bucket_by_tag_01729([p]) == {"a": ["s1"]}
