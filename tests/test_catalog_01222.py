"""Tests for catalog_01222."""

import pytest

from cartservice.generated.catalog_01222 import (
    Product_01222,
    bucket_by_tag_01222,
    is_valid_sku_01222,
    price_with_tax_01222,
)


def test_price_with_tax_01222():
    assert price_with_tax_01222(1000, 500) == 1050


def test_price_with_tax_negative_01222():
    with pytest.raises(ValueError):
        price_with_tax_01222(1000, -1)


def test_is_valid_sku_01222():
    assert is_valid_sku_01222("abc123")
    assert not is_valid_sku_01222("")


def test_bucket_by_tag_01222():
    p = Product_01222("s1", 100, ["a"])
    assert bucket_by_tag_01222([p]) == {"a": ["s1"]}
