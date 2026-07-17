"""Tests for catalog_01710."""

import pytest

from cartservice.generated.catalog_01710 import (
    Product_01710,
    bucket_by_tag_01710,
    is_valid_sku_01710,
    price_with_tax_01710,
)


def test_price_with_tax_01710():
    assert price_with_tax_01710(1000, 500) == 1050


def test_price_with_tax_negative_01710():
    with pytest.raises(ValueError):
        price_with_tax_01710(1000, -1)


def test_is_valid_sku_01710():
    assert is_valid_sku_01710("abc123")
    assert not is_valid_sku_01710("")


def test_bucket_by_tag_01710():
    p = Product_01710("s1", 100, ["a"])
    assert bucket_by_tag_01710([p]) == {"a": ["s1"]}
