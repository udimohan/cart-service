"""Tests for catalog_01347."""

import pytest

from cartservice.generated.catalog_01347 import (
    Product_01347,
    bucket_by_tag_01347,
    is_valid_sku_01347,
    price_with_tax_01347,
)


def test_price_with_tax_01347():
    assert price_with_tax_01347(1000, 500) == 1050


def test_price_with_tax_negative_01347():
    with pytest.raises(ValueError):
        price_with_tax_01347(1000, -1)


def test_is_valid_sku_01347():
    assert is_valid_sku_01347("abc123")
    assert not is_valid_sku_01347("")


def test_bucket_by_tag_01347():
    p = Product_01347("s1", 100, ["a"])
    assert bucket_by_tag_01347([p]) == {"a": ["s1"]}
