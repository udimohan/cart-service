"""Tests for catalog_01014."""

import pytest

from cartservice.generated.catalog_01014 import (
    Product_01014,
    bucket_by_tag_01014,
    is_valid_sku_01014,
    price_with_tax_01014,
)


def test_price_with_tax_01014():
    assert price_with_tax_01014(1000, 500) == 1050


def test_price_with_tax_negative_01014():
    with pytest.raises(ValueError):
        price_with_tax_01014(1000, -1)


def test_is_valid_sku_01014():
    assert is_valid_sku_01014("abc123")
    assert not is_valid_sku_01014("")


def test_bucket_by_tag_01014():
    p = Product_01014("s1", 100, ["a"])
    assert bucket_by_tag_01014([p]) == {"a": ["s1"]}
