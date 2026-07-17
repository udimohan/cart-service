"""Tests for catalog_00088."""

import pytest

from cartservice.generated.catalog_00088 import (
    Product_00088,
    bucket_by_tag_00088,
    is_valid_sku_00088,
    price_with_tax_00088,
)


def test_price_with_tax_00088():
    assert price_with_tax_00088(1000, 500) == 1050


def test_price_with_tax_negative_00088():
    with pytest.raises(ValueError):
        price_with_tax_00088(1000, -1)


def test_is_valid_sku_00088():
    assert is_valid_sku_00088("abc123")
    assert not is_valid_sku_00088("")


def test_bucket_by_tag_00088():
    p = Product_00088("s1", 100, ["a"])
    assert bucket_by_tag_00088([p]) == {"a": ["s1"]}
