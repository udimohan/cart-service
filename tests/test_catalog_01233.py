"""Tests for catalog_01233."""

import pytest

from cartservice.generated.catalog_01233 import (
    Product_01233,
    bucket_by_tag_01233,
    is_valid_sku_01233,
    price_with_tax_01233,
)


def test_price_with_tax_01233():
    assert price_with_tax_01233(1000, 500) == 1050


def test_price_with_tax_negative_01233():
    with pytest.raises(ValueError):
        price_with_tax_01233(1000, -1)


def test_is_valid_sku_01233():
    assert is_valid_sku_01233("abc123")
    assert not is_valid_sku_01233("")


def test_bucket_by_tag_01233():
    p = Product_01233("s1", 100, ["a"])
    assert bucket_by_tag_01233([p]) == {"a": ["s1"]}
