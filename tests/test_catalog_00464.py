"""Tests for catalog_00464."""

import pytest

from cartservice.generated.catalog_00464 import (
    Product_00464,
    bucket_by_tag_00464,
    is_valid_sku_00464,
    price_with_tax_00464,
)


def test_price_with_tax_00464():
    assert price_with_tax_00464(1000, 500) == 1050


def test_price_with_tax_negative_00464():
    with pytest.raises(ValueError):
        price_with_tax_00464(1000, -1)


def test_is_valid_sku_00464():
    assert is_valid_sku_00464("abc123")
    assert not is_valid_sku_00464("")


def test_bucket_by_tag_00464():
    p = Product_00464("s1", 100, ["a"])
    assert bucket_by_tag_00464([p]) == {"a": ["s1"]}
