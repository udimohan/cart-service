"""Tests for catalog_00618."""

import pytest

from cartservice.generated.catalog_00618 import (
    Product_00618,
    bucket_by_tag_00618,
    is_valid_sku_00618,
    price_with_tax_00618,
)


def test_price_with_tax_00618():
    assert price_with_tax_00618(1000, 500) == 1050


def test_price_with_tax_negative_00618():
    with pytest.raises(ValueError):
        price_with_tax_00618(1000, -1)


def test_is_valid_sku_00618():
    assert is_valid_sku_00618("abc123")
    assert not is_valid_sku_00618("")


def test_bucket_by_tag_00618():
    p = Product_00618("s1", 100, ["a"])
    assert bucket_by_tag_00618([p]) == {"a": ["s1"]}
