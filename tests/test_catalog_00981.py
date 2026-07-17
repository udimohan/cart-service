"""Tests for catalog_00981."""

import pytest

from cartservice.generated.catalog_00981 import (
    Product_00981,
    bucket_by_tag_00981,
    is_valid_sku_00981,
    price_with_tax_00981,
)


def test_price_with_tax_00981():
    assert price_with_tax_00981(1000, 500) == 1050


def test_price_with_tax_negative_00981():
    with pytest.raises(ValueError):
        price_with_tax_00981(1000, -1)


def test_is_valid_sku_00981():
    assert is_valid_sku_00981("abc123")
    assert not is_valid_sku_00981("")


def test_bucket_by_tag_00981():
    p = Product_00981("s1", 100, ["a"])
    assert bucket_by_tag_00981([p]) == {"a": ["s1"]}
