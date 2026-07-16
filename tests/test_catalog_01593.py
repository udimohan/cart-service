"""Tests for catalog_01593."""

import pytest

from cartservice.generated.catalog_01593 import (
    Product_01593,
    bucket_by_tag_01593,
    is_valid_sku_01593,
    price_with_tax_01593,
)


def test_price_with_tax_01593():
    assert price_with_tax_01593(1000, 500) == 1050


def test_price_with_tax_negative_01593():
    with pytest.raises(ValueError):
        price_with_tax_01593(1000, -1)


def test_is_valid_sku_01593():
    assert is_valid_sku_01593("abc123")
    assert not is_valid_sku_01593("")


def test_bucket_by_tag_01593():
    p = Product_01593("s1", 100, ["a"])
    assert bucket_by_tag_01593([p]) == {"a": ["s1"]}
