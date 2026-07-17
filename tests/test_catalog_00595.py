"""Tests for catalog_00595."""

import pytest

from cartservice.generated.catalog_00595 import (
    Product_00595,
    bucket_by_tag_00595,
    is_valid_sku_00595,
    price_with_tax_00595,
)


def test_price_with_tax_00595():
    assert price_with_tax_00595(1000, 500) == 1050


def test_price_with_tax_negative_00595():
    with pytest.raises(ValueError):
        price_with_tax_00595(1000, -1)


def test_is_valid_sku_00595():
    assert is_valid_sku_00595("abc123")
    assert not is_valid_sku_00595("")


def test_bucket_by_tag_00595():
    p = Product_00595("s1", 100, ["a"])
    assert bucket_by_tag_00595([p]) == {"a": ["s1"]}
