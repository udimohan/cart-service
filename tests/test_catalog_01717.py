"""Tests for catalog_01717."""

import pytest

from cartservice.generated.catalog_01717 import (
    Product_01717,
    bucket_by_tag_01717,
    is_valid_sku_01717,
    price_with_tax_01717,
)


def test_price_with_tax_01717():
    assert price_with_tax_01717(1000, 500) == 1050


def test_price_with_tax_negative_01717():
    with pytest.raises(ValueError):
        price_with_tax_01717(1000, -1)


def test_is_valid_sku_01717():
    assert is_valid_sku_01717("abc123")
    assert not is_valid_sku_01717("")


def test_bucket_by_tag_01717():
    p = Product_01717("s1", 100, ["a"])
    assert bucket_by_tag_01717([p]) == {"a": ["s1"]}
