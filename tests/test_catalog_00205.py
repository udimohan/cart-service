"""Tests for catalog_00205."""

import pytest

from cartservice.generated.catalog_00205 import (
    Product_00205,
    bucket_by_tag_00205,
    is_valid_sku_00205,
    price_with_tax_00205,
)


def test_price_with_tax_00205():
    assert price_with_tax_00205(1000, 500) == 1050


def test_price_with_tax_negative_00205():
    with pytest.raises(ValueError):
        price_with_tax_00205(1000, -1)


def test_is_valid_sku_00205():
    assert is_valid_sku_00205("abc123")
    assert not is_valid_sku_00205("")


def test_bucket_by_tag_00205():
    p = Product_00205("s1", 100, ["a"])
    assert bucket_by_tag_00205([p]) == {"a": ["s1"]}
