"""Tests for catalog_01550."""

import pytest

from cartservice.generated.catalog_01550 import (
    Product_01550,
    bucket_by_tag_01550,
    is_valid_sku_01550,
    price_with_tax_01550,
)


def test_price_with_tax_01550():
    assert price_with_tax_01550(1000, 500) == 1050


def test_price_with_tax_negative_01550():
    with pytest.raises(ValueError):
        price_with_tax_01550(1000, -1)


def test_is_valid_sku_01550():
    assert is_valid_sku_01550("abc123")
    assert not is_valid_sku_01550("")


def test_bucket_by_tag_01550():
    p = Product_01550("s1", 100, ["a"])
    assert bucket_by_tag_01550([p]) == {"a": ["s1"]}
