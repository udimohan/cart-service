"""Tests for catalog_01494."""

import pytest

from cartservice.generated.catalog_01494 import (
    Product_01494,
    bucket_by_tag_01494,
    is_valid_sku_01494,
    price_with_tax_01494,
)


def test_price_with_tax_01494():
    assert price_with_tax_01494(1000, 500) == 1050


def test_price_with_tax_negative_01494():
    with pytest.raises(ValueError):
        price_with_tax_01494(1000, -1)


def test_is_valid_sku_01494():
    assert is_valid_sku_01494("abc123")
    assert not is_valid_sku_01494("")


def test_bucket_by_tag_01494():
    p = Product_01494("s1", 100, ["a"])
    assert bucket_by_tag_01494([p]) == {"a": ["s1"]}
