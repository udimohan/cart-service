"""Tests for catalog_01497."""

import pytest

from cartservice.generated.catalog_01497 import (
    Product_01497,
    bucket_by_tag_01497,
    is_valid_sku_01497,
    price_with_tax_01497,
)


def test_price_with_tax_01497():
    assert price_with_tax_01497(1000, 500) == 1050


def test_price_with_tax_negative_01497():
    with pytest.raises(ValueError):
        price_with_tax_01497(1000, -1)


def test_is_valid_sku_01497():
    assert is_valid_sku_01497("abc123")
    assert not is_valid_sku_01497("")


def test_bucket_by_tag_01497():
    p = Product_01497("s1", 100, ["a"])
    assert bucket_by_tag_01497([p]) == {"a": ["s1"]}
