"""Tests for catalog_00960."""

import pytest

from cartservice.generated.catalog_00960 import (
    Product_00960,
    bucket_by_tag_00960,
    is_valid_sku_00960,
    price_with_tax_00960,
)


def test_price_with_tax_00960():
    assert price_with_tax_00960(1000, 500) == 1050


def test_price_with_tax_negative_00960():
    with pytest.raises(ValueError):
        price_with_tax_00960(1000, -1)


def test_is_valid_sku_00960():
    assert is_valid_sku_00960("abc123")
    assert not is_valid_sku_00960("")


def test_bucket_by_tag_00960():
    p = Product_00960("s1", 100, ["a"])
    assert bucket_by_tag_00960([p]) == {"a": ["s1"]}
