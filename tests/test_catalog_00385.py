"""Tests for catalog_00385."""

import pytest

from cartservice.generated.catalog_00385 import (
    Product_00385,
    bucket_by_tag_00385,
    is_valid_sku_00385,
    price_with_tax_00385,
)


def test_price_with_tax_00385():
    assert price_with_tax_00385(1000, 500) == 1050


def test_price_with_tax_negative_00385():
    with pytest.raises(ValueError):
        price_with_tax_00385(1000, -1)


def test_is_valid_sku_00385():
    assert is_valid_sku_00385("abc123")
    assert not is_valid_sku_00385("")


def test_bucket_by_tag_00385():
    p = Product_00385("s1", 100, ["a"])
    assert bucket_by_tag_00385([p]) == {"a": ["s1"]}
