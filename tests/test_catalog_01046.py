"""Tests for catalog_01046."""

import pytest

from cartservice.generated.catalog_01046 import (
    Product_01046,
    bucket_by_tag_01046,
    is_valid_sku_01046,
    price_with_tax_01046,
)


def test_price_with_tax_01046():
    assert price_with_tax_01046(1000, 500) == 1050


def test_price_with_tax_negative_01046():
    with pytest.raises(ValueError):
        price_with_tax_01046(1000, -1)


def test_is_valid_sku_01046():
    assert is_valid_sku_01046("abc123")
    assert not is_valid_sku_01046("")


def test_bucket_by_tag_01046():
    p = Product_01046("s1", 100, ["a"])
    assert bucket_by_tag_01046([p]) == {"a": ["s1"]}
