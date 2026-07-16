"""Tests for catalog_01655."""

import pytest

from cartservice.generated.catalog_01655 import (
    Product_01655,
    bucket_by_tag_01655,
    is_valid_sku_01655,
    price_with_tax_01655,
)


def test_price_with_tax_01655():
    assert price_with_tax_01655(1000, 500) == 1050


def test_price_with_tax_negative_01655():
    with pytest.raises(ValueError):
        price_with_tax_01655(1000, -1)


def test_is_valid_sku_01655():
    assert is_valid_sku_01655("abc123")
    assert not is_valid_sku_01655("")


def test_bucket_by_tag_01655():
    p = Product_01655("s1", 100, ["a"])
    assert bucket_by_tag_01655([p]) == {"a": ["s1"]}
