"""Tests for catalog_00435."""

import pytest

from cartservice.generated.catalog_00435 import (
    Product_00435,
    bucket_by_tag_00435,
    is_valid_sku_00435,
    price_with_tax_00435,
)


def test_price_with_tax_00435():
    assert price_with_tax_00435(1000, 500) == 1050


def test_price_with_tax_negative_00435():
    with pytest.raises(ValueError):
        price_with_tax_00435(1000, -1)


def test_is_valid_sku_00435():
    assert is_valid_sku_00435("abc123")
    assert not is_valid_sku_00435("")


def test_bucket_by_tag_00435():
    p = Product_00435("s1", 100, ["a"])
    assert bucket_by_tag_00435([p]) == {"a": ["s1"]}
