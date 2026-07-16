"""Tests for catalog_00964."""

import pytest

from cartservice.generated.catalog_00964 import (
    Product_00964,
    bucket_by_tag_00964,
    is_valid_sku_00964,
    price_with_tax_00964,
)


def test_price_with_tax_00964():
    assert price_with_tax_00964(1000, 500) == 1050


def test_price_with_tax_negative_00964():
    with pytest.raises(ValueError):
        price_with_tax_00964(1000, -1)


def test_is_valid_sku_00964():
    assert is_valid_sku_00964("abc123")
    assert not is_valid_sku_00964("")


def test_bucket_by_tag_00964():
    p = Product_00964("s1", 100, ["a"])
    assert bucket_by_tag_00964([p]) == {"a": ["s1"]}
