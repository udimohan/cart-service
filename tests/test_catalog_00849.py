"""Tests for catalog_00849."""

import pytest

from cartservice.generated.catalog_00849 import (
    Product_00849,
    bucket_by_tag_00849,
    is_valid_sku_00849,
    price_with_tax_00849,
)


def test_price_with_tax_00849():
    assert price_with_tax_00849(1000, 500) == 1050


def test_price_with_tax_negative_00849():
    with pytest.raises(ValueError):
        price_with_tax_00849(1000, -1)


def test_is_valid_sku_00849():
    assert is_valid_sku_00849("abc123")
    assert not is_valid_sku_00849("")


def test_bucket_by_tag_00849():
    p = Product_00849("s1", 100, ["a"])
    assert bucket_by_tag_00849([p]) == {"a": ["s1"]}
