"""Tests for catalog_01092."""

import pytest

from cartservice.generated.catalog_01092 import (
    Product_01092,
    bucket_by_tag_01092,
    is_valid_sku_01092,
    price_with_tax_01092,
)


def test_price_with_tax_01092():
    assert price_with_tax_01092(1000, 500) == 1050


def test_price_with_tax_negative_01092():
    with pytest.raises(ValueError):
        price_with_tax_01092(1000, -1)


def test_is_valid_sku_01092():
    assert is_valid_sku_01092("abc123")
    assert not is_valid_sku_01092("")


def test_bucket_by_tag_01092():
    p = Product_01092("s1", 100, ["a"])
    assert bucket_by_tag_01092([p]) == {"a": ["s1"]}
