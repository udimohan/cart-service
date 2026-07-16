"""Tests for catalog_00683."""

import pytest

from cartservice.generated.catalog_00683 import (
    Product_00683,
    bucket_by_tag_00683,
    is_valid_sku_00683,
    price_with_tax_00683,
)


def test_price_with_tax_00683():
    assert price_with_tax_00683(1000, 500) == 1050


def test_price_with_tax_negative_00683():
    with pytest.raises(ValueError):
        price_with_tax_00683(1000, -1)


def test_is_valid_sku_00683():
    assert is_valid_sku_00683("abc123")
    assert not is_valid_sku_00683("")


def test_bucket_by_tag_00683():
    p = Product_00683("s1", 100, ["a"])
    assert bucket_by_tag_00683([p]) == {"a": ["s1"]}
