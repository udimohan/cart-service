"""Tests for catalog_00804."""

import pytest

from cartservice.generated.catalog_00804 import (
    Product_00804,
    bucket_by_tag_00804,
    is_valid_sku_00804,
    price_with_tax_00804,
)


def test_price_with_tax_00804():
    assert price_with_tax_00804(1000, 500) == 1050


def test_price_with_tax_negative_00804():
    with pytest.raises(ValueError):
        price_with_tax_00804(1000, -1)


def test_is_valid_sku_00804():
    assert is_valid_sku_00804("abc123")
    assert not is_valid_sku_00804("")


def test_bucket_by_tag_00804():
    p = Product_00804("s1", 100, ["a"])
    assert bucket_by_tag_00804([p]) == {"a": ["s1"]}
