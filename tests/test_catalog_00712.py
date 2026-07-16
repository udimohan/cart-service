"""Tests for catalog_00712."""

import pytest

from cartservice.generated.catalog_00712 import (
    Product_00712,
    bucket_by_tag_00712,
    is_valid_sku_00712,
    price_with_tax_00712,
)


def test_price_with_tax_00712():
    assert price_with_tax_00712(1000, 500) == 1050


def test_price_with_tax_negative_00712():
    with pytest.raises(ValueError):
        price_with_tax_00712(1000, -1)


def test_is_valid_sku_00712():
    assert is_valid_sku_00712("abc123")
    assert not is_valid_sku_00712("")


def test_bucket_by_tag_00712():
    p = Product_00712("s1", 100, ["a"])
    assert bucket_by_tag_00712([p]) == {"a": ["s1"]}
