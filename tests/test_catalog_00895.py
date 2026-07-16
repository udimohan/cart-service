"""Tests for catalog_00895."""

import pytest

from cartservice.generated.catalog_00895 import (
    Product_00895,
    bucket_by_tag_00895,
    is_valid_sku_00895,
    price_with_tax_00895,
)


def test_price_with_tax_00895():
    assert price_with_tax_00895(1000, 500) == 1050


def test_price_with_tax_negative_00895():
    with pytest.raises(ValueError):
        price_with_tax_00895(1000, -1)


def test_is_valid_sku_00895():
    assert is_valid_sku_00895("abc123")
    assert not is_valid_sku_00895("")


def test_bucket_by_tag_00895():
    p = Product_00895("s1", 100, ["a"])
    assert bucket_by_tag_00895([p]) == {"a": ["s1"]}
