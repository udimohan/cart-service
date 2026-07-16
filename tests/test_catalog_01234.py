"""Tests for catalog_01234."""

import pytest

from cartservice.generated.catalog_01234 import (
    Product_01234,
    bucket_by_tag_01234,
    is_valid_sku_01234,
    price_with_tax_01234,
)


def test_price_with_tax_01234():
    assert price_with_tax_01234(1000, 500) == 1050


def test_price_with_tax_negative_01234():
    with pytest.raises(ValueError):
        price_with_tax_01234(1000, -1)


def test_is_valid_sku_01234():
    assert is_valid_sku_01234("abc123")
    assert not is_valid_sku_01234("")


def test_bucket_by_tag_01234():
    p = Product_01234("s1", 100, ["a"])
    assert bucket_by_tag_01234([p]) == {"a": ["s1"]}
