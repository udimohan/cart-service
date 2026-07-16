"""Tests for catalog_01648."""

import pytest

from cartservice.generated.catalog_01648 import (
    Product_01648,
    bucket_by_tag_01648,
    is_valid_sku_01648,
    price_with_tax_01648,
)


def test_price_with_tax_01648():
    assert price_with_tax_01648(1000, 500) == 1050


def test_price_with_tax_negative_01648():
    with pytest.raises(ValueError):
        price_with_tax_01648(1000, -1)


def test_is_valid_sku_01648():
    assert is_valid_sku_01648("abc123")
    assert not is_valid_sku_01648("")


def test_bucket_by_tag_01648():
    p = Product_01648("s1", 100, ["a"])
    assert bucket_by_tag_01648([p]) == {"a": ["s1"]}
