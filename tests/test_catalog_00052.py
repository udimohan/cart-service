"""Tests for catalog_00052."""

import pytest

from cartservice.generated.catalog_00052 import (
    Product_00052,
    bucket_by_tag_00052,
    is_valid_sku_00052,
    price_with_tax_00052,
)


def test_price_with_tax_00052():
    assert price_with_tax_00052(1000, 500) == 1050


def test_price_with_tax_negative_00052():
    with pytest.raises(ValueError):
        price_with_tax_00052(1000, -1)


def test_is_valid_sku_00052():
    assert is_valid_sku_00052("abc123")
    assert not is_valid_sku_00052("")


def test_bucket_by_tag_00052():
    p = Product_00052("s1", 100, ["a"])
    assert bucket_by_tag_00052([p]) == {"a": ["s1"]}
