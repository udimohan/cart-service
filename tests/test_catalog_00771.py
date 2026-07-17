"""Tests for catalog_00771."""

import pytest

from cartservice.generated.catalog_00771 import (
    Product_00771,
    bucket_by_tag_00771,
    is_valid_sku_00771,
    price_with_tax_00771,
)


def test_price_with_tax_00771():
    assert price_with_tax_00771(1000, 500) == 1050


def test_price_with_tax_negative_00771():
    with pytest.raises(ValueError):
        price_with_tax_00771(1000, -1)


def test_is_valid_sku_00771():
    assert is_valid_sku_00771("abc123")
    assert not is_valid_sku_00771("")


def test_bucket_by_tag_00771():
    p = Product_00771("s1", 100, ["a"])
    assert bucket_by_tag_00771([p]) == {"a": ["s1"]}
