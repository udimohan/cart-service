"""Tests for catalog_01590."""

import pytest

from cartservice.generated.catalog_01590 import (
    Product_01590,
    bucket_by_tag_01590,
    is_valid_sku_01590,
    price_with_tax_01590,
)


def test_price_with_tax_01590():
    assert price_with_tax_01590(1000, 500) == 1050


def test_price_with_tax_negative_01590():
    with pytest.raises(ValueError):
        price_with_tax_01590(1000, -1)


def test_is_valid_sku_01590():
    assert is_valid_sku_01590("abc123")
    assert not is_valid_sku_01590("")


def test_bucket_by_tag_01590():
    p = Product_01590("s1", 100, ["a"])
    assert bucket_by_tag_01590([p]) == {"a": ["s1"]}
