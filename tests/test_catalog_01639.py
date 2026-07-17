"""Tests for catalog_01639."""

import pytest

from cartservice.generated.catalog_01639 import (
    Product_01639,
    bucket_by_tag_01639,
    is_valid_sku_01639,
    price_with_tax_01639,
)


def test_price_with_tax_01639():
    assert price_with_tax_01639(1000, 500) == 1050


def test_price_with_tax_negative_01639():
    with pytest.raises(ValueError):
        price_with_tax_01639(1000, -1)


def test_is_valid_sku_01639():
    assert is_valid_sku_01639("abc123")
    assert not is_valid_sku_01639("")


def test_bucket_by_tag_01639():
    p = Product_01639("s1", 100, ["a"])
    assert bucket_by_tag_01639([p]) == {"a": ["s1"]}
