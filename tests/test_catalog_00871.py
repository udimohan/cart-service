"""Tests for catalog_00871."""

import pytest

from cartservice.generated.catalog_00871 import (
    Product_00871,
    bucket_by_tag_00871,
    is_valid_sku_00871,
    price_with_tax_00871,
)


def test_price_with_tax_00871():
    assert price_with_tax_00871(1000, 500) == 1050


def test_price_with_tax_negative_00871():
    with pytest.raises(ValueError):
        price_with_tax_00871(1000, -1)


def test_is_valid_sku_00871():
    assert is_valid_sku_00871("abc123")
    assert not is_valid_sku_00871("")


def test_bucket_by_tag_00871():
    p = Product_00871("s1", 100, ["a"])
    assert bucket_by_tag_00871([p]) == {"a": ["s1"]}
