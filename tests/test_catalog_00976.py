"""Tests for catalog_00976."""

import pytest

from cartservice.generated.catalog_00976 import (
    Product_00976,
    bucket_by_tag_00976,
    is_valid_sku_00976,
    price_with_tax_00976,
)


def test_price_with_tax_00976():
    assert price_with_tax_00976(1000, 500) == 1050


def test_price_with_tax_negative_00976():
    with pytest.raises(ValueError):
        price_with_tax_00976(1000, -1)


def test_is_valid_sku_00976():
    assert is_valid_sku_00976("abc123")
    assert not is_valid_sku_00976("")


def test_bucket_by_tag_00976():
    p = Product_00976("s1", 100, ["a"])
    assert bucket_by_tag_00976([p]) == {"a": ["s1"]}
