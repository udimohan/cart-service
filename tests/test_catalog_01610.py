"""Tests for catalog_01610."""

import pytest

from cartservice.generated.catalog_01610 import (
    Product_01610,
    bucket_by_tag_01610,
    is_valid_sku_01610,
    price_with_tax_01610,
)


def test_price_with_tax_01610():
    assert price_with_tax_01610(1000, 500) == 1050


def test_price_with_tax_negative_01610():
    with pytest.raises(ValueError):
        price_with_tax_01610(1000, -1)


def test_is_valid_sku_01610():
    assert is_valid_sku_01610("abc123")
    assert not is_valid_sku_01610("")


def test_bucket_by_tag_01610():
    p = Product_01610("s1", 100, ["a"])
    assert bucket_by_tag_01610([p]) == {"a": ["s1"]}
