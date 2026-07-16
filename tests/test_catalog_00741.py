"""Tests for catalog_00741."""

import pytest

from cartservice.generated.catalog_00741 import (
    Product_00741,
    bucket_by_tag_00741,
    is_valid_sku_00741,
    price_with_tax_00741,
)


def test_price_with_tax_00741():
    assert price_with_tax_00741(1000, 500) == 1050


def test_price_with_tax_negative_00741():
    with pytest.raises(ValueError):
        price_with_tax_00741(1000, -1)


def test_is_valid_sku_00741():
    assert is_valid_sku_00741("abc123")
    assert not is_valid_sku_00741("")


def test_bucket_by_tag_00741():
    p = Product_00741("s1", 100, ["a"])
    assert bucket_by_tag_00741([p]) == {"a": ["s1"]}
