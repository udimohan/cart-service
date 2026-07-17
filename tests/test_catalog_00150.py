"""Tests for catalog_00150."""

import pytest

from cartservice.generated.catalog_00150 import (
    Product_00150,
    bucket_by_tag_00150,
    is_valid_sku_00150,
    price_with_tax_00150,
)


def test_price_with_tax_00150():
    assert price_with_tax_00150(1000, 500) == 1050


def test_price_with_tax_negative_00150():
    with pytest.raises(ValueError):
        price_with_tax_00150(1000, -1)


def test_is_valid_sku_00150():
    assert is_valid_sku_00150("abc123")
    assert not is_valid_sku_00150("")


def test_bucket_by_tag_00150():
    p = Product_00150("s1", 100, ["a"])
    assert bucket_by_tag_00150([p]) == {"a": ["s1"]}
