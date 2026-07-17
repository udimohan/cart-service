"""Tests for catalog_00084."""

import pytest

from cartservice.generated.catalog_00084 import (
    Product_00084,
    bucket_by_tag_00084,
    is_valid_sku_00084,
    price_with_tax_00084,
)


def test_price_with_tax_00084():
    assert price_with_tax_00084(1000, 500) == 1050


def test_price_with_tax_negative_00084():
    with pytest.raises(ValueError):
        price_with_tax_00084(1000, -1)


def test_is_valid_sku_00084():
    assert is_valid_sku_00084("abc123")
    assert not is_valid_sku_00084("")


def test_bucket_by_tag_00084():
    p = Product_00084("s1", 100, ["a"])
    assert bucket_by_tag_00084([p]) == {"a": ["s1"]}
