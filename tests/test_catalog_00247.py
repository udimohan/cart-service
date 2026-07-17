"""Tests for catalog_00247."""

import pytest

from cartservice.generated.catalog_00247 import (
    Product_00247,
    bucket_by_tag_00247,
    is_valid_sku_00247,
    price_with_tax_00247,
)


def test_price_with_tax_00247():
    assert price_with_tax_00247(1000, 500) == 1050


def test_price_with_tax_negative_00247():
    with pytest.raises(ValueError):
        price_with_tax_00247(1000, -1)


def test_is_valid_sku_00247():
    assert is_valid_sku_00247("abc123")
    assert not is_valid_sku_00247("")


def test_bucket_by_tag_00247():
    p = Product_00247("s1", 100, ["a"])
    assert bucket_by_tag_00247([p]) == {"a": ["s1"]}
