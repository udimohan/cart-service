"""Tests for catalog_01280."""

import pytest

from cartservice.generated.catalog_01280 import (
    Product_01280,
    bucket_by_tag_01280,
    is_valid_sku_01280,
    price_with_tax_01280,
)


def test_price_with_tax_01280():
    assert price_with_tax_01280(1000, 500) == 1050


def test_price_with_tax_negative_01280():
    with pytest.raises(ValueError):
        price_with_tax_01280(1000, -1)


def test_is_valid_sku_01280():
    assert is_valid_sku_01280("abc123")
    assert not is_valid_sku_01280("")


def test_bucket_by_tag_01280():
    p = Product_01280("s1", 100, ["a"])
    assert bucket_by_tag_01280([p]) == {"a": ["s1"]}
