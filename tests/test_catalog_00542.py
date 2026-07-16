"""Tests for catalog_00542."""

import pytest

from cartservice.generated.catalog_00542 import (
    Product_00542,
    bucket_by_tag_00542,
    is_valid_sku_00542,
    price_with_tax_00542,
)


def test_price_with_tax_00542():
    assert price_with_tax_00542(1000, 500) == 1050


def test_price_with_tax_negative_00542():
    with pytest.raises(ValueError):
        price_with_tax_00542(1000, -1)


def test_is_valid_sku_00542():
    assert is_valid_sku_00542("abc123")
    assert not is_valid_sku_00542("")


def test_bucket_by_tag_00542():
    p = Product_00542("s1", 100, ["a"])
    assert bucket_by_tag_00542([p]) == {"a": ["s1"]}
