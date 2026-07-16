"""Tests for catalog_01304."""

import pytest

from cartservice.generated.catalog_01304 import (
    Product_01304,
    bucket_by_tag_01304,
    is_valid_sku_01304,
    price_with_tax_01304,
)


def test_price_with_tax_01304():
    assert price_with_tax_01304(1000, 500) == 1050


def test_price_with_tax_negative_01304():
    with pytest.raises(ValueError):
        price_with_tax_01304(1000, -1)


def test_is_valid_sku_01304():
    assert is_valid_sku_01304("abc123")
    assert not is_valid_sku_01304("")


def test_bucket_by_tag_01304():
    p = Product_01304("s1", 100, ["a"])
    assert bucket_by_tag_01304([p]) == {"a": ["s1"]}
