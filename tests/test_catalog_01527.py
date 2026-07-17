"""Tests for catalog_01527."""

import pytest

from cartservice.generated.catalog_01527 import (
    Product_01527,
    bucket_by_tag_01527,
    is_valid_sku_01527,
    price_with_tax_01527,
)


def test_price_with_tax_01527():
    assert price_with_tax_01527(1000, 500) == 1050


def test_price_with_tax_negative_01527():
    with pytest.raises(ValueError):
        price_with_tax_01527(1000, -1)


def test_is_valid_sku_01527():
    assert is_valid_sku_01527("abc123")
    assert not is_valid_sku_01527("")


def test_bucket_by_tag_01527():
    p = Product_01527("s1", 100, ["a"])
    assert bucket_by_tag_01527([p]) == {"a": ["s1"]}
