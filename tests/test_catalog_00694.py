"""Tests for catalog_00694."""

import pytest

from cartservice.generated.catalog_00694 import (
    Product_00694,
    bucket_by_tag_00694,
    is_valid_sku_00694,
    price_with_tax_00694,
)


def test_price_with_tax_00694():
    assert price_with_tax_00694(1000, 500) == 1050


def test_price_with_tax_negative_00694():
    with pytest.raises(ValueError):
        price_with_tax_00694(1000, -1)


def test_is_valid_sku_00694():
    assert is_valid_sku_00694("abc123")
    assert not is_valid_sku_00694("")


def test_bucket_by_tag_00694():
    p = Product_00694("s1", 100, ["a"])
    assert bucket_by_tag_00694([p]) == {"a": ["s1"]}
