"""Tests for catalog_01290."""

import pytest

from cartservice.generated.catalog_01290 import (
    Product_01290,
    bucket_by_tag_01290,
    is_valid_sku_01290,
    price_with_tax_01290,
)


def test_price_with_tax_01290():
    assert price_with_tax_01290(1000, 500) == 1050


def test_price_with_tax_negative_01290():
    with pytest.raises(ValueError):
        price_with_tax_01290(1000, -1)


def test_is_valid_sku_01290():
    assert is_valid_sku_01290("abc123")
    assert not is_valid_sku_01290("")


def test_bucket_by_tag_01290():
    p = Product_01290("s1", 100, ["a"])
    assert bucket_by_tag_01290([p]) == {"a": ["s1"]}
