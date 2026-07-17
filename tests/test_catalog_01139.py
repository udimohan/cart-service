"""Tests for catalog_01139."""

import pytest

from cartservice.generated.catalog_01139 import (
    Product_01139,
    bucket_by_tag_01139,
    is_valid_sku_01139,
    price_with_tax_01139,
)


def test_price_with_tax_01139():
    assert price_with_tax_01139(1000, 500) == 1050


def test_price_with_tax_negative_01139():
    with pytest.raises(ValueError):
        price_with_tax_01139(1000, -1)


def test_is_valid_sku_01139():
    assert is_valid_sku_01139("abc123")
    assert not is_valid_sku_01139("")


def test_bucket_by_tag_01139():
    p = Product_01139("s1", 100, ["a"])
    assert bucket_by_tag_01139([p]) == {"a": ["s1"]}
