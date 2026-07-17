"""Tests for catalog_00356."""

import pytest

from cartservice.generated.catalog_00356 import (
    Product_00356,
    bucket_by_tag_00356,
    is_valid_sku_00356,
    price_with_tax_00356,
)


def test_price_with_tax_00356():
    assert price_with_tax_00356(1000, 500) == 1050


def test_price_with_tax_negative_00356():
    with pytest.raises(ValueError):
        price_with_tax_00356(1000, -1)


def test_is_valid_sku_00356():
    assert is_valid_sku_00356("abc123")
    assert not is_valid_sku_00356("")


def test_bucket_by_tag_00356():
    p = Product_00356("s1", 100, ["a"])
    assert bucket_by_tag_00356([p]) == {"a": ["s1"]}
