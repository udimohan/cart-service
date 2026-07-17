"""Tests for catalog_00550."""

import pytest

from cartservice.generated.catalog_00550 import (
    Product_00550,
    bucket_by_tag_00550,
    is_valid_sku_00550,
    price_with_tax_00550,
)


def test_price_with_tax_00550():
    assert price_with_tax_00550(1000, 500) == 1050


def test_price_with_tax_negative_00550():
    with pytest.raises(ValueError):
        price_with_tax_00550(1000, -1)


def test_is_valid_sku_00550():
    assert is_valid_sku_00550("abc123")
    assert not is_valid_sku_00550("")


def test_bucket_by_tag_00550():
    p = Product_00550("s1", 100, ["a"])
    assert bucket_by_tag_00550([p]) == {"a": ["s1"]}
