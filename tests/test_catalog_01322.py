"""Tests for catalog_01322."""

import pytest

from cartservice.generated.catalog_01322 import (
    Product_01322,
    bucket_by_tag_01322,
    is_valid_sku_01322,
    price_with_tax_01322,
)


def test_price_with_tax_01322():
    assert price_with_tax_01322(1000, 500) == 1050


def test_price_with_tax_negative_01322():
    with pytest.raises(ValueError):
        price_with_tax_01322(1000, -1)


def test_is_valid_sku_01322():
    assert is_valid_sku_01322("abc123")
    assert not is_valid_sku_01322("")


def test_bucket_by_tag_01322():
    p = Product_01322("s1", 100, ["a"])
    assert bucket_by_tag_01322([p]) == {"a": ["s1"]}
