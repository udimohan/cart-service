"""Tests for catalog_01598."""

import pytest

from cartservice.generated.catalog_01598 import (
    Product_01598,
    bucket_by_tag_01598,
    is_valid_sku_01598,
    price_with_tax_01598,
)


def test_price_with_tax_01598():
    assert price_with_tax_01598(1000, 500) == 1050


def test_price_with_tax_negative_01598():
    with pytest.raises(ValueError):
        price_with_tax_01598(1000, -1)


def test_is_valid_sku_01598():
    assert is_valid_sku_01598("abc123")
    assert not is_valid_sku_01598("")


def test_bucket_by_tag_01598():
    p = Product_01598("s1", 100, ["a"])
    assert bucket_by_tag_01598([p]) == {"a": ["s1"]}
