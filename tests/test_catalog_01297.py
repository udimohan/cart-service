"""Tests for catalog_01297."""

import pytest

from cartservice.generated.catalog_01297 import (
    Product_01297,
    bucket_by_tag_01297,
    is_valid_sku_01297,
    price_with_tax_01297,
)


def test_price_with_tax_01297():
    assert price_with_tax_01297(1000, 500) == 1050


def test_price_with_tax_negative_01297():
    with pytest.raises(ValueError):
        price_with_tax_01297(1000, -1)


def test_is_valid_sku_01297():
    assert is_valid_sku_01297("abc123")
    assert not is_valid_sku_01297("")


def test_bucket_by_tag_01297():
    p = Product_01297("s1", 100, ["a"])
    assert bucket_by_tag_01297([p]) == {"a": ["s1"]}
