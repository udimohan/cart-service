"""Tests for catalog_01356."""

import pytest

from cartservice.generated.catalog_01356 import (
    Product_01356,
    bucket_by_tag_01356,
    is_valid_sku_01356,
    price_with_tax_01356,
)


def test_price_with_tax_01356():
    assert price_with_tax_01356(1000, 500) == 1050


def test_price_with_tax_negative_01356():
    with pytest.raises(ValueError):
        price_with_tax_01356(1000, -1)


def test_is_valid_sku_01356():
    assert is_valid_sku_01356("abc123")
    assert not is_valid_sku_01356("")


def test_bucket_by_tag_01356():
    p = Product_01356("s1", 100, ["a"])
    assert bucket_by_tag_01356([p]) == {"a": ["s1"]}
