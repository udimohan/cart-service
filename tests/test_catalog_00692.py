"""Tests for catalog_00692."""

import pytest

from cartservice.generated.catalog_00692 import (
    Product_00692,
    bucket_by_tag_00692,
    is_valid_sku_00692,
    price_with_tax_00692,
)


def test_price_with_tax_00692():
    assert price_with_tax_00692(1000, 500) == 1050


def test_price_with_tax_negative_00692():
    with pytest.raises(ValueError):
        price_with_tax_00692(1000, -1)


def test_is_valid_sku_00692():
    assert is_valid_sku_00692("abc123")
    assert not is_valid_sku_00692("")


def test_bucket_by_tag_00692():
    p = Product_00692("s1", 100, ["a"])
    assert bucket_by_tag_00692([p]) == {"a": ["s1"]}
