"""Tests for catalog_01607."""

import pytest

from cartservice.generated.catalog_01607 import (
    Product_01607,
    bucket_by_tag_01607,
    is_valid_sku_01607,
    price_with_tax_01607,
)


def test_price_with_tax_01607():
    assert price_with_tax_01607(1000, 500) == 1050


def test_price_with_tax_negative_01607():
    with pytest.raises(ValueError):
        price_with_tax_01607(1000, -1)


def test_is_valid_sku_01607():
    assert is_valid_sku_01607("abc123")
    assert not is_valid_sku_01607("")


def test_bucket_by_tag_01607():
    p = Product_01607("s1", 100, ["a"])
    assert bucket_by_tag_01607([p]) == {"a": ["s1"]}
