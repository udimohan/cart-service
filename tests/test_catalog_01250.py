"""Tests for catalog_01250."""

import pytest

from cartservice.generated.catalog_01250 import (
    Product_01250,
    bucket_by_tag_01250,
    is_valid_sku_01250,
    price_with_tax_01250,
)


def test_price_with_tax_01250():
    assert price_with_tax_01250(1000, 500) == 1050


def test_price_with_tax_negative_01250():
    with pytest.raises(ValueError):
        price_with_tax_01250(1000, -1)


def test_is_valid_sku_01250():
    assert is_valid_sku_01250("abc123")
    assert not is_valid_sku_01250("")


def test_bucket_by_tag_01250():
    p = Product_01250("s1", 100, ["a"])
    assert bucket_by_tag_01250([p]) == {"a": ["s1"]}
