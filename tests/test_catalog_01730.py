"""Tests for catalog_01730."""

import pytest

from cartservice.generated.catalog_01730 import (
    Product_01730,
    bucket_by_tag_01730,
    is_valid_sku_01730,
    price_with_tax_01730,
)


def test_price_with_tax_01730():
    assert price_with_tax_01730(1000, 500) == 1050


def test_price_with_tax_negative_01730():
    with pytest.raises(ValueError):
        price_with_tax_01730(1000, -1)


def test_is_valid_sku_01730():
    assert is_valid_sku_01730("abc123")
    assert not is_valid_sku_01730("")


def test_bucket_by_tag_01730():
    p = Product_01730("s1", 100, ["a"])
    assert bucket_by_tag_01730([p]) == {"a": ["s1"]}
