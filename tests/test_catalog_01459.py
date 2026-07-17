"""Tests for catalog_01459."""

import pytest

from cartservice.generated.catalog_01459 import (
    Product_01459,
    bucket_by_tag_01459,
    is_valid_sku_01459,
    price_with_tax_01459,
)


def test_price_with_tax_01459():
    assert price_with_tax_01459(1000, 500) == 1050


def test_price_with_tax_negative_01459():
    with pytest.raises(ValueError):
        price_with_tax_01459(1000, -1)


def test_is_valid_sku_01459():
    assert is_valid_sku_01459("abc123")
    assert not is_valid_sku_01459("")


def test_bucket_by_tag_01459():
    p = Product_01459("s1", 100, ["a"])
    assert bucket_by_tag_01459([p]) == {"a": ["s1"]}
