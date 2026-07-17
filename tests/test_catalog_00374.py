"""Tests for catalog_00374."""

import pytest

from cartservice.generated.catalog_00374 import (
    Product_00374,
    bucket_by_tag_00374,
    is_valid_sku_00374,
    price_with_tax_00374,
)


def test_price_with_tax_00374():
    assert price_with_tax_00374(1000, 500) == 1050


def test_price_with_tax_negative_00374():
    with pytest.raises(ValueError):
        price_with_tax_00374(1000, -1)


def test_is_valid_sku_00374():
    assert is_valid_sku_00374("abc123")
    assert not is_valid_sku_00374("")


def test_bucket_by_tag_00374():
    p = Product_00374("s1", 100, ["a"])
    assert bucket_by_tag_00374([p]) == {"a": ["s1"]}
