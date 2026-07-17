"""Tests for catalog_01246."""

import pytest

from cartservice.generated.catalog_01246 import (
    Product_01246,
    bucket_by_tag_01246,
    is_valid_sku_01246,
    price_with_tax_01246,
)


def test_price_with_tax_01246():
    assert price_with_tax_01246(1000, 500) == 1050


def test_price_with_tax_negative_01246():
    with pytest.raises(ValueError):
        price_with_tax_01246(1000, -1)


def test_is_valid_sku_01246():
    assert is_valid_sku_01246("abc123")
    assert not is_valid_sku_01246("")


def test_bucket_by_tag_01246():
    p = Product_01246("s1", 100, ["a"])
    assert bucket_by_tag_01246([p]) == {"a": ["s1"]}
