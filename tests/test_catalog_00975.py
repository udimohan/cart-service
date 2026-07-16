"""Tests for catalog_00975."""

import pytest

from cartservice.generated.catalog_00975 import (
    Product_00975,
    bucket_by_tag_00975,
    is_valid_sku_00975,
    price_with_tax_00975,
)


def test_price_with_tax_00975():
    assert price_with_tax_00975(1000, 500) == 1050


def test_price_with_tax_negative_00975():
    with pytest.raises(ValueError):
        price_with_tax_00975(1000, -1)


def test_is_valid_sku_00975():
    assert is_valid_sku_00975("abc123")
    assert not is_valid_sku_00975("")


def test_bucket_by_tag_00975():
    p = Product_00975("s1", 100, ["a"])
    assert bucket_by_tag_00975([p]) == {"a": ["s1"]}
