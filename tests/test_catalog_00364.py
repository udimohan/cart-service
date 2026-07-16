"""Tests for catalog_00364."""

import pytest

from cartservice.generated.catalog_00364 import (
    Product_00364,
    bucket_by_tag_00364,
    is_valid_sku_00364,
    price_with_tax_00364,
)


def test_price_with_tax_00364():
    assert price_with_tax_00364(1000, 500) == 1050


def test_price_with_tax_negative_00364():
    with pytest.raises(ValueError):
        price_with_tax_00364(1000, -1)


def test_is_valid_sku_00364():
    assert is_valid_sku_00364("abc123")
    assert not is_valid_sku_00364("")


def test_bucket_by_tag_00364():
    p = Product_00364("s1", 100, ["a"])
    assert bucket_by_tag_00364([p]) == {"a": ["s1"]}
