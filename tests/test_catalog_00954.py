"""Tests for catalog_00954."""

import pytest

from cartservice.generated.catalog_00954 import (
    Product_00954,
    bucket_by_tag_00954,
    is_valid_sku_00954,
    price_with_tax_00954,
)


def test_price_with_tax_00954():
    assert price_with_tax_00954(1000, 500) == 1050


def test_price_with_tax_negative_00954():
    with pytest.raises(ValueError):
        price_with_tax_00954(1000, -1)


def test_is_valid_sku_00954():
    assert is_valid_sku_00954("abc123")
    assert not is_valid_sku_00954("")


def test_bucket_by_tag_00954():
    p = Product_00954("s1", 100, ["a"])
    assert bucket_by_tag_00954([p]) == {"a": ["s1"]}
