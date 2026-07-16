"""Tests for catalog_00092."""

import pytest

from cartservice.generated.catalog_00092 import (
    Product_00092,
    bucket_by_tag_00092,
    is_valid_sku_00092,
    price_with_tax_00092,
)


def test_price_with_tax_00092():
    assert price_with_tax_00092(1000, 500) == 1050


def test_price_with_tax_negative_00092():
    with pytest.raises(ValueError):
        price_with_tax_00092(1000, -1)


def test_is_valid_sku_00092():
    assert is_valid_sku_00092("abc123")
    assert not is_valid_sku_00092("")


def test_bucket_by_tag_00092():
    p = Product_00092("s1", 100, ["a"])
    assert bucket_by_tag_00092([p]) == {"a": ["s1"]}
