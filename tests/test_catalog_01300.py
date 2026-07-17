"""Tests for catalog_01300."""

import pytest

from cartservice.generated.catalog_01300 import (
    Product_01300,
    bucket_by_tag_01300,
    is_valid_sku_01300,
    price_with_tax_01300,
)


def test_price_with_tax_01300():
    assert price_with_tax_01300(1000, 500) == 1050


def test_price_with_tax_negative_01300():
    with pytest.raises(ValueError):
        price_with_tax_01300(1000, -1)


def test_is_valid_sku_01300():
    assert is_valid_sku_01300("abc123")
    assert not is_valid_sku_01300("")


def test_bucket_by_tag_01300():
    p = Product_01300("s1", 100, ["a"])
    assert bucket_by_tag_01300([p]) == {"a": ["s1"]}
