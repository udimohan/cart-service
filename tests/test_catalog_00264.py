"""Tests for catalog_00264."""

import pytest

from cartservice.generated.catalog_00264 import (
    Product_00264,
    bucket_by_tag_00264,
    is_valid_sku_00264,
    price_with_tax_00264,
)


def test_price_with_tax_00264():
    assert price_with_tax_00264(1000, 500) == 1050


def test_price_with_tax_negative_00264():
    with pytest.raises(ValueError):
        price_with_tax_00264(1000, -1)


def test_is_valid_sku_00264():
    assert is_valid_sku_00264("abc123")
    assert not is_valid_sku_00264("")


def test_bucket_by_tag_00264():
    p = Product_00264("s1", 100, ["a"])
    assert bucket_by_tag_00264([p]) == {"a": ["s1"]}
