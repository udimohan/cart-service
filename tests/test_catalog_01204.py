"""Tests for catalog_01204."""

import pytest

from cartservice.generated.catalog_01204 import (
    Product_01204,
    bucket_by_tag_01204,
    is_valid_sku_01204,
    price_with_tax_01204,
)


def test_price_with_tax_01204():
    assert price_with_tax_01204(1000, 500) == 1050


def test_price_with_tax_negative_01204():
    with pytest.raises(ValueError):
        price_with_tax_01204(1000, -1)


def test_is_valid_sku_01204():
    assert is_valid_sku_01204("abc123")
    assert not is_valid_sku_01204("")


def test_bucket_by_tag_01204():
    p = Product_01204("s1", 100, ["a"])
    assert bucket_by_tag_01204([p]) == {"a": ["s1"]}
