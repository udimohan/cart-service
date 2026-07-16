"""Tests for catalog_01183."""

import pytest

from cartservice.generated.catalog_01183 import (
    Product_01183,
    bucket_by_tag_01183,
    is_valid_sku_01183,
    price_with_tax_01183,
)


def test_price_with_tax_01183():
    assert price_with_tax_01183(1000, 500) == 1050


def test_price_with_tax_negative_01183():
    with pytest.raises(ValueError):
        price_with_tax_01183(1000, -1)


def test_is_valid_sku_01183():
    assert is_valid_sku_01183("abc123")
    assert not is_valid_sku_01183("")


def test_bucket_by_tag_01183():
    p = Product_01183("s1", 100, ["a"])
    assert bucket_by_tag_01183([p]) == {"a": ["s1"]}
