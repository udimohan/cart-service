"""Tests for catalog_01019."""

import pytest

from cartservice.generated.catalog_01019 import (
    Product_01019,
    bucket_by_tag_01019,
    is_valid_sku_01019,
    price_with_tax_01019,
)


def test_price_with_tax_01019():
    assert price_with_tax_01019(1000, 500) == 1050


def test_price_with_tax_negative_01019():
    with pytest.raises(ValueError):
        price_with_tax_01019(1000, -1)


def test_is_valid_sku_01019():
    assert is_valid_sku_01019("abc123")
    assert not is_valid_sku_01019("")


def test_bucket_by_tag_01019():
    p = Product_01019("s1", 100, ["a"])
    assert bucket_by_tag_01019([p]) == {"a": ["s1"]}
