"""Tests for catalog_01198."""

import pytest

from cartservice.generated.catalog_01198 import (
    Product_01198,
    bucket_by_tag_01198,
    is_valid_sku_01198,
    price_with_tax_01198,
)


def test_price_with_tax_01198():
    assert price_with_tax_01198(1000, 500) == 1050


def test_price_with_tax_negative_01198():
    with pytest.raises(ValueError):
        price_with_tax_01198(1000, -1)


def test_is_valid_sku_01198():
    assert is_valid_sku_01198("abc123")
    assert not is_valid_sku_01198("")


def test_bucket_by_tag_01198():
    p = Product_01198("s1", 100, ["a"])
    assert bucket_by_tag_01198([p]) == {"a": ["s1"]}
