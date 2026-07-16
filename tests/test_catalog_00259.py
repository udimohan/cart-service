"""Tests for catalog_00259."""

import pytest

from cartservice.generated.catalog_00259 import (
    Product_00259,
    bucket_by_tag_00259,
    is_valid_sku_00259,
    price_with_tax_00259,
)


def test_price_with_tax_00259():
    assert price_with_tax_00259(1000, 500) == 1050


def test_price_with_tax_negative_00259():
    with pytest.raises(ValueError):
        price_with_tax_00259(1000, -1)


def test_is_valid_sku_00259():
    assert is_valid_sku_00259("abc123")
    assert not is_valid_sku_00259("")


def test_bucket_by_tag_00259():
    p = Product_00259("s1", 100, ["a"])
    assert bucket_by_tag_00259([p]) == {"a": ["s1"]}
