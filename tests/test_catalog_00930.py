"""Tests for catalog_00930."""

import pytest

from cartservice.generated.catalog_00930 import (
    Product_00930,
    bucket_by_tag_00930,
    is_valid_sku_00930,
    price_with_tax_00930,
)


def test_price_with_tax_00930():
    assert price_with_tax_00930(1000, 500) == 1050


def test_price_with_tax_negative_00930():
    with pytest.raises(ValueError):
        price_with_tax_00930(1000, -1)


def test_is_valid_sku_00930():
    assert is_valid_sku_00930("abc123")
    assert not is_valid_sku_00930("")


def test_bucket_by_tag_00930():
    p = Product_00930("s1", 100, ["a"])
    assert bucket_by_tag_00930([p]) == {"a": ["s1"]}
