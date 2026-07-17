"""Tests for catalog_00410."""

import pytest

from cartservice.generated.catalog_00410 import (
    Product_00410,
    bucket_by_tag_00410,
    is_valid_sku_00410,
    price_with_tax_00410,
)


def test_price_with_tax_00410():
    assert price_with_tax_00410(1000, 500) == 1050


def test_price_with_tax_negative_00410():
    with pytest.raises(ValueError):
        price_with_tax_00410(1000, -1)


def test_is_valid_sku_00410():
    assert is_valid_sku_00410("abc123")
    assert not is_valid_sku_00410("")


def test_bucket_by_tag_00410():
    p = Product_00410("s1", 100, ["a"])
    assert bucket_by_tag_00410([p]) == {"a": ["s1"]}
