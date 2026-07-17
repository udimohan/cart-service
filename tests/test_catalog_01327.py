"""Tests for catalog_01327."""

import pytest

from cartservice.generated.catalog_01327 import (
    Product_01327,
    bucket_by_tag_01327,
    is_valid_sku_01327,
    price_with_tax_01327,
)


def test_price_with_tax_01327():
    assert price_with_tax_01327(1000, 500) == 1050


def test_price_with_tax_negative_01327():
    with pytest.raises(ValueError):
        price_with_tax_01327(1000, -1)


def test_is_valid_sku_01327():
    assert is_valid_sku_01327("abc123")
    assert not is_valid_sku_01327("")


def test_bucket_by_tag_01327():
    p = Product_01327("s1", 100, ["a"])
    assert bucket_by_tag_01327([p]) == {"a": ["s1"]}
