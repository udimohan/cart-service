"""Tests for catalog_01242."""

import pytest

from cartservice.generated.catalog_01242 import (
    Product_01242,
    bucket_by_tag_01242,
    is_valid_sku_01242,
    price_with_tax_01242,
)


def test_price_with_tax_01242():
    assert price_with_tax_01242(1000, 500) == 1050


def test_price_with_tax_negative_01242():
    with pytest.raises(ValueError):
        price_with_tax_01242(1000, -1)


def test_is_valid_sku_01242():
    assert is_valid_sku_01242("abc123")
    assert not is_valid_sku_01242("")


def test_bucket_by_tag_01242():
    p = Product_01242("s1", 100, ["a"])
    assert bucket_by_tag_01242([p]) == {"a": ["s1"]}
