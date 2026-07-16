"""Tests for catalog_00036."""

import pytest

from cartservice.generated.catalog_00036 import (
    Product_00036,
    bucket_by_tag_00036,
    is_valid_sku_00036,
    price_with_tax_00036,
)


def test_price_with_tax_00036():
    assert price_with_tax_00036(1000, 500) == 1050


def test_price_with_tax_negative_00036():
    with pytest.raises(ValueError):
        price_with_tax_00036(1000, -1)


def test_is_valid_sku_00036():
    assert is_valid_sku_00036("abc123")
    assert not is_valid_sku_00036("")


def test_bucket_by_tag_00036():
    p = Product_00036("s1", 100, ["a"])
    assert bucket_by_tag_00036([p]) == {"a": ["s1"]}
