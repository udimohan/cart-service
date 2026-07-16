"""Tests for catalog_01544."""

import pytest

from cartservice.generated.catalog_01544 import (
    Product_01544,
    bucket_by_tag_01544,
    is_valid_sku_01544,
    price_with_tax_01544,
)


def test_price_with_tax_01544():
    assert price_with_tax_01544(1000, 500) == 1050


def test_price_with_tax_negative_01544():
    with pytest.raises(ValueError):
        price_with_tax_01544(1000, -1)


def test_is_valid_sku_01544():
    assert is_valid_sku_01544("abc123")
    assert not is_valid_sku_01544("")


def test_bucket_by_tag_01544():
    p = Product_01544("s1", 100, ["a"])
    assert bucket_by_tag_01544([p]) == {"a": ["s1"]}
