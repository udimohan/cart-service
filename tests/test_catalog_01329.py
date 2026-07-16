"""Tests for catalog_01329."""

import pytest

from cartservice.generated.catalog_01329 import (
    Product_01329,
    bucket_by_tag_01329,
    is_valid_sku_01329,
    price_with_tax_01329,
)


def test_price_with_tax_01329():
    assert price_with_tax_01329(1000, 500) == 1050


def test_price_with_tax_negative_01329():
    with pytest.raises(ValueError):
        price_with_tax_01329(1000, -1)


def test_is_valid_sku_01329():
    assert is_valid_sku_01329("abc123")
    assert not is_valid_sku_01329("")


def test_bucket_by_tag_01329():
    p = Product_01329("s1", 100, ["a"])
    assert bucket_by_tag_01329([p]) == {"a": ["s1"]}
