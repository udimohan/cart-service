"""Tests for catalog_01037."""

import pytest

from cartservice.generated.catalog_01037 import (
    Product_01037,
    bucket_by_tag_01037,
    is_valid_sku_01037,
    price_with_tax_01037,
)


def test_price_with_tax_01037():
    assert price_with_tax_01037(1000, 500) == 1050


def test_price_with_tax_negative_01037():
    with pytest.raises(ValueError):
        price_with_tax_01037(1000, -1)


def test_is_valid_sku_01037():
    assert is_valid_sku_01037("abc123")
    assert not is_valid_sku_01037("")


def test_bucket_by_tag_01037():
    p = Product_01037("s1", 100, ["a"])
    assert bucket_by_tag_01037([p]) == {"a": ["s1"]}
