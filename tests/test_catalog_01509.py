"""Tests for catalog_01509."""

import pytest

from cartservice.generated.catalog_01509 import (
    Product_01509,
    bucket_by_tag_01509,
    is_valid_sku_01509,
    price_with_tax_01509,
)


def test_price_with_tax_01509():
    assert price_with_tax_01509(1000, 500) == 1050


def test_price_with_tax_negative_01509():
    with pytest.raises(ValueError):
        price_with_tax_01509(1000, -1)


def test_is_valid_sku_01509():
    assert is_valid_sku_01509("abc123")
    assert not is_valid_sku_01509("")


def test_bucket_by_tag_01509():
    p = Product_01509("s1", 100, ["a"])
    assert bucket_by_tag_01509([p]) == {"a": ["s1"]}
