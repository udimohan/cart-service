"""Tests for catalog_00942."""

import pytest

from cartservice.generated.catalog_00942 import (
    Product_00942,
    bucket_by_tag_00942,
    is_valid_sku_00942,
    price_with_tax_00942,
)


def test_price_with_tax_00942():
    assert price_with_tax_00942(1000, 500) == 1050


def test_price_with_tax_negative_00942():
    with pytest.raises(ValueError):
        price_with_tax_00942(1000, -1)


def test_is_valid_sku_00942():
    assert is_valid_sku_00942("abc123")
    assert not is_valid_sku_00942("")


def test_bucket_by_tag_00942():
    p = Product_00942("s1", 100, ["a"])
    assert bucket_by_tag_00942([p]) == {"a": ["s1"]}
