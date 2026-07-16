"""Tests for catalog_00296."""

import pytest

from cartservice.generated.catalog_00296 import (
    Product_00296,
    bucket_by_tag_00296,
    is_valid_sku_00296,
    price_with_tax_00296,
)


def test_price_with_tax_00296():
    assert price_with_tax_00296(1000, 500) == 1050


def test_price_with_tax_negative_00296():
    with pytest.raises(ValueError):
        price_with_tax_00296(1000, -1)


def test_is_valid_sku_00296():
    assert is_valid_sku_00296("abc123")
    assert not is_valid_sku_00296("")


def test_bucket_by_tag_00296():
    p = Product_00296("s1", 100, ["a"])
    assert bucket_by_tag_00296([p]) == {"a": ["s1"]}
