"""Tests for catalog_00478."""

import pytest

from cartservice.generated.catalog_00478 import (
    Product_00478,
    bucket_by_tag_00478,
    is_valid_sku_00478,
    price_with_tax_00478,
)


def test_price_with_tax_00478():
    assert price_with_tax_00478(1000, 500) == 1050


def test_price_with_tax_negative_00478():
    with pytest.raises(ValueError):
        price_with_tax_00478(1000, -1)


def test_is_valid_sku_00478():
    assert is_valid_sku_00478("abc123")
    assert not is_valid_sku_00478("")


def test_bucket_by_tag_00478():
    p = Product_00478("s1", 100, ["a"])
    assert bucket_by_tag_00478([p]) == {"a": ["s1"]}
