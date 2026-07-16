"""Tests for catalog_01153."""

import pytest

from cartservice.generated.catalog_01153 import (
    Product_01153,
    bucket_by_tag_01153,
    is_valid_sku_01153,
    price_with_tax_01153,
)


def test_price_with_tax_01153():
    assert price_with_tax_01153(1000, 500) == 1050


def test_price_with_tax_negative_01153():
    with pytest.raises(ValueError):
        price_with_tax_01153(1000, -1)


def test_is_valid_sku_01153():
    assert is_valid_sku_01153("abc123")
    assert not is_valid_sku_01153("")


def test_bucket_by_tag_01153():
    p = Product_01153("s1", 100, ["a"])
    assert bucket_by_tag_01153([p]) == {"a": ["s1"]}
