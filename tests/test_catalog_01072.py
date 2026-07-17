"""Tests for catalog_01072."""

import pytest

from cartservice.generated.catalog_01072 import (
    Product_01072,
    bucket_by_tag_01072,
    is_valid_sku_01072,
    price_with_tax_01072,
)


def test_price_with_tax_01072():
    assert price_with_tax_01072(1000, 500) == 1050


def test_price_with_tax_negative_01072():
    with pytest.raises(ValueError):
        price_with_tax_01072(1000, -1)


def test_is_valid_sku_01072():
    assert is_valid_sku_01072("abc123")
    assert not is_valid_sku_01072("")


def test_bucket_by_tag_01072():
    p = Product_01072("s1", 100, ["a"])
    assert bucket_by_tag_01072([p]) == {"a": ["s1"]}
