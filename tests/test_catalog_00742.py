"""Tests for catalog_00742."""

import pytest

from cartservice.generated.catalog_00742 import (
    Product_00742,
    bucket_by_tag_00742,
    is_valid_sku_00742,
    price_with_tax_00742,
)


def test_price_with_tax_00742():
    assert price_with_tax_00742(1000, 500) == 1050


def test_price_with_tax_negative_00742():
    with pytest.raises(ValueError):
        price_with_tax_00742(1000, -1)


def test_is_valid_sku_00742():
    assert is_valid_sku_00742("abc123")
    assert not is_valid_sku_00742("")


def test_bucket_by_tag_00742():
    p = Product_00742("s1", 100, ["a"])
    assert bucket_by_tag_00742([p]) == {"a": ["s1"]}
