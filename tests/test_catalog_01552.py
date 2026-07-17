"""Tests for catalog_01552."""

import pytest

from cartservice.generated.catalog_01552 import (
    Product_01552,
    bucket_by_tag_01552,
    is_valid_sku_01552,
    price_with_tax_01552,
)


def test_price_with_tax_01552():
    assert price_with_tax_01552(1000, 500) == 1050


def test_price_with_tax_negative_01552():
    with pytest.raises(ValueError):
        price_with_tax_01552(1000, -1)


def test_is_valid_sku_01552():
    assert is_valid_sku_01552("abc123")
    assert not is_valid_sku_01552("")


def test_bucket_by_tag_01552():
    p = Product_01552("s1", 100, ["a"])
    assert bucket_by_tag_01552([p]) == {"a": ["s1"]}
