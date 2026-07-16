"""Tests for catalog_01236."""

import pytest

from cartservice.generated.catalog_01236 import (
    Product_01236,
    bucket_by_tag_01236,
    is_valid_sku_01236,
    price_with_tax_01236,
)


def test_price_with_tax_01236():
    assert price_with_tax_01236(1000, 500) == 1050


def test_price_with_tax_negative_01236():
    with pytest.raises(ValueError):
        price_with_tax_01236(1000, -1)


def test_is_valid_sku_01236():
    assert is_valid_sku_01236("abc123")
    assert not is_valid_sku_01236("")


def test_bucket_by_tag_01236():
    p = Product_01236("s1", 100, ["a"])
    assert bucket_by_tag_01236([p]) == {"a": ["s1"]}
