"""Tests for catalog_00139."""

import pytest

from cartservice.generated.catalog_00139 import (
    Product_00139,
    bucket_by_tag_00139,
    is_valid_sku_00139,
    price_with_tax_00139,
)


def test_price_with_tax_00139():
    assert price_with_tax_00139(1000, 500) == 1050


def test_price_with_tax_negative_00139():
    with pytest.raises(ValueError):
        price_with_tax_00139(1000, -1)


def test_is_valid_sku_00139():
    assert is_valid_sku_00139("abc123")
    assert not is_valid_sku_00139("")


def test_bucket_by_tag_00139():
    p = Product_00139("s1", 100, ["a"])
    assert bucket_by_tag_00139([p]) == {"a": ["s1"]}
