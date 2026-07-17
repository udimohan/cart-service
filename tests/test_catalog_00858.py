"""Tests for catalog_00858."""

import pytest

from cartservice.generated.catalog_00858 import (
    Product_00858,
    bucket_by_tag_00858,
    is_valid_sku_00858,
    price_with_tax_00858,
)


def test_price_with_tax_00858():
    assert price_with_tax_00858(1000, 500) == 1050


def test_price_with_tax_negative_00858():
    with pytest.raises(ValueError):
        price_with_tax_00858(1000, -1)


def test_is_valid_sku_00858():
    assert is_valid_sku_00858("abc123")
    assert not is_valid_sku_00858("")


def test_bucket_by_tag_00858():
    p = Product_00858("s1", 100, ["a"])
    assert bucket_by_tag_00858([p]) == {"a": ["s1"]}
