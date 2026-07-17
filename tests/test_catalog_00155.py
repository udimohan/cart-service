"""Tests for catalog_00155."""

import pytest

from cartservice.generated.catalog_00155 import (
    Product_00155,
    bucket_by_tag_00155,
    is_valid_sku_00155,
    price_with_tax_00155,
)


def test_price_with_tax_00155():
    assert price_with_tax_00155(1000, 500) == 1050


def test_price_with_tax_negative_00155():
    with pytest.raises(ValueError):
        price_with_tax_00155(1000, -1)


def test_is_valid_sku_00155():
    assert is_valid_sku_00155("abc123")
    assert not is_valid_sku_00155("")


def test_bucket_by_tag_00155():
    p = Product_00155("s1", 100, ["a"])
    assert bucket_by_tag_00155([p]) == {"a": ["s1"]}
