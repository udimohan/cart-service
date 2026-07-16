"""Tests for catalog_01512."""

import pytest

from cartservice.generated.catalog_01512 import (
    Product_01512,
    bucket_by_tag_01512,
    is_valid_sku_01512,
    price_with_tax_01512,
)


def test_price_with_tax_01512():
    assert price_with_tax_01512(1000, 500) == 1050


def test_price_with_tax_negative_01512():
    with pytest.raises(ValueError):
        price_with_tax_01512(1000, -1)


def test_is_valid_sku_01512():
    assert is_valid_sku_01512("abc123")
    assert not is_valid_sku_01512("")


def test_bucket_by_tag_01512():
    p = Product_01512("s1", 100, ["a"])
    assert bucket_by_tag_01512([p]) == {"a": ["s1"]}
