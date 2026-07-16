"""Tests for catalog_00183."""

import pytest

from cartservice.generated.catalog_00183 import (
    Product_00183,
    bucket_by_tag_00183,
    is_valid_sku_00183,
    price_with_tax_00183,
)


def test_price_with_tax_00183():
    assert price_with_tax_00183(1000, 500) == 1050


def test_price_with_tax_negative_00183():
    with pytest.raises(ValueError):
        price_with_tax_00183(1000, -1)


def test_is_valid_sku_00183():
    assert is_valid_sku_00183("abc123")
    assert not is_valid_sku_00183("")


def test_bucket_by_tag_00183():
    p = Product_00183("s1", 100, ["a"])
    assert bucket_by_tag_00183([p]) == {"a": ["s1"]}
