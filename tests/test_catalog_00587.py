"""Tests for catalog_00587."""

import pytest

from cartservice.generated.catalog_00587 import (
    Product_00587,
    bucket_by_tag_00587,
    is_valid_sku_00587,
    price_with_tax_00587,
)


def test_price_with_tax_00587():
    assert price_with_tax_00587(1000, 500) == 1050


def test_price_with_tax_negative_00587():
    with pytest.raises(ValueError):
        price_with_tax_00587(1000, -1)


def test_is_valid_sku_00587():
    assert is_valid_sku_00587("abc123")
    assert not is_valid_sku_00587("")


def test_bucket_by_tag_00587():
    p = Product_00587("s1", 100, ["a"])
    assert bucket_by_tag_00587([p]) == {"a": ["s1"]}
