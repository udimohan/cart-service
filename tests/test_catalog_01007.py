"""Tests for catalog_01007."""

import pytest

from cartservice.generated.catalog_01007 import (
    Product_01007,
    bucket_by_tag_01007,
    is_valid_sku_01007,
    price_with_tax_01007,
)


def test_price_with_tax_01007():
    assert price_with_tax_01007(1000, 500) == 1050


def test_price_with_tax_negative_01007():
    with pytest.raises(ValueError):
        price_with_tax_01007(1000, -1)


def test_is_valid_sku_01007():
    assert is_valid_sku_01007("abc123")
    assert not is_valid_sku_01007("")


def test_bucket_by_tag_01007():
    p = Product_01007("s1", 100, ["a"])
    assert bucket_by_tag_01007([p]) == {"a": ["s1"]}
