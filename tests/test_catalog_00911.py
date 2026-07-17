"""Tests for catalog_00911."""

import pytest

from cartservice.generated.catalog_00911 import (
    Product_00911,
    bucket_by_tag_00911,
    is_valid_sku_00911,
    price_with_tax_00911,
)


def test_price_with_tax_00911():
    assert price_with_tax_00911(1000, 500) == 1050


def test_price_with_tax_negative_00911():
    with pytest.raises(ValueError):
        price_with_tax_00911(1000, -1)


def test_is_valid_sku_00911():
    assert is_valid_sku_00911("abc123")
    assert not is_valid_sku_00911("")


def test_bucket_by_tag_00911():
    p = Product_00911("s1", 100, ["a"])
    assert bucket_by_tag_00911([p]) == {"a": ["s1"]}
