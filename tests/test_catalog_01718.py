"""Tests for catalog_01718."""

import pytest

from cartservice.generated.catalog_01718 import (
    Product_01718,
    bucket_by_tag_01718,
    is_valid_sku_01718,
    price_with_tax_01718,
)


def test_price_with_tax_01718():
    assert price_with_tax_01718(1000, 500) == 1050


def test_price_with_tax_negative_01718():
    with pytest.raises(ValueError):
        price_with_tax_01718(1000, -1)


def test_is_valid_sku_01718():
    assert is_valid_sku_01718("abc123")
    assert not is_valid_sku_01718("")


def test_bucket_by_tag_01718():
    p = Product_01718("s1", 100, ["a"])
    assert bucket_by_tag_01718([p]) == {"a": ["s1"]}
