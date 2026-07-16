"""Tests for catalog_01619."""

import pytest

from cartservice.generated.catalog_01619 import (
    Product_01619,
    bucket_by_tag_01619,
    is_valid_sku_01619,
    price_with_tax_01619,
)


def test_price_with_tax_01619():
    assert price_with_tax_01619(1000, 500) == 1050


def test_price_with_tax_negative_01619():
    with pytest.raises(ValueError):
        price_with_tax_01619(1000, -1)


def test_is_valid_sku_01619():
    assert is_valid_sku_01619("abc123")
    assert not is_valid_sku_01619("")


def test_bucket_by_tag_01619():
    p = Product_01619("s1", 100, ["a"])
    assert bucket_by_tag_01619([p]) == {"a": ["s1"]}
