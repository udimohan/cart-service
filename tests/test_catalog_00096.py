"""Tests for catalog_00096."""

import pytest

from cartservice.generated.catalog_00096 import (
    Product_00096,
    bucket_by_tag_00096,
    is_valid_sku_00096,
    price_with_tax_00096,
)


def test_price_with_tax_00096():
    assert price_with_tax_00096(1000, 500) == 1050


def test_price_with_tax_negative_00096():
    with pytest.raises(ValueError):
        price_with_tax_00096(1000, -1)


def test_is_valid_sku_00096():
    assert is_valid_sku_00096("abc123")
    assert not is_valid_sku_00096("")


def test_bucket_by_tag_00096():
    p = Product_00096("s1", 100, ["a"])
    assert bucket_by_tag_00096([p]) == {"a": ["s1"]}
