"""Tests for catalog_01469."""

import pytest

from cartservice.generated.catalog_01469 import (
    Product_01469,
    bucket_by_tag_01469,
    is_valid_sku_01469,
    price_with_tax_01469,
)


def test_price_with_tax_01469():
    assert price_with_tax_01469(1000, 500) == 1050


def test_price_with_tax_negative_01469():
    with pytest.raises(ValueError):
        price_with_tax_01469(1000, -1)


def test_is_valid_sku_01469():
    assert is_valid_sku_01469("abc123")
    assert not is_valid_sku_01469("")


def test_bucket_by_tag_01469():
    p = Product_01469("s1", 100, ["a"])
    assert bucket_by_tag_01469([p]) == {"a": ["s1"]}
