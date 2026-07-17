"""Tests for catalog_00194."""

import pytest

from cartservice.generated.catalog_00194 import (
    Product_00194,
    bucket_by_tag_00194,
    is_valid_sku_00194,
    price_with_tax_00194,
)


def test_price_with_tax_00194():
    assert price_with_tax_00194(1000, 500) == 1050


def test_price_with_tax_negative_00194():
    with pytest.raises(ValueError):
        price_with_tax_00194(1000, -1)


def test_is_valid_sku_00194():
    assert is_valid_sku_00194("abc123")
    assert not is_valid_sku_00194("")


def test_bucket_by_tag_00194():
    p = Product_00194("s1", 100, ["a"])
    assert bucket_by_tag_00194([p]) == {"a": ["s1"]}
