"""Tests for catalog_01602."""

import pytest

from cartservice.generated.catalog_01602 import (
    Product_01602,
    bucket_by_tag_01602,
    is_valid_sku_01602,
    price_with_tax_01602,
)


def test_price_with_tax_01602():
    assert price_with_tax_01602(1000, 500) == 1050


def test_price_with_tax_negative_01602():
    with pytest.raises(ValueError):
        price_with_tax_01602(1000, -1)


def test_is_valid_sku_01602():
    assert is_valid_sku_01602("abc123")
    assert not is_valid_sku_01602("")


def test_bucket_by_tag_01602():
    p = Product_01602("s1", 100, ["a"])
    assert bucket_by_tag_01602([p]) == {"a": ["s1"]}
