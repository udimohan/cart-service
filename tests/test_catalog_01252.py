"""Tests for catalog_01252."""

import pytest

from cartservice.generated.catalog_01252 import (
    Product_01252,
    bucket_by_tag_01252,
    is_valid_sku_01252,
    price_with_tax_01252,
)


def test_price_with_tax_01252():
    assert price_with_tax_01252(1000, 500) == 1050


def test_price_with_tax_negative_01252():
    with pytest.raises(ValueError):
        price_with_tax_01252(1000, -1)


def test_is_valid_sku_01252():
    assert is_valid_sku_01252("abc123")
    assert not is_valid_sku_01252("")


def test_bucket_by_tag_01252():
    p = Product_01252("s1", 100, ["a"])
    assert bucket_by_tag_01252([p]) == {"a": ["s1"]}
