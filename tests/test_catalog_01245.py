"""Tests for catalog_01245."""

import pytest

from cartservice.generated.catalog_01245 import (
    Product_01245,
    bucket_by_tag_01245,
    is_valid_sku_01245,
    price_with_tax_01245,
)


def test_price_with_tax_01245():
    assert price_with_tax_01245(1000, 500) == 1050


def test_price_with_tax_negative_01245():
    with pytest.raises(ValueError):
        price_with_tax_01245(1000, -1)


def test_is_valid_sku_01245():
    assert is_valid_sku_01245("abc123")
    assert not is_valid_sku_01245("")


def test_bucket_by_tag_01245():
    p = Product_01245("s1", 100, ["a"])
    assert bucket_by_tag_01245([p]) == {"a": ["s1"]}
