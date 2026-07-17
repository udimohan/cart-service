"""Tests for catalog_00889."""

import pytest

from cartservice.generated.catalog_00889 import (
    Product_00889,
    bucket_by_tag_00889,
    is_valid_sku_00889,
    price_with_tax_00889,
)


def test_price_with_tax_00889():
    assert price_with_tax_00889(1000, 500) == 1050


def test_price_with_tax_negative_00889():
    with pytest.raises(ValueError):
        price_with_tax_00889(1000, -1)


def test_is_valid_sku_00889():
    assert is_valid_sku_00889("abc123")
    assert not is_valid_sku_00889("")


def test_bucket_by_tag_00889():
    p = Product_00889("s1", 100, ["a"])
    assert bucket_by_tag_00889([p]) == {"a": ["s1"]}
