"""Tests for catalog_01722."""

import pytest

from cartservice.generated.catalog_01722 import (
    Product_01722,
    bucket_by_tag_01722,
    is_valid_sku_01722,
    price_with_tax_01722,
)


def test_price_with_tax_01722():
    assert price_with_tax_01722(1000, 500) == 1050


def test_price_with_tax_negative_01722():
    with pytest.raises(ValueError):
        price_with_tax_01722(1000, -1)


def test_is_valid_sku_01722():
    assert is_valid_sku_01722("abc123")
    assert not is_valid_sku_01722("")


def test_bucket_by_tag_01722():
    p = Product_01722("s1", 100, ["a"])
    assert bucket_by_tag_01722([p]) == {"a": ["s1"]}
