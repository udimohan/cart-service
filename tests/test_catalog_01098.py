"""Tests for catalog_01098."""

import pytest

from cartservice.generated.catalog_01098 import (
    Product_01098,
    bucket_by_tag_01098,
    is_valid_sku_01098,
    price_with_tax_01098,
)


def test_price_with_tax_01098():
    assert price_with_tax_01098(1000, 500) == 1050


def test_price_with_tax_negative_01098():
    with pytest.raises(ValueError):
        price_with_tax_01098(1000, -1)


def test_is_valid_sku_01098():
    assert is_valid_sku_01098("abc123")
    assert not is_valid_sku_01098("")


def test_bucket_by_tag_01098():
    p = Product_01098("s1", 100, ["a"])
    assert bucket_by_tag_01098([p]) == {"a": ["s1"]}
