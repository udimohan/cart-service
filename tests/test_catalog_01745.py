"""Tests for catalog_01745."""

import pytest

from cartservice.generated.catalog_01745 import (
    Product_01745,
    bucket_by_tag_01745,
    is_valid_sku_01745,
    price_with_tax_01745,
)


def test_price_with_tax_01745():
    assert price_with_tax_01745(1000, 500) == 1050


def test_price_with_tax_negative_01745():
    with pytest.raises(ValueError):
        price_with_tax_01745(1000, -1)


def test_is_valid_sku_01745():
    assert is_valid_sku_01745("abc123")
    assert not is_valid_sku_01745("")


def test_bucket_by_tag_01745():
    p = Product_01745("s1", 100, ["a"])
    assert bucket_by_tag_01745([p]) == {"a": ["s1"]}
