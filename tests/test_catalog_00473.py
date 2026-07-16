"""Tests for catalog_00473."""

import pytest

from cartservice.generated.catalog_00473 import (
    Product_00473,
    bucket_by_tag_00473,
    is_valid_sku_00473,
    price_with_tax_00473,
)


def test_price_with_tax_00473():
    assert price_with_tax_00473(1000, 500) == 1050


def test_price_with_tax_negative_00473():
    with pytest.raises(ValueError):
        price_with_tax_00473(1000, -1)


def test_is_valid_sku_00473():
    assert is_valid_sku_00473("abc123")
    assert not is_valid_sku_00473("")


def test_bucket_by_tag_00473():
    p = Product_00473("s1", 100, ["a"])
    assert bucket_by_tag_00473([p]) == {"a": ["s1"]}
