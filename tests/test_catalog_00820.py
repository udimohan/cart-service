"""Tests for catalog_00820."""

import pytest

from cartservice.generated.catalog_00820 import (
    Product_00820,
    bucket_by_tag_00820,
    is_valid_sku_00820,
    price_with_tax_00820,
)


def test_price_with_tax_00820():
    assert price_with_tax_00820(1000, 500) == 1050


def test_price_with_tax_negative_00820():
    with pytest.raises(ValueError):
        price_with_tax_00820(1000, -1)


def test_is_valid_sku_00820():
    assert is_valid_sku_00820("abc123")
    assert not is_valid_sku_00820("")


def test_bucket_by_tag_00820():
    p = Product_00820("s1", 100, ["a"])
    assert bucket_by_tag_00820([p]) == {"a": ["s1"]}
