"""Tests for catalog_01584."""

import pytest

from cartservice.generated.catalog_01584 import (
    Product_01584,
    bucket_by_tag_01584,
    is_valid_sku_01584,
    price_with_tax_01584,
)


def test_price_with_tax_01584():
    assert price_with_tax_01584(1000, 500) == 1050


def test_price_with_tax_negative_01584():
    with pytest.raises(ValueError):
        price_with_tax_01584(1000, -1)


def test_is_valid_sku_01584():
    assert is_valid_sku_01584("abc123")
    assert not is_valid_sku_01584("")


def test_bucket_by_tag_01584():
    p = Product_01584("s1", 100, ["a"])
    assert bucket_by_tag_01584([p]) == {"a": ["s1"]}
