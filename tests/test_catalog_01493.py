"""Tests for catalog_01493."""

import pytest

from cartservice.generated.catalog_01493 import (
    Product_01493,
    bucket_by_tag_01493,
    is_valid_sku_01493,
    price_with_tax_01493,
)


def test_price_with_tax_01493():
    assert price_with_tax_01493(1000, 500) == 1050


def test_price_with_tax_negative_01493():
    with pytest.raises(ValueError):
        price_with_tax_01493(1000, -1)


def test_is_valid_sku_01493():
    assert is_valid_sku_01493("abc123")
    assert not is_valid_sku_01493("")


def test_bucket_by_tag_01493():
    p = Product_01493("s1", 100, ["a"])
    assert bucket_by_tag_01493([p]) == {"a": ["s1"]}
