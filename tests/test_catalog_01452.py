"""Tests for catalog_01452."""

import pytest

from cartservice.generated.catalog_01452 import (
    Product_01452,
    bucket_by_tag_01452,
    is_valid_sku_01452,
    price_with_tax_01452,
)


def test_price_with_tax_01452():
    assert price_with_tax_01452(1000, 500) == 1050


def test_price_with_tax_negative_01452():
    with pytest.raises(ValueError):
        price_with_tax_01452(1000, -1)


def test_is_valid_sku_01452():
    assert is_valid_sku_01452("abc123")
    assert not is_valid_sku_01452("")


def test_bucket_by_tag_01452():
    p = Product_01452("s1", 100, ["a"])
    assert bucket_by_tag_01452([p]) == {"a": ["s1"]}
