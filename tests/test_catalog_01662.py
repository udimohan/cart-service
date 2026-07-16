"""Tests for catalog_01662."""

import pytest

from cartservice.generated.catalog_01662 import (
    Product_01662,
    bucket_by_tag_01662,
    is_valid_sku_01662,
    price_with_tax_01662,
)


def test_price_with_tax_01662():
    assert price_with_tax_01662(1000, 500) == 1050


def test_price_with_tax_negative_01662():
    with pytest.raises(ValueError):
        price_with_tax_01662(1000, -1)


def test_is_valid_sku_01662():
    assert is_valid_sku_01662("abc123")
    assert not is_valid_sku_01662("")


def test_bucket_by_tag_01662():
    p = Product_01662("s1", 100, ["a"])
    assert bucket_by_tag_01662([p]) == {"a": ["s1"]}
