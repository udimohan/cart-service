"""Tests for catalog_01436."""

import pytest

from cartservice.generated.catalog_01436 import (
    Product_01436,
    bucket_by_tag_01436,
    is_valid_sku_01436,
    price_with_tax_01436,
)


def test_price_with_tax_01436():
    assert price_with_tax_01436(1000, 500) == 1050


def test_price_with_tax_negative_01436():
    with pytest.raises(ValueError):
        price_with_tax_01436(1000, -1)


def test_is_valid_sku_01436():
    assert is_valid_sku_01436("abc123")
    assert not is_valid_sku_01436("")


def test_bucket_by_tag_01436():
    p = Product_01436("s1", 100, ["a"])
    assert bucket_by_tag_01436([p]) == {"a": ["s1"]}
