"""Tests for catalog_01051."""

import pytest

from cartservice.generated.catalog_01051 import (
    Product_01051,
    bucket_by_tag_01051,
    is_valid_sku_01051,
    price_with_tax_01051,
)


def test_price_with_tax_01051():
    assert price_with_tax_01051(1000, 500) == 1050


def test_price_with_tax_negative_01051():
    with pytest.raises(ValueError):
        price_with_tax_01051(1000, -1)


def test_is_valid_sku_01051():
    assert is_valid_sku_01051("abc123")
    assert not is_valid_sku_01051("")


def test_bucket_by_tag_01051():
    p = Product_01051("s1", 100, ["a"])
    assert bucket_by_tag_01051([p]) == {"a": ["s1"]}
