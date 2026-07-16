"""Tests for catalog_01201."""

import pytest

from cartservice.generated.catalog_01201 import (
    Product_01201,
    bucket_by_tag_01201,
    is_valid_sku_01201,
    price_with_tax_01201,
)


def test_price_with_tax_01201():
    assert price_with_tax_01201(1000, 500) == 1050


def test_price_with_tax_negative_01201():
    with pytest.raises(ValueError):
        price_with_tax_01201(1000, -1)


def test_is_valid_sku_01201():
    assert is_valid_sku_01201("abc123")
    assert not is_valid_sku_01201("")


def test_bucket_by_tag_01201():
    p = Product_01201("s1", 100, ["a"])
    assert bucket_by_tag_01201([p]) == {"a": ["s1"]}
