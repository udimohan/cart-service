"""Tests for catalog_00488."""

import pytest

from cartservice.generated.catalog_00488 import (
    Product_00488,
    bucket_by_tag_00488,
    is_valid_sku_00488,
    price_with_tax_00488,
)


def test_price_with_tax_00488():
    assert price_with_tax_00488(1000, 500) == 1050


def test_price_with_tax_negative_00488():
    with pytest.raises(ValueError):
        price_with_tax_00488(1000, -1)


def test_is_valid_sku_00488():
    assert is_valid_sku_00488("abc123")
    assert not is_valid_sku_00488("")


def test_bucket_by_tag_00488():
    p = Product_00488("s1", 100, ["a"])
    assert bucket_by_tag_00488([p]) == {"a": ["s1"]}
