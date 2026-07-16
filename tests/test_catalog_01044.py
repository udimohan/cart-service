"""Tests for catalog_01044."""

import pytest

from cartservice.generated.catalog_01044 import (
    Product_01044,
    bucket_by_tag_01044,
    is_valid_sku_01044,
    price_with_tax_01044,
)


def test_price_with_tax_01044():
    assert price_with_tax_01044(1000, 500) == 1050


def test_price_with_tax_negative_01044():
    with pytest.raises(ValueError):
        price_with_tax_01044(1000, -1)


def test_is_valid_sku_01044():
    assert is_valid_sku_01044("abc123")
    assert not is_valid_sku_01044("")


def test_bucket_by_tag_01044():
    p = Product_01044("s1", 100, ["a"])
    assert bucket_by_tag_01044([p]) == {"a": ["s1"]}
