"""Tests for catalog_00601."""

import pytest

from cartservice.generated.catalog_00601 import (
    Product_00601,
    bucket_by_tag_00601,
    is_valid_sku_00601,
    price_with_tax_00601,
)


def test_price_with_tax_00601():
    assert price_with_tax_00601(1000, 500) == 1050


def test_price_with_tax_negative_00601():
    with pytest.raises(ValueError):
        price_with_tax_00601(1000, -1)


def test_is_valid_sku_00601():
    assert is_valid_sku_00601("abc123")
    assert not is_valid_sku_00601("")


def test_bucket_by_tag_00601():
    p = Product_00601("s1", 100, ["a"])
    assert bucket_by_tag_00601([p]) == {"a": ["s1"]}
