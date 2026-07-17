"""Tests for catalog_00592."""

import pytest

from cartservice.generated.catalog_00592 import (
    Product_00592,
    bucket_by_tag_00592,
    is_valid_sku_00592,
    price_with_tax_00592,
)


def test_price_with_tax_00592():
    assert price_with_tax_00592(1000, 500) == 1050


def test_price_with_tax_negative_00592():
    with pytest.raises(ValueError):
        price_with_tax_00592(1000, -1)


def test_is_valid_sku_00592():
    assert is_valid_sku_00592("abc123")
    assert not is_valid_sku_00592("")


def test_bucket_by_tag_00592():
    p = Product_00592("s1", 100, ["a"])
    assert bucket_by_tag_00592([p]) == {"a": ["s1"]}
