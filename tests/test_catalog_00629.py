"""Tests for catalog_00629."""

import pytest

from cartservice.generated.catalog_00629 import (
    Product_00629,
    bucket_by_tag_00629,
    is_valid_sku_00629,
    price_with_tax_00629,
)


def test_price_with_tax_00629():
    assert price_with_tax_00629(1000, 500) == 1050


def test_price_with_tax_negative_00629():
    with pytest.raises(ValueError):
        price_with_tax_00629(1000, -1)


def test_is_valid_sku_00629():
    assert is_valid_sku_00629("abc123")
    assert not is_valid_sku_00629("")


def test_bucket_by_tag_00629():
    p = Product_00629("s1", 100, ["a"])
    assert bucket_by_tag_00629([p]) == {"a": ["s1"]}
