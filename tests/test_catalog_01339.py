"""Tests for catalog_01339."""

import pytest

from cartservice.generated.catalog_01339 import (
    Product_01339,
    bucket_by_tag_01339,
    is_valid_sku_01339,
    price_with_tax_01339,
)


def test_price_with_tax_01339():
    assert price_with_tax_01339(1000, 500) == 1050


def test_price_with_tax_negative_01339():
    with pytest.raises(ValueError):
        price_with_tax_01339(1000, -1)


def test_is_valid_sku_01339():
    assert is_valid_sku_01339("abc123")
    assert not is_valid_sku_01339("")


def test_bucket_by_tag_01339():
    p = Product_01339("s1", 100, ["a"])
    assert bucket_by_tag_01339([p]) == {"a": ["s1"]}
