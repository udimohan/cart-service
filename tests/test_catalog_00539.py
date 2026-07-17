"""Tests for catalog_00539."""

import pytest

from cartservice.generated.catalog_00539 import (
    Product_00539,
    bucket_by_tag_00539,
    is_valid_sku_00539,
    price_with_tax_00539,
)


def test_price_with_tax_00539():
    assert price_with_tax_00539(1000, 500) == 1050


def test_price_with_tax_negative_00539():
    with pytest.raises(ValueError):
        price_with_tax_00539(1000, -1)


def test_is_valid_sku_00539():
    assert is_valid_sku_00539("abc123")
    assert not is_valid_sku_00539("")


def test_bucket_by_tag_00539():
    p = Product_00539("s1", 100, ["a"])
    assert bucket_by_tag_00539([p]) == {"a": ["s1"]}
