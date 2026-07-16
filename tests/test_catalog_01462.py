"""Tests for catalog_01462."""

import pytest

from cartservice.generated.catalog_01462 import (
    Product_01462,
    bucket_by_tag_01462,
    is_valid_sku_01462,
    price_with_tax_01462,
)


def test_price_with_tax_01462():
    assert price_with_tax_01462(1000, 500) == 1050


def test_price_with_tax_negative_01462():
    with pytest.raises(ValueError):
        price_with_tax_01462(1000, -1)


def test_is_valid_sku_01462():
    assert is_valid_sku_01462("abc123")
    assert not is_valid_sku_01462("")


def test_bucket_by_tag_01462():
    p = Product_01462("s1", 100, ["a"])
    assert bucket_by_tag_01462([p]) == {"a": ["s1"]}
