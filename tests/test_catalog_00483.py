"""Tests for catalog_00483."""

import pytest

from cartservice.generated.catalog_00483 import (
    Product_00483,
    bucket_by_tag_00483,
    is_valid_sku_00483,
    price_with_tax_00483,
)


def test_price_with_tax_00483():
    assert price_with_tax_00483(1000, 500) == 1050


def test_price_with_tax_negative_00483():
    with pytest.raises(ValueError):
        price_with_tax_00483(1000, -1)


def test_is_valid_sku_00483():
    assert is_valid_sku_00483("abc123")
    assert not is_valid_sku_00483("")


def test_bucket_by_tag_00483():
    p = Product_00483("s1", 100, ["a"])
    assert bucket_by_tag_00483([p]) == {"a": ["s1"]}
