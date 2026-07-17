"""Tests for catalog_00947."""

import pytest

from cartservice.generated.catalog_00947 import (
    Product_00947,
    bucket_by_tag_00947,
    is_valid_sku_00947,
    price_with_tax_00947,
)


def test_price_with_tax_00947():
    assert price_with_tax_00947(1000, 500) == 1050


def test_price_with_tax_negative_00947():
    with pytest.raises(ValueError):
        price_with_tax_00947(1000, -1)


def test_is_valid_sku_00947():
    assert is_valid_sku_00947("abc123")
    assert not is_valid_sku_00947("")


def test_bucket_by_tag_00947():
    p = Product_00947("s1", 100, ["a"])
    assert bucket_by_tag_00947([p]) == {"a": ["s1"]}
