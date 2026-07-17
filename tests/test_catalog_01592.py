"""Tests for catalog_01592."""

import pytest

from cartservice.generated.catalog_01592 import (
    Product_01592,
    bucket_by_tag_01592,
    is_valid_sku_01592,
    price_with_tax_01592,
)


def test_price_with_tax_01592():
    assert price_with_tax_01592(1000, 500) == 1050


def test_price_with_tax_negative_01592():
    with pytest.raises(ValueError):
        price_with_tax_01592(1000, -1)


def test_is_valid_sku_01592():
    assert is_valid_sku_01592("abc123")
    assert not is_valid_sku_01592("")


def test_bucket_by_tag_01592():
    p = Product_01592("s1", 100, ["a"])
    assert bucket_by_tag_01592([p]) == {"a": ["s1"]}
