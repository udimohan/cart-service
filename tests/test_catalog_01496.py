"""Tests for catalog_01496."""

import pytest

from cartservice.generated.catalog_01496 import (
    Product_01496,
    bucket_by_tag_01496,
    is_valid_sku_01496,
    price_with_tax_01496,
)


def test_price_with_tax_01496():
    assert price_with_tax_01496(1000, 500) == 1050


def test_price_with_tax_negative_01496():
    with pytest.raises(ValueError):
        price_with_tax_01496(1000, -1)


def test_is_valid_sku_01496():
    assert is_valid_sku_01496("abc123")
    assert not is_valid_sku_01496("")


def test_bucket_by_tag_01496():
    p = Product_01496("s1", 100, ["a"])
    assert bucket_by_tag_01496([p]) == {"a": ["s1"]}
