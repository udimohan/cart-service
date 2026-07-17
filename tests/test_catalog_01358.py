"""Tests for catalog_01358."""

import pytest

from cartservice.generated.catalog_01358 import (
    Product_01358,
    bucket_by_tag_01358,
    is_valid_sku_01358,
    price_with_tax_01358,
)


def test_price_with_tax_01358():
    assert price_with_tax_01358(1000, 500) == 1050


def test_price_with_tax_negative_01358():
    with pytest.raises(ValueError):
        price_with_tax_01358(1000, -1)


def test_is_valid_sku_01358():
    assert is_valid_sku_01358("abc123")
    assert not is_valid_sku_01358("")


def test_bucket_by_tag_01358():
    p = Product_01358("s1", 100, ["a"])
    assert bucket_by_tag_01358([p]) == {"a": ["s1"]}
