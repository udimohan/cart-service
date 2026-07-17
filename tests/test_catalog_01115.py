"""Tests for catalog_01115."""

import pytest

from cartservice.generated.catalog_01115 import (
    Product_01115,
    bucket_by_tag_01115,
    is_valid_sku_01115,
    price_with_tax_01115,
)


def test_price_with_tax_01115():
    assert price_with_tax_01115(1000, 500) == 1050


def test_price_with_tax_negative_01115():
    with pytest.raises(ValueError):
        price_with_tax_01115(1000, -1)


def test_is_valid_sku_01115():
    assert is_valid_sku_01115("abc123")
    assert not is_valid_sku_01115("")


def test_bucket_by_tag_01115():
    p = Product_01115("s1", 100, ["a"])
    assert bucket_by_tag_01115([p]) == {"a": ["s1"]}
