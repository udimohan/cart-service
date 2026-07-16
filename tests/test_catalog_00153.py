"""Tests for catalog_00153."""

import pytest

from cartservice.generated.catalog_00153 import (
    Product_00153,
    bucket_by_tag_00153,
    is_valid_sku_00153,
    price_with_tax_00153,
)


def test_price_with_tax_00153():
    assert price_with_tax_00153(1000, 500) == 1050


def test_price_with_tax_negative_00153():
    with pytest.raises(ValueError):
        price_with_tax_00153(1000, -1)


def test_is_valid_sku_00153():
    assert is_valid_sku_00153("abc123")
    assert not is_valid_sku_00153("")


def test_bucket_by_tag_00153():
    p = Product_00153("s1", 100, ["a"])
    assert bucket_by_tag_00153([p]) == {"a": ["s1"]}
