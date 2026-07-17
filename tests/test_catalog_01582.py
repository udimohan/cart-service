"""Tests for catalog_01582."""

import pytest

from cartservice.generated.catalog_01582 import (
    Product_01582,
    bucket_by_tag_01582,
    is_valid_sku_01582,
    price_with_tax_01582,
)


def test_price_with_tax_01582():
    assert price_with_tax_01582(1000, 500) == 1050


def test_price_with_tax_negative_01582():
    with pytest.raises(ValueError):
        price_with_tax_01582(1000, -1)


def test_is_valid_sku_01582():
    assert is_valid_sku_01582("abc123")
    assert not is_valid_sku_01582("")


def test_bucket_by_tag_01582():
    p = Product_01582("s1", 100, ["a"])
    assert bucket_by_tag_01582([p]) == {"a": ["s1"]}
