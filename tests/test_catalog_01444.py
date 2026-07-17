"""Tests for catalog_01444."""

import pytest

from cartservice.generated.catalog_01444 import (
    Product_01444,
    bucket_by_tag_01444,
    is_valid_sku_01444,
    price_with_tax_01444,
)


def test_price_with_tax_01444():
    assert price_with_tax_01444(1000, 500) == 1050


def test_price_with_tax_negative_01444():
    with pytest.raises(ValueError):
        price_with_tax_01444(1000, -1)


def test_is_valid_sku_01444():
    assert is_valid_sku_01444("abc123")
    assert not is_valid_sku_01444("")


def test_bucket_by_tag_01444():
    p = Product_01444("s1", 100, ["a"])
    assert bucket_by_tag_01444([p]) == {"a": ["s1"]}
