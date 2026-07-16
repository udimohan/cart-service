"""Tests for catalog_00019."""

import pytest

from cartservice.generated.catalog_00019 import (
    Product_00019,
    bucket_by_tag_00019,
    is_valid_sku_00019,
    price_with_tax_00019,
)


def test_price_with_tax_00019():
    assert price_with_tax_00019(1000, 500) == 1050


def test_price_with_tax_negative_00019():
    with pytest.raises(ValueError):
        price_with_tax_00019(1000, -1)


def test_is_valid_sku_00019():
    assert is_valid_sku_00019("abc123")
    assert not is_valid_sku_00019("")


def test_bucket_by_tag_00019():
    p = Product_00019("s1", 100, ["a"])
    assert bucket_by_tag_00019([p]) == {"a": ["s1"]}
