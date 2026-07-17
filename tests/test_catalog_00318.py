"""Tests for catalog_00318."""

import pytest

from cartservice.generated.catalog_00318 import (
    Product_00318,
    bucket_by_tag_00318,
    is_valid_sku_00318,
    price_with_tax_00318,
)


def test_price_with_tax_00318():
    assert price_with_tax_00318(1000, 500) == 1050


def test_price_with_tax_negative_00318():
    with pytest.raises(ValueError):
        price_with_tax_00318(1000, -1)


def test_is_valid_sku_00318():
    assert is_valid_sku_00318("abc123")
    assert not is_valid_sku_00318("")


def test_bucket_by_tag_00318():
    p = Product_00318("s1", 100, ["a"])
    assert bucket_by_tag_00318([p]) == {"a": ["s1"]}
