"""Tests for catalog_01317."""

import pytest

from cartservice.generated.catalog_01317 import (
    Product_01317,
    bucket_by_tag_01317,
    is_valid_sku_01317,
    price_with_tax_01317,
)


def test_price_with_tax_01317():
    assert price_with_tax_01317(1000, 500) == 1050


def test_price_with_tax_negative_01317():
    with pytest.raises(ValueError):
        price_with_tax_01317(1000, -1)


def test_is_valid_sku_01317():
    assert is_valid_sku_01317("abc123")
    assert not is_valid_sku_01317("")


def test_bucket_by_tag_01317():
    p = Product_01317("s1", 100, ["a"])
    assert bucket_by_tag_01317([p]) == {"a": ["s1"]}
