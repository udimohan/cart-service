"""Tests for catalog_01271."""

import pytest

from cartservice.generated.catalog_01271 import (
    Product_01271,
    bucket_by_tag_01271,
    is_valid_sku_01271,
    price_with_tax_01271,
)


def test_price_with_tax_01271():
    assert price_with_tax_01271(1000, 500) == 1050


def test_price_with_tax_negative_01271():
    with pytest.raises(ValueError):
        price_with_tax_01271(1000, -1)


def test_is_valid_sku_01271():
    assert is_valid_sku_01271("abc123")
    assert not is_valid_sku_01271("")


def test_bucket_by_tag_01271():
    p = Product_01271("s1", 100, ["a"])
    assert bucket_by_tag_01271([p]) == {"a": ["s1"]}
