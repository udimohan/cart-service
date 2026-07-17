"""Tests for catalog_01685."""

import pytest

from cartservice.generated.catalog_01685 import (
    Product_01685,
    bucket_by_tag_01685,
    is_valid_sku_01685,
    price_with_tax_01685,
)


def test_price_with_tax_01685():
    assert price_with_tax_01685(1000, 500) == 1050


def test_price_with_tax_negative_01685():
    with pytest.raises(ValueError):
        price_with_tax_01685(1000, -1)


def test_is_valid_sku_01685():
    assert is_valid_sku_01685("abc123")
    assert not is_valid_sku_01685("")


def test_bucket_by_tag_01685():
    p = Product_01685("s1", 100, ["a"])
    assert bucket_by_tag_01685([p]) == {"a": ["s1"]}
