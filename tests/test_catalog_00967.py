"""Tests for catalog_00967."""

import pytest

from cartservice.generated.catalog_00967 import (
    Product_00967,
    bucket_by_tag_00967,
    is_valid_sku_00967,
    price_with_tax_00967,
)


def test_price_with_tax_00967():
    assert price_with_tax_00967(1000, 500) == 1050


def test_price_with_tax_negative_00967():
    with pytest.raises(ValueError):
        price_with_tax_00967(1000, -1)


def test_is_valid_sku_00967():
    assert is_valid_sku_00967("abc123")
    assert not is_valid_sku_00967("")


def test_bucket_by_tag_00967():
    p = Product_00967("s1", 100, ["a"])
    assert bucket_by_tag_00967([p]) == {"a": ["s1"]}
