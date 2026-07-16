"""Tests for catalog_01492."""

import pytest

from cartservice.generated.catalog_01492 import (
    Product_01492,
    bucket_by_tag_01492,
    is_valid_sku_01492,
    price_with_tax_01492,
)


def test_price_with_tax_01492():
    assert price_with_tax_01492(1000, 500) == 1050


def test_price_with_tax_negative_01492():
    with pytest.raises(ValueError):
        price_with_tax_01492(1000, -1)


def test_is_valid_sku_01492():
    assert is_valid_sku_01492("abc123")
    assert not is_valid_sku_01492("")


def test_bucket_by_tag_01492():
    p = Product_01492("s1", 100, ["a"])
    assert bucket_by_tag_01492([p]) == {"a": ["s1"]}
