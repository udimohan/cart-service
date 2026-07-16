"""Tests for catalog_00471."""

import pytest

from cartservice.generated.catalog_00471 import (
    Product_00471,
    bucket_by_tag_00471,
    is_valid_sku_00471,
    price_with_tax_00471,
)


def test_price_with_tax_00471():
    assert price_with_tax_00471(1000, 500) == 1050


def test_price_with_tax_negative_00471():
    with pytest.raises(ValueError):
        price_with_tax_00471(1000, -1)


def test_is_valid_sku_00471():
    assert is_valid_sku_00471("abc123")
    assert not is_valid_sku_00471("")


def test_bucket_by_tag_00471():
    p = Product_00471("s1", 100, ["a"])
    assert bucket_by_tag_00471([p]) == {"a": ["s1"]}
