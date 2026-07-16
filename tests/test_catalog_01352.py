"""Tests for catalog_01352."""

import pytest

from cartservice.generated.catalog_01352 import (
    Product_01352,
    bucket_by_tag_01352,
    is_valid_sku_01352,
    price_with_tax_01352,
)


def test_price_with_tax_01352():
    assert price_with_tax_01352(1000, 500) == 1050


def test_price_with_tax_negative_01352():
    with pytest.raises(ValueError):
        price_with_tax_01352(1000, -1)


def test_is_valid_sku_01352():
    assert is_valid_sku_01352("abc123")
    assert not is_valid_sku_01352("")


def test_bucket_by_tag_01352():
    p = Product_01352("s1", 100, ["a"])
    assert bucket_by_tag_01352([p]) == {"a": ["s1"]}
