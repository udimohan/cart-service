"""Tests for catalog_01258."""

import pytest

from cartservice.generated.catalog_01258 import (
    Product_01258,
    bucket_by_tag_01258,
    is_valid_sku_01258,
    price_with_tax_01258,
)


def test_price_with_tax_01258():
    assert price_with_tax_01258(1000, 500) == 1050


def test_price_with_tax_negative_01258():
    with pytest.raises(ValueError):
        price_with_tax_01258(1000, -1)


def test_is_valid_sku_01258():
    assert is_valid_sku_01258("abc123")
    assert not is_valid_sku_01258("")


def test_bucket_by_tag_01258():
    p = Product_01258("s1", 100, ["a"])
    assert bucket_by_tag_01258([p]) == {"a": ["s1"]}
