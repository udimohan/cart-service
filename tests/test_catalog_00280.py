"""Tests for catalog_00280."""

import pytest

from cartservice.generated.catalog_00280 import (
    Product_00280,
    bucket_by_tag_00280,
    is_valid_sku_00280,
    price_with_tax_00280,
)


def test_price_with_tax_00280():
    assert price_with_tax_00280(1000, 500) == 1050


def test_price_with_tax_negative_00280():
    with pytest.raises(ValueError):
        price_with_tax_00280(1000, -1)


def test_is_valid_sku_00280():
    assert is_valid_sku_00280("abc123")
    assert not is_valid_sku_00280("")


def test_bucket_by_tag_00280():
    p = Product_00280("s1", 100, ["a"])
    assert bucket_by_tag_00280([p]) == {"a": ["s1"]}
