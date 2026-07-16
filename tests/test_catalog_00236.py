"""Tests for catalog_00236."""

import pytest

from cartservice.generated.catalog_00236 import (
    Product_00236,
    bucket_by_tag_00236,
    is_valid_sku_00236,
    price_with_tax_00236,
)


def test_price_with_tax_00236():
    assert price_with_tax_00236(1000, 500) == 1050


def test_price_with_tax_negative_00236():
    with pytest.raises(ValueError):
        price_with_tax_00236(1000, -1)


def test_is_valid_sku_00236():
    assert is_valid_sku_00236("abc123")
    assert not is_valid_sku_00236("")


def test_bucket_by_tag_00236():
    p = Product_00236("s1", 100, ["a"])
    assert bucket_by_tag_00236([p]) == {"a": ["s1"]}
