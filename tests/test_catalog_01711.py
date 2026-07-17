"""Tests for catalog_01711."""

import pytest

from cartservice.generated.catalog_01711 import (
    Product_01711,
    bucket_by_tag_01711,
    is_valid_sku_01711,
    price_with_tax_01711,
)


def test_price_with_tax_01711():
    assert price_with_tax_01711(1000, 500) == 1050


def test_price_with_tax_negative_01711():
    with pytest.raises(ValueError):
        price_with_tax_01711(1000, -1)


def test_is_valid_sku_01711():
    assert is_valid_sku_01711("abc123")
    assert not is_valid_sku_01711("")


def test_bucket_by_tag_01711():
    p = Product_01711("s1", 100, ["a"])
    assert bucket_by_tag_01711([p]) == {"a": ["s1"]}
