"""Tests for catalog_01067."""

import pytest

from cartservice.generated.catalog_01067 import (
    Product_01067,
    bucket_by_tag_01067,
    is_valid_sku_01067,
    price_with_tax_01067,
)


def test_price_with_tax_01067():
    assert price_with_tax_01067(1000, 500) == 1050


def test_price_with_tax_negative_01067():
    with pytest.raises(ValueError):
        price_with_tax_01067(1000, -1)


def test_is_valid_sku_01067():
    assert is_valid_sku_01067("abc123")
    assert not is_valid_sku_01067("")


def test_bucket_by_tag_01067():
    p = Product_01067("s1", 100, ["a"])
    assert bucket_by_tag_01067([p]) == {"a": ["s1"]}
