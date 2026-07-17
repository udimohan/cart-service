"""Tests for catalog_00462."""

import pytest

from cartservice.generated.catalog_00462 import (
    Product_00462,
    bucket_by_tag_00462,
    is_valid_sku_00462,
    price_with_tax_00462,
)


def test_price_with_tax_00462():
    assert price_with_tax_00462(1000, 500) == 1050


def test_price_with_tax_negative_00462():
    with pytest.raises(ValueError):
        price_with_tax_00462(1000, -1)


def test_is_valid_sku_00462():
    assert is_valid_sku_00462("abc123")
    assert not is_valid_sku_00462("")


def test_bucket_by_tag_00462():
    p = Product_00462("s1", 100, ["a"])
    assert bucket_by_tag_00462([p]) == {"a": ["s1"]}
