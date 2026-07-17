"""Tests for catalog_00353."""

import pytest

from cartservice.generated.catalog_00353 import (
    Product_00353,
    bucket_by_tag_00353,
    is_valid_sku_00353,
    price_with_tax_00353,
)


def test_price_with_tax_00353():
    assert price_with_tax_00353(1000, 500) == 1050


def test_price_with_tax_negative_00353():
    with pytest.raises(ValueError):
        price_with_tax_00353(1000, -1)


def test_is_valid_sku_00353():
    assert is_valid_sku_00353("abc123")
    assert not is_valid_sku_00353("")


def test_bucket_by_tag_00353():
    p = Product_00353("s1", 100, ["a"])
    assert bucket_by_tag_00353([p]) == {"a": ["s1"]}
