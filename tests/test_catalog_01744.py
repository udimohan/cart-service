"""Tests for catalog_01744."""

import pytest

from cartservice.generated.catalog_01744 import (
    Product_01744,
    bucket_by_tag_01744,
    is_valid_sku_01744,
    price_with_tax_01744,
)


def test_price_with_tax_01744():
    assert price_with_tax_01744(1000, 500) == 1050


def test_price_with_tax_negative_01744():
    with pytest.raises(ValueError):
        price_with_tax_01744(1000, -1)


def test_is_valid_sku_01744():
    assert is_valid_sku_01744("abc123")
    assert not is_valid_sku_01744("")


def test_bucket_by_tag_01744():
    p = Product_01744("s1", 100, ["a"])
    assert bucket_by_tag_01744([p]) == {"a": ["s1"]}
