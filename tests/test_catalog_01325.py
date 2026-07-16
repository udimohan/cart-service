"""Tests for catalog_01325."""

import pytest

from cartservice.generated.catalog_01325 import (
    Product_01325,
    bucket_by_tag_01325,
    is_valid_sku_01325,
    price_with_tax_01325,
)


def test_price_with_tax_01325():
    assert price_with_tax_01325(1000, 500) == 1050


def test_price_with_tax_negative_01325():
    with pytest.raises(ValueError):
        price_with_tax_01325(1000, -1)


def test_is_valid_sku_01325():
    assert is_valid_sku_01325("abc123")
    assert not is_valid_sku_01325("")


def test_bucket_by_tag_01325():
    p = Product_01325("s1", 100, ["a"])
    assert bucket_by_tag_01325([p]) == {"a": ["s1"]}
