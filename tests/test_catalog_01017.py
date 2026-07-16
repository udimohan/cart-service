"""Tests for catalog_01017."""

import pytest

from cartservice.generated.catalog_01017 import (
    Product_01017,
    bucket_by_tag_01017,
    is_valid_sku_01017,
    price_with_tax_01017,
)


def test_price_with_tax_01017():
    assert price_with_tax_01017(1000, 500) == 1050


def test_price_with_tax_negative_01017():
    with pytest.raises(ValueError):
        price_with_tax_01017(1000, -1)


def test_is_valid_sku_01017():
    assert is_valid_sku_01017("abc123")
    assert not is_valid_sku_01017("")


def test_bucket_by_tag_01017():
    p = Product_01017("s1", 100, ["a"])
    assert bucket_by_tag_01017([p]) == {"a": ["s1"]}
