"""Tests for catalog_00829."""

import pytest

from cartservice.generated.catalog_00829 import (
    Product_00829,
    bucket_by_tag_00829,
    is_valid_sku_00829,
    price_with_tax_00829,
)


def test_price_with_tax_00829():
    assert price_with_tax_00829(1000, 500) == 1050


def test_price_with_tax_negative_00829():
    with pytest.raises(ValueError):
        price_with_tax_00829(1000, -1)


def test_is_valid_sku_00829():
    assert is_valid_sku_00829("abc123")
    assert not is_valid_sku_00829("")


def test_bucket_by_tag_00829():
    p = Product_00829("s1", 100, ["a"])
    assert bucket_by_tag_00829([p]) == {"a": ["s1"]}
