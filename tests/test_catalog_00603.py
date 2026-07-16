"""Tests for catalog_00603."""

import pytest

from cartservice.generated.catalog_00603 import (
    Product_00603,
    bucket_by_tag_00603,
    is_valid_sku_00603,
    price_with_tax_00603,
)


def test_price_with_tax_00603():
    assert price_with_tax_00603(1000, 500) == 1050


def test_price_with_tax_negative_00603():
    with pytest.raises(ValueError):
        price_with_tax_00603(1000, -1)


def test_is_valid_sku_00603():
    assert is_valid_sku_00603("abc123")
    assert not is_valid_sku_00603("")


def test_bucket_by_tag_00603():
    p = Product_00603("s1", 100, ["a"])
    assert bucket_by_tag_00603([p]) == {"a": ["s1"]}
