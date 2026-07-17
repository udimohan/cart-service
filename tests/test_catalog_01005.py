"""Tests for catalog_01005."""

import pytest

from cartservice.generated.catalog_01005 import (
    Product_01005,
    bucket_by_tag_01005,
    is_valid_sku_01005,
    price_with_tax_01005,
)


def test_price_with_tax_01005():
    assert price_with_tax_01005(1000, 500) == 1050


def test_price_with_tax_negative_01005():
    with pytest.raises(ValueError):
        price_with_tax_01005(1000, -1)


def test_is_valid_sku_01005():
    assert is_valid_sku_01005("abc123")
    assert not is_valid_sku_01005("")


def test_bucket_by_tag_01005():
    p = Product_01005("s1", 100, ["a"])
    assert bucket_by_tag_01005([p]) == {"a": ["s1"]}
