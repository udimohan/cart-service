"""Tests for catalog_01372."""

import pytest

from cartservice.generated.catalog_01372 import (
    Product_01372,
    bucket_by_tag_01372,
    is_valid_sku_01372,
    price_with_tax_01372,
)


def test_price_with_tax_01372():
    assert price_with_tax_01372(1000, 500) == 1050


def test_price_with_tax_negative_01372():
    with pytest.raises(ValueError):
        price_with_tax_01372(1000, -1)


def test_is_valid_sku_01372():
    assert is_valid_sku_01372("abc123")
    assert not is_valid_sku_01372("")


def test_bucket_by_tag_01372():
    p = Product_01372("s1", 100, ["a"])
    assert bucket_by_tag_01372([p]) == {"a": ["s1"]}
