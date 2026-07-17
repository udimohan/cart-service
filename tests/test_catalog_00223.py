"""Tests for catalog_00223."""

import pytest

from cartservice.generated.catalog_00223 import (
    Product_00223,
    bucket_by_tag_00223,
    is_valid_sku_00223,
    price_with_tax_00223,
)


def test_price_with_tax_00223():
    assert price_with_tax_00223(1000, 500) == 1050


def test_price_with_tax_negative_00223():
    with pytest.raises(ValueError):
        price_with_tax_00223(1000, -1)


def test_is_valid_sku_00223():
    assert is_valid_sku_00223("abc123")
    assert not is_valid_sku_00223("")


def test_bucket_by_tag_00223():
    p = Product_00223("s1", 100, ["a"])
    assert bucket_by_tag_00223([p]) == {"a": ["s1"]}
