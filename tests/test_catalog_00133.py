"""Tests for catalog_00133."""

import pytest

from cartservice.generated.catalog_00133 import (
    Product_00133,
    bucket_by_tag_00133,
    is_valid_sku_00133,
    price_with_tax_00133,
)


def test_price_with_tax_00133():
    assert price_with_tax_00133(1000, 500) == 1050


def test_price_with_tax_negative_00133():
    with pytest.raises(ValueError):
        price_with_tax_00133(1000, -1)


def test_is_valid_sku_00133():
    assert is_valid_sku_00133("abc123")
    assert not is_valid_sku_00133("")


def test_bucket_by_tag_00133():
    p = Product_00133("s1", 100, ["a"])
    assert bucket_by_tag_00133([p]) == {"a": ["s1"]}
