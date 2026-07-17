"""Tests for catalog_00035."""

import pytest

from cartservice.generated.catalog_00035 import (
    Product_00035,
    bucket_by_tag_00035,
    is_valid_sku_00035,
    price_with_tax_00035,
)


def test_price_with_tax_00035():
    assert price_with_tax_00035(1000, 500) == 1050


def test_price_with_tax_negative_00035():
    with pytest.raises(ValueError):
        price_with_tax_00035(1000, -1)


def test_is_valid_sku_00035():
    assert is_valid_sku_00035("abc123")
    assert not is_valid_sku_00035("")


def test_bucket_by_tag_00035():
    p = Product_00035("s1", 100, ["a"])
    assert bucket_by_tag_00035([p]) == {"a": ["s1"]}
