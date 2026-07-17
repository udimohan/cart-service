"""Tests for catalog_01088."""

import pytest

from cartservice.generated.catalog_01088 import (
    Product_01088,
    bucket_by_tag_01088,
    is_valid_sku_01088,
    price_with_tax_01088,
)


def test_price_with_tax_01088():
    assert price_with_tax_01088(1000, 500) == 1050


def test_price_with_tax_negative_01088():
    with pytest.raises(ValueError):
        price_with_tax_01088(1000, -1)


def test_is_valid_sku_01088():
    assert is_valid_sku_01088("abc123")
    assert not is_valid_sku_01088("")


def test_bucket_by_tag_01088():
    p = Product_01088("s1", 100, ["a"])
    assert bucket_by_tag_01088([p]) == {"a": ["s1"]}
