"""Tests for catalog_00518."""

import pytest

from cartservice.generated.catalog_00518 import (
    Product_00518,
    bucket_by_tag_00518,
    is_valid_sku_00518,
    price_with_tax_00518,
)


def test_price_with_tax_00518():
    assert price_with_tax_00518(1000, 500) == 1050


def test_price_with_tax_negative_00518():
    with pytest.raises(ValueError):
        price_with_tax_00518(1000, -1)


def test_is_valid_sku_00518():
    assert is_valid_sku_00518("abc123")
    assert not is_valid_sku_00518("")


def test_bucket_by_tag_00518():
    p = Product_00518("s1", 100, ["a"])
    assert bucket_by_tag_00518([p]) == {"a": ["s1"]}
