"""Tests for catalog_01323."""

import pytest

from cartservice.generated.catalog_01323 import (
    Product_01323,
    bucket_by_tag_01323,
    is_valid_sku_01323,
    price_with_tax_01323,
)


def test_price_with_tax_01323():
    assert price_with_tax_01323(1000, 500) == 1050


def test_price_with_tax_negative_01323():
    with pytest.raises(ValueError):
        price_with_tax_01323(1000, -1)


def test_is_valid_sku_01323():
    assert is_valid_sku_01323("abc123")
    assert not is_valid_sku_01323("")


def test_bucket_by_tag_01323():
    p = Product_01323("s1", 100, ["a"])
    assert bucket_by_tag_01323([p]) == {"a": ["s1"]}
