"""Tests for catalog_00685."""

import pytest

from cartservice.generated.catalog_00685 import (
    Product_00685,
    bucket_by_tag_00685,
    is_valid_sku_00685,
    price_with_tax_00685,
)


def test_price_with_tax_00685():
    assert price_with_tax_00685(1000, 500) == 1050


def test_price_with_tax_negative_00685():
    with pytest.raises(ValueError):
        price_with_tax_00685(1000, -1)


def test_is_valid_sku_00685():
    assert is_valid_sku_00685("abc123")
    assert not is_valid_sku_00685("")


def test_bucket_by_tag_00685():
    p = Product_00685("s1", 100, ["a"])
    assert bucket_by_tag_00685([p]) == {"a": ["s1"]}
