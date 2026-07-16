"""Tests for catalog_01026."""

import pytest

from cartservice.generated.catalog_01026 import (
    Product_01026,
    bucket_by_tag_01026,
    is_valid_sku_01026,
    price_with_tax_01026,
)


def test_price_with_tax_01026():
    assert price_with_tax_01026(1000, 500) == 1050


def test_price_with_tax_negative_01026():
    with pytest.raises(ValueError):
        price_with_tax_01026(1000, -1)


def test_is_valid_sku_01026():
    assert is_valid_sku_01026("abc123")
    assert not is_valid_sku_01026("")


def test_bucket_by_tag_01026():
    p = Product_01026("s1", 100, ["a"])
    assert bucket_by_tag_01026([p]) == {"a": ["s1"]}
