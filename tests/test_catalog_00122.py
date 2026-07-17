"""Tests for catalog_00122."""

import pytest

from cartservice.generated.catalog_00122 import (
    Product_00122,
    bucket_by_tag_00122,
    is_valid_sku_00122,
    price_with_tax_00122,
)


def test_price_with_tax_00122():
    assert price_with_tax_00122(1000, 500) == 1050


def test_price_with_tax_negative_00122():
    with pytest.raises(ValueError):
        price_with_tax_00122(1000, -1)


def test_is_valid_sku_00122():
    assert is_valid_sku_00122("abc123")
    assert not is_valid_sku_00122("")


def test_bucket_by_tag_00122():
    p = Product_00122("s1", 100, ["a"])
    assert bucket_by_tag_00122([p]) == {"a": ["s1"]}
