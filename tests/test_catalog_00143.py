"""Tests for catalog_00143."""

import pytest

from cartservice.generated.catalog_00143 import (
    Product_00143,
    bucket_by_tag_00143,
    is_valid_sku_00143,
    price_with_tax_00143,
)


def test_price_with_tax_00143():
    assert price_with_tax_00143(1000, 500) == 1050


def test_price_with_tax_negative_00143():
    with pytest.raises(ValueError):
        price_with_tax_00143(1000, -1)


def test_is_valid_sku_00143():
    assert is_valid_sku_00143("abc123")
    assert not is_valid_sku_00143("")


def test_bucket_by_tag_00143():
    p = Product_00143("s1", 100, ["a"])
    assert bucket_by_tag_00143([p]) == {"a": ["s1"]}
