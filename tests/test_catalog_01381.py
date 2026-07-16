"""Tests for catalog_01381."""

import pytest

from cartservice.generated.catalog_01381 import (
    Product_01381,
    bucket_by_tag_01381,
    is_valid_sku_01381,
    price_with_tax_01381,
)


def test_price_with_tax_01381():
    assert price_with_tax_01381(1000, 500) == 1050


def test_price_with_tax_negative_01381():
    with pytest.raises(ValueError):
        price_with_tax_01381(1000, -1)


def test_is_valid_sku_01381():
    assert is_valid_sku_01381("abc123")
    assert not is_valid_sku_01381("")


def test_bucket_by_tag_01381():
    p = Product_01381("s1", 100, ["a"])
    assert bucket_by_tag_01381([p]) == {"a": ["s1"]}
