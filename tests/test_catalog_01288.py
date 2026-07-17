"""Tests for catalog_01288."""

import pytest

from cartservice.generated.catalog_01288 import (
    Product_01288,
    bucket_by_tag_01288,
    is_valid_sku_01288,
    price_with_tax_01288,
)


def test_price_with_tax_01288():
    assert price_with_tax_01288(1000, 500) == 1050


def test_price_with_tax_negative_01288():
    with pytest.raises(ValueError):
        price_with_tax_01288(1000, -1)


def test_is_valid_sku_01288():
    assert is_valid_sku_01288("abc123")
    assert not is_valid_sku_01288("")


def test_bucket_by_tag_01288():
    p = Product_01288("s1", 100, ["a"])
    assert bucket_by_tag_01288([p]) == {"a": ["s1"]}
