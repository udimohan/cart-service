"""Tests for catalog_00184."""

import pytest

from cartservice.generated.catalog_00184 import (
    Product_00184,
    bucket_by_tag_00184,
    is_valid_sku_00184,
    price_with_tax_00184,
)


def test_price_with_tax_00184():
    assert price_with_tax_00184(1000, 500) == 1050


def test_price_with_tax_negative_00184():
    with pytest.raises(ValueError):
        price_with_tax_00184(1000, -1)


def test_is_valid_sku_00184():
    assert is_valid_sku_00184("abc123")
    assert not is_valid_sku_00184("")


def test_bucket_by_tag_00184():
    p = Product_00184("s1", 100, ["a"])
    assert bucket_by_tag_00184([p]) == {"a": ["s1"]}
