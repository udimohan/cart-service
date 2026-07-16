"""Tests for catalog_01364."""

import pytest

from cartservice.generated.catalog_01364 import (
    Product_01364,
    bucket_by_tag_01364,
    is_valid_sku_01364,
    price_with_tax_01364,
)


def test_price_with_tax_01364():
    assert price_with_tax_01364(1000, 500) == 1050


def test_price_with_tax_negative_01364():
    with pytest.raises(ValueError):
        price_with_tax_01364(1000, -1)


def test_is_valid_sku_01364():
    assert is_valid_sku_01364("abc123")
    assert not is_valid_sku_01364("")


def test_bucket_by_tag_01364():
    p = Product_01364("s1", 100, ["a"])
    assert bucket_by_tag_01364([p]) == {"a": ["s1"]}
