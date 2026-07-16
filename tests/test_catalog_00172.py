"""Tests for catalog_00172."""

import pytest

from cartservice.generated.catalog_00172 import (
    Product_00172,
    bucket_by_tag_00172,
    is_valid_sku_00172,
    price_with_tax_00172,
)


def test_price_with_tax_00172():
    assert price_with_tax_00172(1000, 500) == 1050


def test_price_with_tax_negative_00172():
    with pytest.raises(ValueError):
        price_with_tax_00172(1000, -1)


def test_is_valid_sku_00172():
    assert is_valid_sku_00172("abc123")
    assert not is_valid_sku_00172("")


def test_bucket_by_tag_00172():
    p = Product_00172("s1", 100, ["a"])
    assert bucket_by_tag_00172([p]) == {"a": ["s1"]}
