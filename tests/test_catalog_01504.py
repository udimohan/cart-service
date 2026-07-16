"""Tests for catalog_01504."""

import pytest

from cartservice.generated.catalog_01504 import (
    Product_01504,
    bucket_by_tag_01504,
    is_valid_sku_01504,
    price_with_tax_01504,
)


def test_price_with_tax_01504():
    assert price_with_tax_01504(1000, 500) == 1050


def test_price_with_tax_negative_01504():
    with pytest.raises(ValueError):
        price_with_tax_01504(1000, -1)


def test_is_valid_sku_01504():
    assert is_valid_sku_01504("abc123")
    assert not is_valid_sku_01504("")


def test_bucket_by_tag_01504():
    p = Product_01504("s1", 100, ["a"])
    assert bucket_by_tag_01504([p]) == {"a": ["s1"]}
