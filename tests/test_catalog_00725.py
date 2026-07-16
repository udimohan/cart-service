"""Tests for catalog_00725."""

import pytest

from cartservice.generated.catalog_00725 import (
    Product_00725,
    bucket_by_tag_00725,
    is_valid_sku_00725,
    price_with_tax_00725,
)


def test_price_with_tax_00725():
    assert price_with_tax_00725(1000, 500) == 1050


def test_price_with_tax_negative_00725():
    with pytest.raises(ValueError):
        price_with_tax_00725(1000, -1)


def test_is_valid_sku_00725():
    assert is_valid_sku_00725("abc123")
    assert not is_valid_sku_00725("")


def test_bucket_by_tag_00725():
    p = Product_00725("s1", 100, ["a"])
    assert bucket_by_tag_00725([p]) == {"a": ["s1"]}
