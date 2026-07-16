"""Tests for catalog_01182."""

import pytest

from cartservice.generated.catalog_01182 import (
    Product_01182,
    bucket_by_tag_01182,
    is_valid_sku_01182,
    price_with_tax_01182,
)


def test_price_with_tax_01182():
    assert price_with_tax_01182(1000, 500) == 1050


def test_price_with_tax_negative_01182():
    with pytest.raises(ValueError):
        price_with_tax_01182(1000, -1)


def test_is_valid_sku_01182():
    assert is_valid_sku_01182("abc123")
    assert not is_valid_sku_01182("")


def test_bucket_by_tag_01182():
    p = Product_01182("s1", 100, ["a"])
    assert bucket_by_tag_01182([p]) == {"a": ["s1"]}
