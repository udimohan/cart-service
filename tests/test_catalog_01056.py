"""Tests for catalog_01056."""

import pytest

from cartservice.generated.catalog_01056 import (
    Product_01056,
    bucket_by_tag_01056,
    is_valid_sku_01056,
    price_with_tax_01056,
)


def test_price_with_tax_01056():
    assert price_with_tax_01056(1000, 500) == 1050


def test_price_with_tax_negative_01056():
    with pytest.raises(ValueError):
        price_with_tax_01056(1000, -1)


def test_is_valid_sku_01056():
    assert is_valid_sku_01056("abc123")
    assert not is_valid_sku_01056("")


def test_bucket_by_tag_01056():
    p = Product_01056("s1", 100, ["a"])
    assert bucket_by_tag_01056([p]) == {"a": ["s1"]}
