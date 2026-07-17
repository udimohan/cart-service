"""Tests for catalog_00017."""

import pytest

from cartservice.generated.catalog_00017 import (
    Product_00017,
    bucket_by_tag_00017,
    is_valid_sku_00017,
    price_with_tax_00017,
)


def test_price_with_tax_00017():
    assert price_with_tax_00017(1000, 500) == 1050


def test_price_with_tax_negative_00017():
    with pytest.raises(ValueError):
        price_with_tax_00017(1000, -1)


def test_is_valid_sku_00017():
    assert is_valid_sku_00017("abc123")
    assert not is_valid_sku_00017("")


def test_bucket_by_tag_00017():
    p = Product_00017("s1", 100, ["a"])
    assert bucket_by_tag_00017([p]) == {"a": ["s1"]}
