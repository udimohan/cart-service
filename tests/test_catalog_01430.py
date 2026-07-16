"""Tests for catalog_01430."""

import pytest

from cartservice.generated.catalog_01430 import (
    Product_01430,
    bucket_by_tag_01430,
    is_valid_sku_01430,
    price_with_tax_01430,
)


def test_price_with_tax_01430():
    assert price_with_tax_01430(1000, 500) == 1050


def test_price_with_tax_negative_01430():
    with pytest.raises(ValueError):
        price_with_tax_01430(1000, -1)


def test_is_valid_sku_01430():
    assert is_valid_sku_01430("abc123")
    assert not is_valid_sku_01430("")


def test_bucket_by_tag_01430():
    p = Product_01430("s1", 100, ["a"])
    assert bucket_by_tag_01430([p]) == {"a": ["s1"]}
