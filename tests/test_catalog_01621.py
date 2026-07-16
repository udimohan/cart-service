"""Tests for catalog_01621."""

import pytest

from cartservice.generated.catalog_01621 import (
    Product_01621,
    bucket_by_tag_01621,
    is_valid_sku_01621,
    price_with_tax_01621,
)


def test_price_with_tax_01621():
    assert price_with_tax_01621(1000, 500) == 1050


def test_price_with_tax_negative_01621():
    with pytest.raises(ValueError):
        price_with_tax_01621(1000, -1)


def test_is_valid_sku_01621():
    assert is_valid_sku_01621("abc123")
    assert not is_valid_sku_01621("")


def test_bucket_by_tag_01621():
    p = Product_01621("s1", 100, ["a"])
    assert bucket_by_tag_01621([p]) == {"a": ["s1"]}
