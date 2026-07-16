"""Tests for catalog_01259."""

import pytest

from cartservice.generated.catalog_01259 import (
    Product_01259,
    bucket_by_tag_01259,
    is_valid_sku_01259,
    price_with_tax_01259,
)


def test_price_with_tax_01259():
    assert price_with_tax_01259(1000, 500) == 1050


def test_price_with_tax_negative_01259():
    with pytest.raises(ValueError):
        price_with_tax_01259(1000, -1)


def test_is_valid_sku_01259():
    assert is_valid_sku_01259("abc123")
    assert not is_valid_sku_01259("")


def test_bucket_by_tag_01259():
    p = Product_01259("s1", 100, ["a"])
    assert bucket_by_tag_01259([p]) == {"a": ["s1"]}
