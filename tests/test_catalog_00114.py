"""Tests for catalog_00114."""

import pytest

from cartservice.generated.catalog_00114 import (
    Product_00114,
    bucket_by_tag_00114,
    is_valid_sku_00114,
    price_with_tax_00114,
)


def test_price_with_tax_00114():
    assert price_with_tax_00114(1000, 500) == 1050


def test_price_with_tax_negative_00114():
    with pytest.raises(ValueError):
        price_with_tax_00114(1000, -1)


def test_is_valid_sku_00114():
    assert is_valid_sku_00114("abc123")
    assert not is_valid_sku_00114("")


def test_bucket_by_tag_00114():
    p = Product_00114("s1", 100, ["a"])
    assert bucket_by_tag_00114([p]) == {"a": ["s1"]}
