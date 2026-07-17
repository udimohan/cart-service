"""Tests for catalog_00686."""

import pytest

from cartservice.generated.catalog_00686 import (
    Product_00686,
    bucket_by_tag_00686,
    is_valid_sku_00686,
    price_with_tax_00686,
)


def test_price_with_tax_00686():
    assert price_with_tax_00686(1000, 500) == 1050


def test_price_with_tax_negative_00686():
    with pytest.raises(ValueError):
        price_with_tax_00686(1000, -1)


def test_is_valid_sku_00686():
    assert is_valid_sku_00686("abc123")
    assert not is_valid_sku_00686("")


def test_bucket_by_tag_00686():
    p = Product_00686("s1", 100, ["a"])
    assert bucket_by_tag_00686([p]) == {"a": ["s1"]}
