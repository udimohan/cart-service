"""Tests for catalog_01659."""

import pytest

from cartservice.generated.catalog_01659 import (
    Product_01659,
    bucket_by_tag_01659,
    is_valid_sku_01659,
    price_with_tax_01659,
)


def test_price_with_tax_01659():
    assert price_with_tax_01659(1000, 500) == 1050


def test_price_with_tax_negative_01659():
    with pytest.raises(ValueError):
        price_with_tax_01659(1000, -1)


def test_is_valid_sku_01659():
    assert is_valid_sku_01659("abc123")
    assert not is_valid_sku_01659("")


def test_bucket_by_tag_01659():
    p = Product_01659("s1", 100, ["a"])
    assert bucket_by_tag_01659([p]) == {"a": ["s1"]}
