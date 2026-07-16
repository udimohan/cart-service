"""Tests for catalog_00874."""

import pytest

from cartservice.generated.catalog_00874 import (
    Product_00874,
    bucket_by_tag_00874,
    is_valid_sku_00874,
    price_with_tax_00874,
)


def test_price_with_tax_00874():
    assert price_with_tax_00874(1000, 500) == 1050


def test_price_with_tax_negative_00874():
    with pytest.raises(ValueError):
        price_with_tax_00874(1000, -1)


def test_is_valid_sku_00874():
    assert is_valid_sku_00874("abc123")
    assert not is_valid_sku_00874("")


def test_bucket_by_tag_00874():
    p = Product_00874("s1", 100, ["a"])
    assert bucket_by_tag_00874([p]) == {"a": ["s1"]}
