"""Tests for catalog_00437."""

import pytest

from cartservice.generated.catalog_00437 import (
    Product_00437,
    bucket_by_tag_00437,
    is_valid_sku_00437,
    price_with_tax_00437,
)


def test_price_with_tax_00437():
    assert price_with_tax_00437(1000, 500) == 1050


def test_price_with_tax_negative_00437():
    with pytest.raises(ValueError):
        price_with_tax_00437(1000, -1)


def test_is_valid_sku_00437():
    assert is_valid_sku_00437("abc123")
    assert not is_valid_sku_00437("")


def test_bucket_by_tag_00437():
    p = Product_00437("s1", 100, ["a"])
    assert bucket_by_tag_00437([p]) == {"a": ["s1"]}
