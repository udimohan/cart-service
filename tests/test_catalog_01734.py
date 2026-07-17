"""Tests for catalog_01734."""

import pytest

from cartservice.generated.catalog_01734 import (
    Product_01734,
    bucket_by_tag_01734,
    is_valid_sku_01734,
    price_with_tax_01734,
)


def test_price_with_tax_01734():
    assert price_with_tax_01734(1000, 500) == 1050


def test_price_with_tax_negative_01734():
    with pytest.raises(ValueError):
        price_with_tax_01734(1000, -1)


def test_is_valid_sku_01734():
    assert is_valid_sku_01734("abc123")
    assert not is_valid_sku_01734("")


def test_bucket_by_tag_01734():
    p = Product_01734("s1", 100, ["a"])
    assert bucket_by_tag_01734([p]) == {"a": ["s1"]}
