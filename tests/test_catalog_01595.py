"""Tests for catalog_01595."""

import pytest

from cartservice.generated.catalog_01595 import (
    Product_01595,
    bucket_by_tag_01595,
    is_valid_sku_01595,
    price_with_tax_01595,
)


def test_price_with_tax_01595():
    assert price_with_tax_01595(1000, 500) == 1050


def test_price_with_tax_negative_01595():
    with pytest.raises(ValueError):
        price_with_tax_01595(1000, -1)


def test_is_valid_sku_01595():
    assert is_valid_sku_01595("abc123")
    assert not is_valid_sku_01595("")


def test_bucket_by_tag_01595():
    p = Product_01595("s1", 100, ["a"])
    assert bucket_by_tag_01595([p]) == {"a": ["s1"]}
