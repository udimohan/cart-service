"""Tests for catalog_01195."""

import pytest

from cartservice.generated.catalog_01195 import (
    Product_01195,
    bucket_by_tag_01195,
    is_valid_sku_01195,
    price_with_tax_01195,
)


def test_price_with_tax_01195():
    assert price_with_tax_01195(1000, 500) == 1050


def test_price_with_tax_negative_01195():
    with pytest.raises(ValueError):
        price_with_tax_01195(1000, -1)


def test_is_valid_sku_01195():
    assert is_valid_sku_01195("abc123")
    assert not is_valid_sku_01195("")


def test_bucket_by_tag_01195():
    p = Product_01195("s1", 100, ["a"])
    assert bucket_by_tag_01195([p]) == {"a": ["s1"]}
