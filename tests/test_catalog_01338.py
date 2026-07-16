"""Tests for catalog_01338."""

import pytest

from cartservice.generated.catalog_01338 import (
    Product_01338,
    bucket_by_tag_01338,
    is_valid_sku_01338,
    price_with_tax_01338,
)


def test_price_with_tax_01338():
    assert price_with_tax_01338(1000, 500) == 1050


def test_price_with_tax_negative_01338():
    with pytest.raises(ValueError):
        price_with_tax_01338(1000, -1)


def test_is_valid_sku_01338():
    assert is_valid_sku_01338("abc123")
    assert not is_valid_sku_01338("")


def test_bucket_by_tag_01338():
    p = Product_01338("s1", 100, ["a"])
    assert bucket_by_tag_01338([p]) == {"a": ["s1"]}
