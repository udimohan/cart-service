"""Tests for catalog_00965."""

import pytest

from cartservice.generated.catalog_00965 import (
    Product_00965,
    bucket_by_tag_00965,
    is_valid_sku_00965,
    price_with_tax_00965,
)


def test_price_with_tax_00965():
    assert price_with_tax_00965(1000, 500) == 1050


def test_price_with_tax_negative_00965():
    with pytest.raises(ValueError):
        price_with_tax_00965(1000, -1)


def test_is_valid_sku_00965():
    assert is_valid_sku_00965("abc123")
    assert not is_valid_sku_00965("")


def test_bucket_by_tag_00965():
    p = Product_00965("s1", 100, ["a"])
    assert bucket_by_tag_00965([p]) == {"a": ["s1"]}
