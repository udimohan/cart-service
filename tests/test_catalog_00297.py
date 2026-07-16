"""Tests for catalog_00297."""

import pytest

from cartservice.generated.catalog_00297 import (
    Product_00297,
    bucket_by_tag_00297,
    is_valid_sku_00297,
    price_with_tax_00297,
)


def test_price_with_tax_00297():
    assert price_with_tax_00297(1000, 500) == 1050


def test_price_with_tax_negative_00297():
    with pytest.raises(ValueError):
        price_with_tax_00297(1000, -1)


def test_is_valid_sku_00297():
    assert is_valid_sku_00297("abc123")
    assert not is_valid_sku_00297("")


def test_bucket_by_tag_00297():
    p = Product_00297("s1", 100, ["a"])
    assert bucket_by_tag_00297([p]) == {"a": ["s1"]}
