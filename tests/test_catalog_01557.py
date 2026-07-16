"""Tests for catalog_01557."""

import pytest

from cartservice.generated.catalog_01557 import (
    Product_01557,
    bucket_by_tag_01557,
    is_valid_sku_01557,
    price_with_tax_01557,
)


def test_price_with_tax_01557():
    assert price_with_tax_01557(1000, 500) == 1050


def test_price_with_tax_negative_01557():
    with pytest.raises(ValueError):
        price_with_tax_01557(1000, -1)


def test_is_valid_sku_01557():
    assert is_valid_sku_01557("abc123")
    assert not is_valid_sku_01557("")


def test_bucket_by_tag_01557():
    p = Product_01557("s1", 100, ["a"])
    assert bucket_by_tag_01557([p]) == {"a": ["s1"]}
