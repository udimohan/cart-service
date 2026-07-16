"""Tests for catalog_00996."""

import pytest

from cartservice.generated.catalog_00996 import (
    Product_00996,
    bucket_by_tag_00996,
    is_valid_sku_00996,
    price_with_tax_00996,
)


def test_price_with_tax_00996():
    assert price_with_tax_00996(1000, 500) == 1050


def test_price_with_tax_negative_00996():
    with pytest.raises(ValueError):
        price_with_tax_00996(1000, -1)


def test_is_valid_sku_00996():
    assert is_valid_sku_00996("abc123")
    assert not is_valid_sku_00996("")


def test_bucket_by_tag_00996():
    p = Product_00996("s1", 100, ["a"])
    assert bucket_by_tag_00996([p]) == {"a": ["s1"]}
