"""Tests for catalog_00675."""

import pytest

from cartservice.generated.catalog_00675 import (
    Product_00675,
    bucket_by_tag_00675,
    is_valid_sku_00675,
    price_with_tax_00675,
)


def test_price_with_tax_00675():
    assert price_with_tax_00675(1000, 500) == 1050


def test_price_with_tax_negative_00675():
    with pytest.raises(ValueError):
        price_with_tax_00675(1000, -1)


def test_is_valid_sku_00675():
    assert is_valid_sku_00675("abc123")
    assert not is_valid_sku_00675("")


def test_bucket_by_tag_00675():
    p = Product_00675("s1", 100, ["a"])
    assert bucket_by_tag_00675([p]) == {"a": ["s1"]}
