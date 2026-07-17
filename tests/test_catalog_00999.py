"""Tests for catalog_00999."""

import pytest

from cartservice.generated.catalog_00999 import (
    Product_00999,
    bucket_by_tag_00999,
    is_valid_sku_00999,
    price_with_tax_00999,
)


def test_price_with_tax_00999():
    assert price_with_tax_00999(1000, 500) == 1050


def test_price_with_tax_negative_00999():
    with pytest.raises(ValueError):
        price_with_tax_00999(1000, -1)


def test_is_valid_sku_00999():
    assert is_valid_sku_00999("abc123")
    assert not is_valid_sku_00999("")


def test_bucket_by_tag_00999():
    p = Product_00999("s1", 100, ["a"])
    assert bucket_by_tag_00999([p]) == {"a": ["s1"]}
