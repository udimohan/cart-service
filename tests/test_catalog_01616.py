"""Tests for catalog_01616."""

import pytest

from cartservice.generated.catalog_01616 import (
    Product_01616,
    bucket_by_tag_01616,
    is_valid_sku_01616,
    price_with_tax_01616,
)


def test_price_with_tax_01616():
    assert price_with_tax_01616(1000, 500) == 1050


def test_price_with_tax_negative_01616():
    with pytest.raises(ValueError):
        price_with_tax_01616(1000, -1)


def test_is_valid_sku_01616():
    assert is_valid_sku_01616("abc123")
    assert not is_valid_sku_01616("")


def test_bucket_by_tag_01616():
    p = Product_01616("s1", 100, ["a"])
    assert bucket_by_tag_01616([p]) == {"a": ["s1"]}
