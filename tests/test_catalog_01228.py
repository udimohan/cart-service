"""Tests for catalog_01228."""

import pytest

from cartservice.generated.catalog_01228 import (
    Product_01228,
    bucket_by_tag_01228,
    is_valid_sku_01228,
    price_with_tax_01228,
)


def test_price_with_tax_01228():
    assert price_with_tax_01228(1000, 500) == 1050


def test_price_with_tax_negative_01228():
    with pytest.raises(ValueError):
        price_with_tax_01228(1000, -1)


def test_is_valid_sku_01228():
    assert is_valid_sku_01228("abc123")
    assert not is_valid_sku_01228("")


def test_bucket_by_tag_01228():
    p = Product_01228("s1", 100, ["a"])
    assert bucket_by_tag_01228([p]) == {"a": ["s1"]}
