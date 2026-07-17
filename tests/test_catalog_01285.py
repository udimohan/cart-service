"""Tests for catalog_01285."""

import pytest

from cartservice.generated.catalog_01285 import (
    Product_01285,
    bucket_by_tag_01285,
    is_valid_sku_01285,
    price_with_tax_01285,
)


def test_price_with_tax_01285():
    assert price_with_tax_01285(1000, 500) == 1050


def test_price_with_tax_negative_01285():
    with pytest.raises(ValueError):
        price_with_tax_01285(1000, -1)


def test_is_valid_sku_01285():
    assert is_valid_sku_01285("abc123")
    assert not is_valid_sku_01285("")


def test_bucket_by_tag_01285():
    p = Product_01285("s1", 100, ["a"])
    assert bucket_by_tag_01285([p]) == {"a": ["s1"]}
