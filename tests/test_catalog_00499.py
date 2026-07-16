"""Tests for catalog_00499."""

import pytest

from cartservice.generated.catalog_00499 import (
    Product_00499,
    bucket_by_tag_00499,
    is_valid_sku_00499,
    price_with_tax_00499,
)


def test_price_with_tax_00499():
    assert price_with_tax_00499(1000, 500) == 1050


def test_price_with_tax_negative_00499():
    with pytest.raises(ValueError):
        price_with_tax_00499(1000, -1)


def test_is_valid_sku_00499():
    assert is_valid_sku_00499("abc123")
    assert not is_valid_sku_00499("")


def test_bucket_by_tag_00499():
    p = Product_00499("s1", 100, ["a"])
    assert bucket_by_tag_00499([p]) == {"a": ["s1"]}
