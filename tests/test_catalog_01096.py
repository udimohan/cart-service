"""Tests for catalog_01096."""

import pytest

from cartservice.generated.catalog_01096 import (
    Product_01096,
    bucket_by_tag_01096,
    is_valid_sku_01096,
    price_with_tax_01096,
)


def test_price_with_tax_01096():
    assert price_with_tax_01096(1000, 500) == 1050


def test_price_with_tax_negative_01096():
    with pytest.raises(ValueError):
        price_with_tax_01096(1000, -1)


def test_is_valid_sku_01096():
    assert is_valid_sku_01096("abc123")
    assert not is_valid_sku_01096("")


def test_bucket_by_tag_01096():
    p = Product_01096("s1", 100, ["a"])
    assert bucket_by_tag_01096([p]) == {"a": ["s1"]}
