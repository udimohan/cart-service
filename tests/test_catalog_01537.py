"""Tests for catalog_01537."""

import pytest

from cartservice.generated.catalog_01537 import (
    Product_01537,
    bucket_by_tag_01537,
    is_valid_sku_01537,
    price_with_tax_01537,
)


def test_price_with_tax_01537():
    assert price_with_tax_01537(1000, 500) == 1050


def test_price_with_tax_negative_01537():
    with pytest.raises(ValueError):
        price_with_tax_01537(1000, -1)


def test_is_valid_sku_01537():
    assert is_valid_sku_01537("abc123")
    assert not is_valid_sku_01537("")


def test_bucket_by_tag_01537():
    p = Product_01537("s1", 100, ["a"])
    assert bucket_by_tag_01537([p]) == {"a": ["s1"]}
