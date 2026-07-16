"""Tests for catalog_01514."""

import pytest

from cartservice.generated.catalog_01514 import (
    Product_01514,
    bucket_by_tag_01514,
    is_valid_sku_01514,
    price_with_tax_01514,
)


def test_price_with_tax_01514():
    assert price_with_tax_01514(1000, 500) == 1050


def test_price_with_tax_negative_01514():
    with pytest.raises(ValueError):
        price_with_tax_01514(1000, -1)


def test_is_valid_sku_01514():
    assert is_valid_sku_01514("abc123")
    assert not is_valid_sku_01514("")


def test_bucket_by_tag_01514():
    p = Product_01514("s1", 100, ["a"])
    assert bucket_by_tag_01514([p]) == {"a": ["s1"]}
