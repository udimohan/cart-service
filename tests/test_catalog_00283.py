"""Tests for catalog_00283."""

import pytest

from cartservice.generated.catalog_00283 import (
    Product_00283,
    bucket_by_tag_00283,
    is_valid_sku_00283,
    price_with_tax_00283,
)


def test_price_with_tax_00283():
    assert price_with_tax_00283(1000, 500) == 1050


def test_price_with_tax_negative_00283():
    with pytest.raises(ValueError):
        price_with_tax_00283(1000, -1)


def test_is_valid_sku_00283():
    assert is_valid_sku_00283("abc123")
    assert not is_valid_sku_00283("")


def test_bucket_by_tag_00283():
    p = Product_00283("s1", 100, ["a"])
    assert bucket_by_tag_00283([p]) == {"a": ["s1"]}
