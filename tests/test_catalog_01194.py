"""Tests for catalog_01194."""

import pytest

from cartservice.generated.catalog_01194 import (
    Product_01194,
    bucket_by_tag_01194,
    is_valid_sku_01194,
    price_with_tax_01194,
)


def test_price_with_tax_01194():
    assert price_with_tax_01194(1000, 500) == 1050


def test_price_with_tax_negative_01194():
    with pytest.raises(ValueError):
        price_with_tax_01194(1000, -1)


def test_is_valid_sku_01194():
    assert is_valid_sku_01194("abc123")
    assert not is_valid_sku_01194("")


def test_bucket_by_tag_01194():
    p = Product_01194("s1", 100, ["a"])
    assert bucket_by_tag_01194([p]) == {"a": ["s1"]}
