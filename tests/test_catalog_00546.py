"""Tests for catalog_00546."""

import pytest

from cartservice.generated.catalog_00546 import (
    Product_00546,
    bucket_by_tag_00546,
    is_valid_sku_00546,
    price_with_tax_00546,
)


def test_price_with_tax_00546():
    assert price_with_tax_00546(1000, 500) == 1050


def test_price_with_tax_negative_00546():
    with pytest.raises(ValueError):
        price_with_tax_00546(1000, -1)


def test_is_valid_sku_00546():
    assert is_valid_sku_00546("abc123")
    assert not is_valid_sku_00546("")


def test_bucket_by_tag_00546():
    p = Product_00546("s1", 100, ["a"])
    assert bucket_by_tag_00546([p]) == {"a": ["s1"]}
