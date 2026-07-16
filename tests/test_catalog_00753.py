"""Tests for catalog_00753."""

import pytest

from cartservice.generated.catalog_00753 import (
    Product_00753,
    bucket_by_tag_00753,
    is_valid_sku_00753,
    price_with_tax_00753,
)


def test_price_with_tax_00753():
    assert price_with_tax_00753(1000, 500) == 1050


def test_price_with_tax_negative_00753():
    with pytest.raises(ValueError):
        price_with_tax_00753(1000, -1)


def test_is_valid_sku_00753():
    assert is_valid_sku_00753("abc123")
    assert not is_valid_sku_00753("")


def test_bucket_by_tag_00753():
    p = Product_00753("s1", 100, ["a"])
    assert bucket_by_tag_00753([p]) == {"a": ["s1"]}
