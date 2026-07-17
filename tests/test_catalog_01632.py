"""Tests for catalog_01632."""

import pytest

from cartservice.generated.catalog_01632 import (
    Product_01632,
    bucket_by_tag_01632,
    is_valid_sku_01632,
    price_with_tax_01632,
)


def test_price_with_tax_01632():
    assert price_with_tax_01632(1000, 500) == 1050


def test_price_with_tax_negative_01632():
    with pytest.raises(ValueError):
        price_with_tax_01632(1000, -1)


def test_is_valid_sku_01632():
    assert is_valid_sku_01632("abc123")
    assert not is_valid_sku_01632("")


def test_bucket_by_tag_01632():
    p = Product_01632("s1", 100, ["a"])
    assert bucket_by_tag_01632([p]) == {"a": ["s1"]}
