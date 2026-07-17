"""Tests for catalog_00010."""

import pytest

from cartservice.generated.catalog_00010 import (
    Product_00010,
    bucket_by_tag_00010,
    is_valid_sku_00010,
    price_with_tax_00010,
)


def test_price_with_tax_00010():
    assert price_with_tax_00010(1000, 500) == 1050


def test_price_with_tax_negative_00010():
    with pytest.raises(ValueError):
        price_with_tax_00010(1000, -1)


def test_is_valid_sku_00010():
    assert is_valid_sku_00010("abc123")
    assert not is_valid_sku_00010("")


def test_bucket_by_tag_00010():
    p = Product_00010("s1", 100, ["a"])
    assert bucket_by_tag_00010([p]) == {"a": ["s1"]}
