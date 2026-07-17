"""Tests for catalog_01513."""

import pytest

from cartservice.generated.catalog_01513 import (
    Product_01513,
    bucket_by_tag_01513,
    is_valid_sku_01513,
    price_with_tax_01513,
)


def test_price_with_tax_01513():
    assert price_with_tax_01513(1000, 500) == 1050


def test_price_with_tax_negative_01513():
    with pytest.raises(ValueError):
        price_with_tax_01513(1000, -1)


def test_is_valid_sku_01513():
    assert is_valid_sku_01513("abc123")
    assert not is_valid_sku_01513("")


def test_bucket_by_tag_01513():
    p = Product_01513("s1", 100, ["a"])
    assert bucket_by_tag_01513([p]) == {"a": ["s1"]}
