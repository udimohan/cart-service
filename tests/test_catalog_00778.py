"""Tests for catalog_00778."""

import pytest

from cartservice.generated.catalog_00778 import (
    Product_00778,
    bucket_by_tag_00778,
    is_valid_sku_00778,
    price_with_tax_00778,
)


def test_price_with_tax_00778():
    assert price_with_tax_00778(1000, 500) == 1050


def test_price_with_tax_negative_00778():
    with pytest.raises(ValueError):
        price_with_tax_00778(1000, -1)


def test_is_valid_sku_00778():
    assert is_valid_sku_00778("abc123")
    assert not is_valid_sku_00778("")


def test_bucket_by_tag_00778():
    p = Product_00778("s1", 100, ["a"])
    assert bucket_by_tag_00778([p]) == {"a": ["s1"]}
