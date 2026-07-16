"""Tests for catalog_00837."""

import pytest

from cartservice.generated.catalog_00837 import (
    Product_00837,
    bucket_by_tag_00837,
    is_valid_sku_00837,
    price_with_tax_00837,
)


def test_price_with_tax_00837():
    assert price_with_tax_00837(1000, 500) == 1050


def test_price_with_tax_negative_00837():
    with pytest.raises(ValueError):
        price_with_tax_00837(1000, -1)


def test_is_valid_sku_00837():
    assert is_valid_sku_00837("abc123")
    assert not is_valid_sku_00837("")


def test_bucket_by_tag_00837():
    p = Product_00837("s1", 100, ["a"])
    assert bucket_by_tag_00837([p]) == {"a": ["s1"]}
