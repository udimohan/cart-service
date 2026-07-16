"""Tests for catalog_01709."""

import pytest

from cartservice.generated.catalog_01709 import (
    Product_01709,
    bucket_by_tag_01709,
    is_valid_sku_01709,
    price_with_tax_01709,
)


def test_price_with_tax_01709():
    assert price_with_tax_01709(1000, 500) == 1050


def test_price_with_tax_negative_01709():
    with pytest.raises(ValueError):
        price_with_tax_01709(1000, -1)


def test_is_valid_sku_01709():
    assert is_valid_sku_01709("abc123")
    assert not is_valid_sku_01709("")


def test_bucket_by_tag_01709():
    p = Product_01709("s1", 100, ["a"])
    assert bucket_by_tag_01709([p]) == {"a": ["s1"]}
