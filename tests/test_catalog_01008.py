"""Tests for catalog_01008."""

import pytest

from cartservice.generated.catalog_01008 import (
    Product_01008,
    bucket_by_tag_01008,
    is_valid_sku_01008,
    price_with_tax_01008,
)


def test_price_with_tax_01008():
    assert price_with_tax_01008(1000, 500) == 1050


def test_price_with_tax_negative_01008():
    with pytest.raises(ValueError):
        price_with_tax_01008(1000, -1)


def test_is_valid_sku_01008():
    assert is_valid_sku_01008("abc123")
    assert not is_valid_sku_01008("")


def test_bucket_by_tag_01008():
    p = Product_01008("s1", 100, ["a"])
    assert bucket_by_tag_01008([p]) == {"a": ["s1"]}
