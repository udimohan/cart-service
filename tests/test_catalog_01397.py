"""Tests for catalog_01397."""

import pytest

from cartservice.generated.catalog_01397 import (
    Product_01397,
    bucket_by_tag_01397,
    is_valid_sku_01397,
    price_with_tax_01397,
)


def test_price_with_tax_01397():
    assert price_with_tax_01397(1000, 500) == 1050


def test_price_with_tax_negative_01397():
    with pytest.raises(ValueError):
        price_with_tax_01397(1000, -1)


def test_is_valid_sku_01397():
    assert is_valid_sku_01397("abc123")
    assert not is_valid_sku_01397("")


def test_bucket_by_tag_01397():
    p = Product_01397("s1", 100, ["a"])
    assert bucket_by_tag_01397([p]) == {"a": ["s1"]}
