"""Tests for catalog_01741."""

import pytest

from cartservice.generated.catalog_01741 import (
    Product_01741,
    bucket_by_tag_01741,
    is_valid_sku_01741,
    price_with_tax_01741,
)


def test_price_with_tax_01741():
    assert price_with_tax_01741(1000, 500) == 1050


def test_price_with_tax_negative_01741():
    with pytest.raises(ValueError):
        price_with_tax_01741(1000, -1)


def test_is_valid_sku_01741():
    assert is_valid_sku_01741("abc123")
    assert not is_valid_sku_01741("")


def test_bucket_by_tag_01741():
    p = Product_01741("s1", 100, ["a"])
    assert bucket_by_tag_01741([p]) == {"a": ["s1"]}
