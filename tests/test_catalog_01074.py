"""Tests for catalog_01074."""

import pytest

from cartservice.generated.catalog_01074 import (
    Product_01074,
    bucket_by_tag_01074,
    is_valid_sku_01074,
    price_with_tax_01074,
)


def test_price_with_tax_01074():
    assert price_with_tax_01074(1000, 500) == 1050


def test_price_with_tax_negative_01074():
    with pytest.raises(ValueError):
        price_with_tax_01074(1000, -1)


def test_is_valid_sku_01074():
    assert is_valid_sku_01074("abc123")
    assert not is_valid_sku_01074("")


def test_bucket_by_tag_01074():
    p = Product_01074("s1", 100, ["a"])
    assert bucket_by_tag_01074([p]) == {"a": ["s1"]}
