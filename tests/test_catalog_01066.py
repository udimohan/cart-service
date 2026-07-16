"""Tests for catalog_01066."""

import pytest

from cartservice.generated.catalog_01066 import (
    Product_01066,
    bucket_by_tag_01066,
    is_valid_sku_01066,
    price_with_tax_01066,
)


def test_price_with_tax_01066():
    assert price_with_tax_01066(1000, 500) == 1050


def test_price_with_tax_negative_01066():
    with pytest.raises(ValueError):
        price_with_tax_01066(1000, -1)


def test_is_valid_sku_01066():
    assert is_valid_sku_01066("abc123")
    assert not is_valid_sku_01066("")


def test_bucket_by_tag_01066():
    p = Product_01066("s1", 100, ["a"])
    assert bucket_by_tag_01066([p]) == {"a": ["s1"]}
