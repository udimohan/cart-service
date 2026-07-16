"""Tests for catalog_00867."""

import pytest

from cartservice.generated.catalog_00867 import (
    Product_00867,
    bucket_by_tag_00867,
    is_valid_sku_00867,
    price_with_tax_00867,
)


def test_price_with_tax_00867():
    assert price_with_tax_00867(1000, 500) == 1050


def test_price_with_tax_negative_00867():
    with pytest.raises(ValueError):
        price_with_tax_00867(1000, -1)


def test_is_valid_sku_00867():
    assert is_valid_sku_00867("abc123")
    assert not is_valid_sku_00867("")


def test_bucket_by_tag_00867():
    p = Product_00867("s1", 100, ["a"])
    assert bucket_by_tag_00867([p]) == {"a": ["s1"]}
