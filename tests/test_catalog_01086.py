"""Tests for catalog_01086."""

import pytest

from cartservice.generated.catalog_01086 import (
    Product_01086,
    bucket_by_tag_01086,
    is_valid_sku_01086,
    price_with_tax_01086,
)


def test_price_with_tax_01086():
    assert price_with_tax_01086(1000, 500) == 1050


def test_price_with_tax_negative_01086():
    with pytest.raises(ValueError):
        price_with_tax_01086(1000, -1)


def test_is_valid_sku_01086():
    assert is_valid_sku_01086("abc123")
    assert not is_valid_sku_01086("")


def test_bucket_by_tag_01086():
    p = Product_01086("s1", 100, ["a"])
    assert bucket_by_tag_01086([p]) == {"a": ["s1"]}
