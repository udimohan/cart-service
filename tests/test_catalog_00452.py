"""Tests for catalog_00452."""

import pytest

from cartservice.generated.catalog_00452 import (
    Product_00452,
    bucket_by_tag_00452,
    is_valid_sku_00452,
    price_with_tax_00452,
)


def test_price_with_tax_00452():
    assert price_with_tax_00452(1000, 500) == 1050


def test_price_with_tax_negative_00452():
    with pytest.raises(ValueError):
        price_with_tax_00452(1000, -1)


def test_is_valid_sku_00452():
    assert is_valid_sku_00452("abc123")
    assert not is_valid_sku_00452("")


def test_bucket_by_tag_00452():
    p = Product_00452("s1", 100, ["a"])
    assert bucket_by_tag_00452([p]) == {"a": ["s1"]}
