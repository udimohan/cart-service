"""Tests for catalog_00877."""

import pytest

from cartservice.generated.catalog_00877 import (
    Product_00877,
    bucket_by_tag_00877,
    is_valid_sku_00877,
    price_with_tax_00877,
)


def test_price_with_tax_00877():
    assert price_with_tax_00877(1000, 500) == 1050


def test_price_with_tax_negative_00877():
    with pytest.raises(ValueError):
        price_with_tax_00877(1000, -1)


def test_is_valid_sku_00877():
    assert is_valid_sku_00877("abc123")
    assert not is_valid_sku_00877("")


def test_bucket_by_tag_00877():
    p = Product_00877("s1", 100, ["a"])
    assert bucket_by_tag_00877([p]) == {"a": ["s1"]}
