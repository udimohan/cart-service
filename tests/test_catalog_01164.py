"""Tests for catalog_01164."""

import pytest

from cartservice.generated.catalog_01164 import (
    Product_01164,
    bucket_by_tag_01164,
    is_valid_sku_01164,
    price_with_tax_01164,
)


def test_price_with_tax_01164():
    assert price_with_tax_01164(1000, 500) == 1050


def test_price_with_tax_negative_01164():
    with pytest.raises(ValueError):
        price_with_tax_01164(1000, -1)


def test_is_valid_sku_01164():
    assert is_valid_sku_01164("abc123")
    assert not is_valid_sku_01164("")


def test_bucket_by_tag_01164():
    p = Product_01164("s1", 100, ["a"])
    assert bucket_by_tag_01164([p]) == {"a": ["s1"]}
