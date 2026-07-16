"""Tests for catalog_00881."""

import pytest

from cartservice.generated.catalog_00881 import (
    Product_00881,
    bucket_by_tag_00881,
    is_valid_sku_00881,
    price_with_tax_00881,
)


def test_price_with_tax_00881():
    assert price_with_tax_00881(1000, 500) == 1050


def test_price_with_tax_negative_00881():
    with pytest.raises(ValueError):
        price_with_tax_00881(1000, -1)


def test_is_valid_sku_00881():
    assert is_valid_sku_00881("abc123")
    assert not is_valid_sku_00881("")


def test_bucket_by_tag_00881():
    p = Product_00881("s1", 100, ["a"])
    assert bucket_by_tag_00881([p]) == {"a": ["s1"]}
