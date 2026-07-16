"""Tests for catalog_01484."""

import pytest

from cartservice.generated.catalog_01484 import (
    Product_01484,
    bucket_by_tag_01484,
    is_valid_sku_01484,
    price_with_tax_01484,
)


def test_price_with_tax_01484():
    assert price_with_tax_01484(1000, 500) == 1050


def test_price_with_tax_negative_01484():
    with pytest.raises(ValueError):
        price_with_tax_01484(1000, -1)


def test_is_valid_sku_01484():
    assert is_valid_sku_01484("abc123")
    assert not is_valid_sku_01484("")


def test_bucket_by_tag_01484():
    p = Product_01484("s1", 100, ["a"])
    assert bucket_by_tag_01484([p]) == {"a": ["s1"]}
