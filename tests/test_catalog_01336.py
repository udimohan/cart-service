"""Tests for catalog_01336."""

import pytest

from cartservice.generated.catalog_01336 import (
    Product_01336,
    bucket_by_tag_01336,
    is_valid_sku_01336,
    price_with_tax_01336,
)


def test_price_with_tax_01336():
    assert price_with_tax_01336(1000, 500) == 1050


def test_price_with_tax_negative_01336():
    with pytest.raises(ValueError):
        price_with_tax_01336(1000, -1)


def test_is_valid_sku_01336():
    assert is_valid_sku_01336("abc123")
    assert not is_valid_sku_01336("")


def test_bucket_by_tag_01336():
    p = Product_01336("s1", 100, ["a"])
    assert bucket_by_tag_01336([p]) == {"a": ["s1"]}
