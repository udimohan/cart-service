"""Tests for catalog_01413."""

import pytest

from cartservice.generated.catalog_01413 import (
    Product_01413,
    bucket_by_tag_01413,
    is_valid_sku_01413,
    price_with_tax_01413,
)


def test_price_with_tax_01413():
    assert price_with_tax_01413(1000, 500) == 1050


def test_price_with_tax_negative_01413():
    with pytest.raises(ValueError):
        price_with_tax_01413(1000, -1)


def test_is_valid_sku_01413():
    assert is_valid_sku_01413("abc123")
    assert not is_valid_sku_01413("")


def test_bucket_by_tag_01413():
    p = Product_01413("s1", 100, ["a"])
    assert bucket_by_tag_01413([p]) == {"a": ["s1"]}
