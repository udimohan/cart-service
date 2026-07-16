"""Tests for catalog_00570."""

import pytest

from cartservice.generated.catalog_00570 import (
    Product_00570,
    bucket_by_tag_00570,
    is_valid_sku_00570,
    price_with_tax_00570,
)


def test_price_with_tax_00570():
    assert price_with_tax_00570(1000, 500) == 1050


def test_price_with_tax_negative_00570():
    with pytest.raises(ValueError):
        price_with_tax_00570(1000, -1)


def test_is_valid_sku_00570():
    assert is_valid_sku_00570("abc123")
    assert not is_valid_sku_00570("")


def test_bucket_by_tag_00570():
    p = Product_00570("s1", 100, ["a"])
    assert bucket_by_tag_00570([p]) == {"a": ["s1"]}
