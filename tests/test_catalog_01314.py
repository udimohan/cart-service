"""Tests for catalog_01314."""

import pytest

from cartservice.generated.catalog_01314 import (
    Product_01314,
    bucket_by_tag_01314,
    is_valid_sku_01314,
    price_with_tax_01314,
)


def test_price_with_tax_01314():
    assert price_with_tax_01314(1000, 500) == 1050


def test_price_with_tax_negative_01314():
    with pytest.raises(ValueError):
        price_with_tax_01314(1000, -1)


def test_is_valid_sku_01314():
    assert is_valid_sku_01314("abc123")
    assert not is_valid_sku_01314("")


def test_bucket_by_tag_01314():
    p = Product_01314("s1", 100, ["a"])
    assert bucket_by_tag_01314([p]) == {"a": ["s1"]}
