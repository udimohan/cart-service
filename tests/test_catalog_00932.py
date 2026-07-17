"""Tests for catalog_00932."""

import pytest

from cartservice.generated.catalog_00932 import (
    Product_00932,
    bucket_by_tag_00932,
    is_valid_sku_00932,
    price_with_tax_00932,
)


def test_price_with_tax_00932():
    assert price_with_tax_00932(1000, 500) == 1050


def test_price_with_tax_negative_00932():
    with pytest.raises(ValueError):
        price_with_tax_00932(1000, -1)


def test_is_valid_sku_00932():
    assert is_valid_sku_00932("abc123")
    assert not is_valid_sku_00932("")


def test_bucket_by_tag_00932():
    p = Product_00932("s1", 100, ["a"])
    assert bucket_by_tag_00932([p]) == {"a": ["s1"]}
