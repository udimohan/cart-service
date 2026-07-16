"""Tests for catalog_00908."""

import pytest

from cartservice.generated.catalog_00908 import (
    Product_00908,
    bucket_by_tag_00908,
    is_valid_sku_00908,
    price_with_tax_00908,
)


def test_price_with_tax_00908():
    assert price_with_tax_00908(1000, 500) == 1050


def test_price_with_tax_negative_00908():
    with pytest.raises(ValueError):
        price_with_tax_00908(1000, -1)


def test_is_valid_sku_00908():
    assert is_valid_sku_00908("abc123")
    assert not is_valid_sku_00908("")


def test_bucket_by_tag_00908():
    p = Product_00908("s1", 100, ["a"])
    assert bucket_by_tag_00908([p]) == {"a": ["s1"]}
