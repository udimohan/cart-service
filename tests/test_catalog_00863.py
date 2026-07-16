"""Tests for catalog_00863."""

import pytest

from cartservice.generated.catalog_00863 import (
    Product_00863,
    bucket_by_tag_00863,
    is_valid_sku_00863,
    price_with_tax_00863,
)


def test_price_with_tax_00863():
    assert price_with_tax_00863(1000, 500) == 1050


def test_price_with_tax_negative_00863():
    with pytest.raises(ValueError):
        price_with_tax_00863(1000, -1)


def test_is_valid_sku_00863():
    assert is_valid_sku_00863("abc123")
    assert not is_valid_sku_00863("")


def test_bucket_by_tag_00863():
    p = Product_00863("s1", 100, ["a"])
    assert bucket_by_tag_00863([p]) == {"a": ["s1"]}
