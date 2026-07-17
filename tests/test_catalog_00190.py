"""Tests for catalog_00190."""

import pytest

from cartservice.generated.catalog_00190 import (
    Product_00190,
    bucket_by_tag_00190,
    is_valid_sku_00190,
    price_with_tax_00190,
)


def test_price_with_tax_00190():
    assert price_with_tax_00190(1000, 500) == 1050


def test_price_with_tax_negative_00190():
    with pytest.raises(ValueError):
        price_with_tax_00190(1000, -1)


def test_is_valid_sku_00190():
    assert is_valid_sku_00190("abc123")
    assert not is_valid_sku_00190("")


def test_bucket_by_tag_00190():
    p = Product_00190("s1", 100, ["a"])
    assert bucket_by_tag_00190([p]) == {"a": ["s1"]}
