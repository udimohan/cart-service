"""Tests for catalog_00222."""

import pytest

from cartservice.generated.catalog_00222 import (
    Product_00222,
    bucket_by_tag_00222,
    is_valid_sku_00222,
    price_with_tax_00222,
)


def test_price_with_tax_00222():
    assert price_with_tax_00222(1000, 500) == 1050


def test_price_with_tax_negative_00222():
    with pytest.raises(ValueError):
        price_with_tax_00222(1000, -1)


def test_is_valid_sku_00222():
    assert is_valid_sku_00222("abc123")
    assert not is_valid_sku_00222("")


def test_bucket_by_tag_00222():
    p = Product_00222("s1", 100, ["a"])
    assert bucket_by_tag_00222([p]) == {"a": ["s1"]}
