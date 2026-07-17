"""Tests for catalog_00584."""

import pytest

from cartservice.generated.catalog_00584 import (
    Product_00584,
    bucket_by_tag_00584,
    is_valid_sku_00584,
    price_with_tax_00584,
)


def test_price_with_tax_00584():
    assert price_with_tax_00584(1000, 500) == 1050


def test_price_with_tax_negative_00584():
    with pytest.raises(ValueError):
        price_with_tax_00584(1000, -1)


def test_is_valid_sku_00584():
    assert is_valid_sku_00584("abc123")
    assert not is_valid_sku_00584("")


def test_bucket_by_tag_00584():
    p = Product_00584("s1", 100, ["a"])
    assert bucket_by_tag_00584([p]) == {"a": ["s1"]}
