"""Tests for catalog_00005."""

import pytest

from cartservice.generated.catalog_00005 import (
    Product_00005,
    bucket_by_tag_00005,
    is_valid_sku_00005,
    price_with_tax_00005,
)


def test_price_with_tax_00005():
    assert price_with_tax_00005(1000, 500) == 1050


def test_price_with_tax_negative_00005():
    with pytest.raises(ValueError):
        price_with_tax_00005(1000, -1)


def test_is_valid_sku_00005():
    assert is_valid_sku_00005("abc123")
    assert not is_valid_sku_00005("")


def test_bucket_by_tag_00005():
    p = Product_00005("s1", 100, ["a"])
    assert bucket_by_tag_00005([p]) == {"a": ["s1"]}
