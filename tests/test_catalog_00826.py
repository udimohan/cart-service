"""Tests for catalog_00826."""

import pytest

from cartservice.generated.catalog_00826 import (
    Product_00826,
    bucket_by_tag_00826,
    is_valid_sku_00826,
    price_with_tax_00826,
)


def test_price_with_tax_00826():
    assert price_with_tax_00826(1000, 500) == 1050


def test_price_with_tax_negative_00826():
    with pytest.raises(ValueError):
        price_with_tax_00826(1000, -1)


def test_is_valid_sku_00826():
    assert is_valid_sku_00826("abc123")
    assert not is_valid_sku_00826("")


def test_bucket_by_tag_00826():
    p = Product_00826("s1", 100, ["a"])
    assert bucket_by_tag_00826([p]) == {"a": ["s1"]}
