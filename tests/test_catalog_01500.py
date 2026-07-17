"""Tests for catalog_01500."""

import pytest

from cartservice.generated.catalog_01500 import (
    Product_01500,
    bucket_by_tag_01500,
    is_valid_sku_01500,
    price_with_tax_01500,
)


def test_price_with_tax_01500():
    assert price_with_tax_01500(1000, 500) == 1050


def test_price_with_tax_negative_01500():
    with pytest.raises(ValueError):
        price_with_tax_01500(1000, -1)


def test_is_valid_sku_01500():
    assert is_valid_sku_01500("abc123")
    assert not is_valid_sku_01500("")


def test_bucket_by_tag_01500():
    p = Product_01500("s1", 100, ["a"])
    assert bucket_by_tag_01500([p]) == {"a": ["s1"]}
