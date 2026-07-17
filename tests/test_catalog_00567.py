"""Tests for catalog_00567."""

import pytest

from cartservice.generated.catalog_00567 import (
    Product_00567,
    bucket_by_tag_00567,
    is_valid_sku_00567,
    price_with_tax_00567,
)


def test_price_with_tax_00567():
    assert price_with_tax_00567(1000, 500) == 1050


def test_price_with_tax_negative_00567():
    with pytest.raises(ValueError):
        price_with_tax_00567(1000, -1)


def test_is_valid_sku_00567():
    assert is_valid_sku_00567("abc123")
    assert not is_valid_sku_00567("")


def test_bucket_by_tag_00567():
    p = Product_00567("s1", 100, ["a"])
    assert bucket_by_tag_00567([p]) == {"a": ["s1"]}
