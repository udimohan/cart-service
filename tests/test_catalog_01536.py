"""Tests for catalog_01536."""

import pytest

from cartservice.generated.catalog_01536 import (
    Product_01536,
    bucket_by_tag_01536,
    is_valid_sku_01536,
    price_with_tax_01536,
)


def test_price_with_tax_01536():
    assert price_with_tax_01536(1000, 500) == 1050


def test_price_with_tax_negative_01536():
    with pytest.raises(ValueError):
        price_with_tax_01536(1000, -1)


def test_is_valid_sku_01536():
    assert is_valid_sku_01536("abc123")
    assert not is_valid_sku_01536("")


def test_bucket_by_tag_01536():
    p = Product_01536("s1", 100, ["a"])
    assert bucket_by_tag_01536([p]) == {"a": ["s1"]}
