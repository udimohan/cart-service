"""Tests for catalog_00722."""

import pytest

from cartservice.generated.catalog_00722 import (
    Product_00722,
    bucket_by_tag_00722,
    is_valid_sku_00722,
    price_with_tax_00722,
)


def test_price_with_tax_00722():
    assert price_with_tax_00722(1000, 500) == 1050


def test_price_with_tax_negative_00722():
    with pytest.raises(ValueError):
        price_with_tax_00722(1000, -1)


def test_is_valid_sku_00722():
    assert is_valid_sku_00722("abc123")
    assert not is_valid_sku_00722("")


def test_bucket_by_tag_00722():
    p = Product_00722("s1", 100, ["a"])
    assert bucket_by_tag_00722([p]) == {"a": ["s1"]}
