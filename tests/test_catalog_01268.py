"""Tests for catalog_01268."""

import pytest

from cartservice.generated.catalog_01268 import (
    Product_01268,
    bucket_by_tag_01268,
    is_valid_sku_01268,
    price_with_tax_01268,
)


def test_price_with_tax_01268():
    assert price_with_tax_01268(1000, 500) == 1050


def test_price_with_tax_negative_01268():
    with pytest.raises(ValueError):
        price_with_tax_01268(1000, -1)


def test_is_valid_sku_01268():
    assert is_valid_sku_01268("abc123")
    assert not is_valid_sku_01268("")


def test_bucket_by_tag_01268():
    p = Product_01268("s1", 100, ["a"])
    assert bucket_by_tag_01268([p]) == {"a": ["s1"]}
