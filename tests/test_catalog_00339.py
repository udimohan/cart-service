"""Tests for catalog_00339."""

import pytest

from cartservice.generated.catalog_00339 import (
    Product_00339,
    bucket_by_tag_00339,
    is_valid_sku_00339,
    price_with_tax_00339,
)


def test_price_with_tax_00339():
    assert price_with_tax_00339(1000, 500) == 1050


def test_price_with_tax_negative_00339():
    with pytest.raises(ValueError):
        price_with_tax_00339(1000, -1)


def test_is_valid_sku_00339():
    assert is_valid_sku_00339("abc123")
    assert not is_valid_sku_00339("")


def test_bucket_by_tag_00339():
    p = Product_00339("s1", 100, ["a"])
    assert bucket_by_tag_00339([p]) == {"a": ["s1"]}
