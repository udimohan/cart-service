"""Tests for catalog_00268."""

import pytest

from cartservice.generated.catalog_00268 import (
    Product_00268,
    bucket_by_tag_00268,
    is_valid_sku_00268,
    price_with_tax_00268,
)


def test_price_with_tax_00268():
    assert price_with_tax_00268(1000, 500) == 1050


def test_price_with_tax_negative_00268():
    with pytest.raises(ValueError):
        price_with_tax_00268(1000, -1)


def test_is_valid_sku_00268():
    assert is_valid_sku_00268("abc123")
    assert not is_valid_sku_00268("")


def test_bucket_by_tag_00268():
    p = Product_00268("s1", 100, ["a"])
    assert bucket_by_tag_00268([p]) == {"a": ["s1"]}
