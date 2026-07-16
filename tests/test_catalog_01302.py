"""Tests for catalog_01302."""

import pytest

from cartservice.generated.catalog_01302 import (
    Product_01302,
    bucket_by_tag_01302,
    is_valid_sku_01302,
    price_with_tax_01302,
)


def test_price_with_tax_01302():
    assert price_with_tax_01302(1000, 500) == 1050


def test_price_with_tax_negative_01302():
    with pytest.raises(ValueError):
        price_with_tax_01302(1000, -1)


def test_is_valid_sku_01302():
    assert is_valid_sku_01302("abc123")
    assert not is_valid_sku_01302("")


def test_bucket_by_tag_01302():
    p = Product_01302("s1", 100, ["a"])
    assert bucket_by_tag_01302([p]) == {"a": ["s1"]}
