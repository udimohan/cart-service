"""Tests for catalog_01170."""

import pytest

from cartservice.generated.catalog_01170 import (
    Product_01170,
    bucket_by_tag_01170,
    is_valid_sku_01170,
    price_with_tax_01170,
)


def test_price_with_tax_01170():
    assert price_with_tax_01170(1000, 500) == 1050


def test_price_with_tax_negative_01170():
    with pytest.raises(ValueError):
        price_with_tax_01170(1000, -1)


def test_is_valid_sku_01170():
    assert is_valid_sku_01170("abc123")
    assert not is_valid_sku_01170("")


def test_bucket_by_tag_01170():
    p = Product_01170("s1", 100, ["a"])
    assert bucket_by_tag_01170([p]) == {"a": ["s1"]}
