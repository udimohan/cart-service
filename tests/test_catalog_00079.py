"""Tests for catalog_00079."""

import pytest

from cartservice.generated.catalog_00079 import (
    Product_00079,
    bucket_by_tag_00079,
    is_valid_sku_00079,
    price_with_tax_00079,
)


def test_price_with_tax_00079():
    assert price_with_tax_00079(1000, 500) == 1050


def test_price_with_tax_negative_00079():
    with pytest.raises(ValueError):
        price_with_tax_00079(1000, -1)


def test_is_valid_sku_00079():
    assert is_valid_sku_00079("abc123")
    assert not is_valid_sku_00079("")


def test_bucket_by_tag_00079():
    p = Product_00079("s1", 100, ["a"])
    assert bucket_by_tag_00079([p]) == {"a": ["s1"]}
