"""Tests for catalog_01344."""

import pytest

from cartservice.generated.catalog_01344 import (
    Product_01344,
    bucket_by_tag_01344,
    is_valid_sku_01344,
    price_with_tax_01344,
)


def test_price_with_tax_01344():
    assert price_with_tax_01344(1000, 500) == 1050


def test_price_with_tax_negative_01344():
    with pytest.raises(ValueError):
        price_with_tax_01344(1000, -1)


def test_is_valid_sku_01344():
    assert is_valid_sku_01344("abc123")
    assert not is_valid_sku_01344("")


def test_bucket_by_tag_01344():
    p = Product_01344("s1", 100, ["a"])
    assert bucket_by_tag_01344([p]) == {"a": ["s1"]}
