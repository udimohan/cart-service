"""Tests for catalog_01275."""

import pytest

from cartservice.generated.catalog_01275 import (
    Product_01275,
    bucket_by_tag_01275,
    is_valid_sku_01275,
    price_with_tax_01275,
)


def test_price_with_tax_01275():
    assert price_with_tax_01275(1000, 500) == 1050


def test_price_with_tax_negative_01275():
    with pytest.raises(ValueError):
        price_with_tax_01275(1000, -1)


def test_is_valid_sku_01275():
    assert is_valid_sku_01275("abc123")
    assert not is_valid_sku_01275("")


def test_bucket_by_tag_01275():
    p = Product_01275("s1", 100, ["a"])
    assert bucket_by_tag_01275([p]) == {"a": ["s1"]}
