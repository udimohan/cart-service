"""Tests for catalog_01703."""

import pytest

from cartservice.generated.catalog_01703 import (
    Product_01703,
    bucket_by_tag_01703,
    is_valid_sku_01703,
    price_with_tax_01703,
)


def test_price_with_tax_01703():
    assert price_with_tax_01703(1000, 500) == 1050


def test_price_with_tax_negative_01703():
    with pytest.raises(ValueError):
        price_with_tax_01703(1000, -1)


def test_is_valid_sku_01703():
    assert is_valid_sku_01703("abc123")
    assert not is_valid_sku_01703("")


def test_bucket_by_tag_01703():
    p = Product_01703("s1", 100, ["a"])
    assert bucket_by_tag_01703([p]) == {"a": ["s1"]}
