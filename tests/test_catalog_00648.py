"""Tests for catalog_00648."""

import pytest

from cartservice.generated.catalog_00648 import (
    Product_00648,
    bucket_by_tag_00648,
    is_valid_sku_00648,
    price_with_tax_00648,
)


def test_price_with_tax_00648():
    assert price_with_tax_00648(1000, 500) == 1050


def test_price_with_tax_negative_00648():
    with pytest.raises(ValueError):
        price_with_tax_00648(1000, -1)


def test_is_valid_sku_00648():
    assert is_valid_sku_00648("abc123")
    assert not is_valid_sku_00648("")


def test_bucket_by_tag_00648():
    p = Product_00648("s1", 100, ["a"])
    assert bucket_by_tag_00648([p]) == {"a": ["s1"]}
