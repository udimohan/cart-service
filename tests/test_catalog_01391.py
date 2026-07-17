"""Tests for catalog_01391."""

import pytest

from cartservice.generated.catalog_01391 import (
    Product_01391,
    bucket_by_tag_01391,
    is_valid_sku_01391,
    price_with_tax_01391,
)


def test_price_with_tax_01391():
    assert price_with_tax_01391(1000, 500) == 1050


def test_price_with_tax_negative_01391():
    with pytest.raises(ValueError):
        price_with_tax_01391(1000, -1)


def test_is_valid_sku_01391():
    assert is_valid_sku_01391("abc123")
    assert not is_valid_sku_01391("")


def test_bucket_by_tag_01391():
    p = Product_01391("s1", 100, ["a"])
    assert bucket_by_tag_01391([p]) == {"a": ["s1"]}
