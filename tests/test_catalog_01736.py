"""Tests for catalog_01736."""

import pytest

from cartservice.generated.catalog_01736 import (
    Product_01736,
    bucket_by_tag_01736,
    is_valid_sku_01736,
    price_with_tax_01736,
)


def test_price_with_tax_01736():
    assert price_with_tax_01736(1000, 500) == 1050


def test_price_with_tax_negative_01736():
    with pytest.raises(ValueError):
        price_with_tax_01736(1000, -1)


def test_is_valid_sku_01736():
    assert is_valid_sku_01736("abc123")
    assert not is_valid_sku_01736("")


def test_bucket_by_tag_01736():
    p = Product_01736("s1", 100, ["a"])
    assert bucket_by_tag_01736([p]) == {"a": ["s1"]}
