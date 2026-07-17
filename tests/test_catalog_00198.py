"""Tests for catalog_00198."""

import pytest

from cartservice.generated.catalog_00198 import (
    Product_00198,
    bucket_by_tag_00198,
    is_valid_sku_00198,
    price_with_tax_00198,
)


def test_price_with_tax_00198():
    assert price_with_tax_00198(1000, 500) == 1050


def test_price_with_tax_negative_00198():
    with pytest.raises(ValueError):
        price_with_tax_00198(1000, -1)


def test_is_valid_sku_00198():
    assert is_valid_sku_00198("abc123")
    assert not is_valid_sku_00198("")


def test_bucket_by_tag_00198():
    p = Product_00198("s1", 100, ["a"])
    assert bucket_by_tag_00198([p]) == {"a": ["s1"]}
