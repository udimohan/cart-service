"""Tests for catalog_00182."""

import pytest

from cartservice.generated.catalog_00182 import (
    Product_00182,
    bucket_by_tag_00182,
    is_valid_sku_00182,
    price_with_tax_00182,
)


def test_price_with_tax_00182():
    assert price_with_tax_00182(1000, 500) == 1050


def test_price_with_tax_negative_00182():
    with pytest.raises(ValueError):
        price_with_tax_00182(1000, -1)


def test_is_valid_sku_00182():
    assert is_valid_sku_00182("abc123")
    assert not is_valid_sku_00182("")


def test_bucket_by_tag_00182():
    p = Product_00182("s1", 100, ["a"])
    assert bucket_by_tag_00182([p]) == {"a": ["s1"]}
