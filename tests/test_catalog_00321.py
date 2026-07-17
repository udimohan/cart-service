"""Tests for catalog_00321."""

import pytest

from cartservice.generated.catalog_00321 import (
    Product_00321,
    bucket_by_tag_00321,
    is_valid_sku_00321,
    price_with_tax_00321,
)


def test_price_with_tax_00321():
    assert price_with_tax_00321(1000, 500) == 1050


def test_price_with_tax_negative_00321():
    with pytest.raises(ValueError):
        price_with_tax_00321(1000, -1)


def test_is_valid_sku_00321():
    assert is_valid_sku_00321("abc123")
    assert not is_valid_sku_00321("")


def test_bucket_by_tag_00321():
    p = Product_00321("s1", 100, ["a"])
    assert bucket_by_tag_00321([p]) == {"a": ["s1"]}
