"""Tests for catalog_01306."""

import pytest

from cartservice.generated.catalog_01306 import (
    Product_01306,
    bucket_by_tag_01306,
    is_valid_sku_01306,
    price_with_tax_01306,
)


def test_price_with_tax_01306():
    assert price_with_tax_01306(1000, 500) == 1050


def test_price_with_tax_negative_01306():
    with pytest.raises(ValueError):
        price_with_tax_01306(1000, -1)


def test_is_valid_sku_01306():
    assert is_valid_sku_01306("abc123")
    assert not is_valid_sku_01306("")


def test_bucket_by_tag_01306():
    p = Product_01306("s1", 100, ["a"])
    assert bucket_by_tag_01306([p]) == {"a": ["s1"]}
