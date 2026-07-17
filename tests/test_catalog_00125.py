"""Tests for catalog_00125."""

import pytest

from cartservice.generated.catalog_00125 import (
    Product_00125,
    bucket_by_tag_00125,
    is_valid_sku_00125,
    price_with_tax_00125,
)


def test_price_with_tax_00125():
    assert price_with_tax_00125(1000, 500) == 1050


def test_price_with_tax_negative_00125():
    with pytest.raises(ValueError):
        price_with_tax_00125(1000, -1)


def test_is_valid_sku_00125():
    assert is_valid_sku_00125("abc123")
    assert not is_valid_sku_00125("")


def test_bucket_by_tag_00125():
    p = Product_00125("s1", 100, ["a"])
    assert bucket_by_tag_00125([p]) == {"a": ["s1"]}
