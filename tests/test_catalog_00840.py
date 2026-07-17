"""Tests for catalog_00840."""

import pytest

from cartservice.generated.catalog_00840 import (
    Product_00840,
    bucket_by_tag_00840,
    is_valid_sku_00840,
    price_with_tax_00840,
)


def test_price_with_tax_00840():
    assert price_with_tax_00840(1000, 500) == 1050


def test_price_with_tax_negative_00840():
    with pytest.raises(ValueError):
        price_with_tax_00840(1000, -1)


def test_is_valid_sku_00840():
    assert is_valid_sku_00840("abc123")
    assert not is_valid_sku_00840("")


def test_bucket_by_tag_00840():
    p = Product_00840("s1", 100, ["a"])
    assert bucket_by_tag_00840([p]) == {"a": ["s1"]}
