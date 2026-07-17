"""Tests for catalog_01171."""

import pytest

from cartservice.generated.catalog_01171 import (
    Product_01171,
    bucket_by_tag_01171,
    is_valid_sku_01171,
    price_with_tax_01171,
)


def test_price_with_tax_01171():
    assert price_with_tax_01171(1000, 500) == 1050


def test_price_with_tax_negative_01171():
    with pytest.raises(ValueError):
        price_with_tax_01171(1000, -1)


def test_is_valid_sku_01171():
    assert is_valid_sku_01171("abc123")
    assert not is_valid_sku_01171("")


def test_bucket_by_tag_01171():
    p = Product_01171("s1", 100, ["a"])
    assert bucket_by_tag_01171([p]) == {"a": ["s1"]}
