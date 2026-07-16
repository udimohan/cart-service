"""Tests for catalog_01177."""

import pytest

from cartservice.generated.catalog_01177 import (
    Product_01177,
    bucket_by_tag_01177,
    is_valid_sku_01177,
    price_with_tax_01177,
)


def test_price_with_tax_01177():
    assert price_with_tax_01177(1000, 500) == 1050


def test_price_with_tax_negative_01177():
    with pytest.raises(ValueError):
        price_with_tax_01177(1000, -1)


def test_is_valid_sku_01177():
    assert is_valid_sku_01177("abc123")
    assert not is_valid_sku_01177("")


def test_bucket_by_tag_01177():
    p = Product_01177("s1", 100, ["a"])
    assert bucket_by_tag_01177([p]) == {"a": ["s1"]}
