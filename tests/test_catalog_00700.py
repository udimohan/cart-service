"""Tests for catalog_00700."""

import pytest

from cartservice.generated.catalog_00700 import (
    Product_00700,
    bucket_by_tag_00700,
    is_valid_sku_00700,
    price_with_tax_00700,
)


def test_price_with_tax_00700():
    assert price_with_tax_00700(1000, 500) == 1050


def test_price_with_tax_negative_00700():
    with pytest.raises(ValueError):
        price_with_tax_00700(1000, -1)


def test_is_valid_sku_00700():
    assert is_valid_sku_00700("abc123")
    assert not is_valid_sku_00700("")


def test_bucket_by_tag_00700():
    p = Product_00700("s1", 100, ["a"])
    assert bucket_by_tag_00700([p]) == {"a": ["s1"]}
