"""Tests for catalog_00734."""

import pytest

from cartservice.generated.catalog_00734 import (
    Product_00734,
    bucket_by_tag_00734,
    is_valid_sku_00734,
    price_with_tax_00734,
)


def test_price_with_tax_00734():
    assert price_with_tax_00734(1000, 500) == 1050


def test_price_with_tax_negative_00734():
    with pytest.raises(ValueError):
        price_with_tax_00734(1000, -1)


def test_is_valid_sku_00734():
    assert is_valid_sku_00734("abc123")
    assert not is_valid_sku_00734("")


def test_bucket_by_tag_00734():
    p = Product_00734("s1", 100, ["a"])
    assert bucket_by_tag_00734([p]) == {"a": ["s1"]}
