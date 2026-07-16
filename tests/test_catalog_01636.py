"""Tests for catalog_01636."""

import pytest

from cartservice.generated.catalog_01636 import (
    Product_01636,
    bucket_by_tag_01636,
    is_valid_sku_01636,
    price_with_tax_01636,
)


def test_price_with_tax_01636():
    assert price_with_tax_01636(1000, 500) == 1050


def test_price_with_tax_negative_01636():
    with pytest.raises(ValueError):
        price_with_tax_01636(1000, -1)


def test_is_valid_sku_01636():
    assert is_valid_sku_01636("abc123")
    assert not is_valid_sku_01636("")


def test_bucket_by_tag_01636():
    p = Product_01636("s1", 100, ["a"])
    assert bucket_by_tag_01636([p]) == {"a": ["s1"]}
