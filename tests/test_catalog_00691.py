"""Tests for catalog_00691."""

import pytest

from cartservice.generated.catalog_00691 import (
    Product_00691,
    bucket_by_tag_00691,
    is_valid_sku_00691,
    price_with_tax_00691,
)


def test_price_with_tax_00691():
    assert price_with_tax_00691(1000, 500) == 1050


def test_price_with_tax_negative_00691():
    with pytest.raises(ValueError):
        price_with_tax_00691(1000, -1)


def test_is_valid_sku_00691():
    assert is_valid_sku_00691("abc123")
    assert not is_valid_sku_00691("")


def test_bucket_by_tag_00691():
    p = Product_00691("s1", 100, ["a"])
    assert bucket_by_tag_00691([p]) == {"a": ["s1"]}
