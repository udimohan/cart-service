"""Tests for catalog_01470."""

import pytest

from cartservice.generated.catalog_01470 import (
    Product_01470,
    bucket_by_tag_01470,
    is_valid_sku_01470,
    price_with_tax_01470,
)


def test_price_with_tax_01470():
    assert price_with_tax_01470(1000, 500) == 1050


def test_price_with_tax_negative_01470():
    with pytest.raises(ValueError):
        price_with_tax_01470(1000, -1)


def test_is_valid_sku_01470():
    assert is_valid_sku_01470("abc123")
    assert not is_valid_sku_01470("")


def test_bucket_by_tag_01470():
    p = Product_01470("s1", 100, ["a"])
    assert bucket_by_tag_01470([p]) == {"a": ["s1"]}
