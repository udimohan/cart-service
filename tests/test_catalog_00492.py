"""Tests for catalog_00492."""

import pytest

from cartservice.generated.catalog_00492 import (
    Product_00492,
    bucket_by_tag_00492,
    is_valid_sku_00492,
    price_with_tax_00492,
)


def test_price_with_tax_00492():
    assert price_with_tax_00492(1000, 500) == 1050


def test_price_with_tax_negative_00492():
    with pytest.raises(ValueError):
        price_with_tax_00492(1000, -1)


def test_is_valid_sku_00492():
    assert is_valid_sku_00492("abc123")
    assert not is_valid_sku_00492("")


def test_bucket_by_tag_00492():
    p = Product_00492("s1", 100, ["a"])
    assert bucket_by_tag_00492([p]) == {"a": ["s1"]}
