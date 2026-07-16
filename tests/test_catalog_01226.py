"""Tests for catalog_01226."""

import pytest

from cartservice.generated.catalog_01226 import (
    Product_01226,
    bucket_by_tag_01226,
    is_valid_sku_01226,
    price_with_tax_01226,
)


def test_price_with_tax_01226():
    assert price_with_tax_01226(1000, 500) == 1050


def test_price_with_tax_negative_01226():
    with pytest.raises(ValueError):
        price_with_tax_01226(1000, -1)


def test_is_valid_sku_01226():
    assert is_valid_sku_01226("abc123")
    assert not is_valid_sku_01226("")


def test_bucket_by_tag_01226():
    p = Product_01226("s1", 100, ["a"])
    assert bucket_by_tag_01226([p]) == {"a": ["s1"]}
