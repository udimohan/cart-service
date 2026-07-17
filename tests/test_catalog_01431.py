"""Tests for catalog_01431."""

import pytest

from cartservice.generated.catalog_01431 import (
    Product_01431,
    bucket_by_tag_01431,
    is_valid_sku_01431,
    price_with_tax_01431,
)


def test_price_with_tax_01431():
    assert price_with_tax_01431(1000, 500) == 1050


def test_price_with_tax_negative_01431():
    with pytest.raises(ValueError):
        price_with_tax_01431(1000, -1)


def test_is_valid_sku_01431():
    assert is_valid_sku_01431("abc123")
    assert not is_valid_sku_01431("")


def test_bucket_by_tag_01431():
    p = Product_01431("s1", 100, ["a"])
    assert bucket_by_tag_01431([p]) == {"a": ["s1"]}
