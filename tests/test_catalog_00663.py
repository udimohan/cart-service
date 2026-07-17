"""Tests for catalog_00663."""

import pytest

from cartservice.generated.catalog_00663 import (
    Product_00663,
    bucket_by_tag_00663,
    is_valid_sku_00663,
    price_with_tax_00663,
)


def test_price_with_tax_00663():
    assert price_with_tax_00663(1000, 500) == 1050


def test_price_with_tax_negative_00663():
    with pytest.raises(ValueError):
        price_with_tax_00663(1000, -1)


def test_is_valid_sku_00663():
    assert is_valid_sku_00663("abc123")
    assert not is_valid_sku_00663("")


def test_bucket_by_tag_00663():
    p = Product_00663("s1", 100, ["a"])
    assert bucket_by_tag_00663([p]) == {"a": ["s1"]}
