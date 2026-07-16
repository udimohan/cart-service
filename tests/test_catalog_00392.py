"""Tests for catalog_00392."""

import pytest

from cartservice.generated.catalog_00392 import (
    Product_00392,
    bucket_by_tag_00392,
    is_valid_sku_00392,
    price_with_tax_00392,
)


def test_price_with_tax_00392():
    assert price_with_tax_00392(1000, 500) == 1050


def test_price_with_tax_negative_00392():
    with pytest.raises(ValueError):
        price_with_tax_00392(1000, -1)


def test_is_valid_sku_00392():
    assert is_valid_sku_00392("abc123")
    assert not is_valid_sku_00392("")


def test_bucket_by_tag_00392():
    p = Product_00392("s1", 100, ["a"])
    assert bucket_by_tag_00392([p]) == {"a": ["s1"]}
