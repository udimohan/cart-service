"""Tests for catalog_01079."""

import pytest

from cartservice.generated.catalog_01079 import (
    Product_01079,
    bucket_by_tag_01079,
    is_valid_sku_01079,
    price_with_tax_01079,
)


def test_price_with_tax_01079():
    assert price_with_tax_01079(1000, 500) == 1050


def test_price_with_tax_negative_01079():
    with pytest.raises(ValueError):
        price_with_tax_01079(1000, -1)


def test_is_valid_sku_01079():
    assert is_valid_sku_01079("abc123")
    assert not is_valid_sku_01079("")


def test_bucket_by_tag_01079():
    p = Product_01079("s1", 100, ["a"])
    assert bucket_by_tag_01079([p]) == {"a": ["s1"]}
