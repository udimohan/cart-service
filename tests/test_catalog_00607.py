"""Tests for catalog_00607."""

import pytest

from cartservice.generated.catalog_00607 import (
    Product_00607,
    bucket_by_tag_00607,
    is_valid_sku_00607,
    price_with_tax_00607,
)


def test_price_with_tax_00607():
    assert price_with_tax_00607(1000, 500) == 1050


def test_price_with_tax_negative_00607():
    with pytest.raises(ValueError):
        price_with_tax_00607(1000, -1)


def test_is_valid_sku_00607():
    assert is_valid_sku_00607("abc123")
    assert not is_valid_sku_00607("")


def test_bucket_by_tag_00607():
    p = Product_00607("s1", 100, ["a"])
    assert bucket_by_tag_00607([p]) == {"a": ["s1"]}
