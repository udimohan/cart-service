"""Tests for catalog_01683."""

import pytest

from cartservice.generated.catalog_01683 import (
    Product_01683,
    bucket_by_tag_01683,
    is_valid_sku_01683,
    price_with_tax_01683,
)


def test_price_with_tax_01683():
    assert price_with_tax_01683(1000, 500) == 1050


def test_price_with_tax_negative_01683():
    with pytest.raises(ValueError):
        price_with_tax_01683(1000, -1)


def test_is_valid_sku_01683():
    assert is_valid_sku_01683("abc123")
    assert not is_valid_sku_01683("")


def test_bucket_by_tag_01683():
    p = Product_01683("s1", 100, ["a"])
    assert bucket_by_tag_01683([p]) == {"a": ["s1"]}
