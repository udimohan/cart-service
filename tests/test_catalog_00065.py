"""Tests for catalog_00065."""

import pytest

from cartservice.generated.catalog_00065 import (
    Product_00065,
    bucket_by_tag_00065,
    is_valid_sku_00065,
    price_with_tax_00065,
)


def test_price_with_tax_00065():
    assert price_with_tax_00065(1000, 500) == 1050


def test_price_with_tax_negative_00065():
    with pytest.raises(ValueError):
        price_with_tax_00065(1000, -1)


def test_is_valid_sku_00065():
    assert is_valid_sku_00065("abc123")
    assert not is_valid_sku_00065("")


def test_bucket_by_tag_00065():
    p = Product_00065("s1", 100, ["a"])
    assert bucket_by_tag_00065([p]) == {"a": ["s1"]}
