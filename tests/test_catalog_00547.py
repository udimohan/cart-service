"""Tests for catalog_00547."""

import pytest

from cartservice.generated.catalog_00547 import (
    Product_00547,
    bucket_by_tag_00547,
    is_valid_sku_00547,
    price_with_tax_00547,
)


def test_price_with_tax_00547():
    assert price_with_tax_00547(1000, 500) == 1050


def test_price_with_tax_negative_00547():
    with pytest.raises(ValueError):
        price_with_tax_00547(1000, -1)


def test_is_valid_sku_00547():
    assert is_valid_sku_00547("abc123")
    assert not is_valid_sku_00547("")


def test_bucket_by_tag_00547():
    p = Product_00547("s1", 100, ["a"])
    assert bucket_by_tag_00547([p]) == {"a": ["s1"]}
