"""Tests for catalog_00736."""

import pytest

from cartservice.generated.catalog_00736 import (
    Product_00736,
    bucket_by_tag_00736,
    is_valid_sku_00736,
    price_with_tax_00736,
)


def test_price_with_tax_00736():
    assert price_with_tax_00736(1000, 500) == 1050


def test_price_with_tax_negative_00736():
    with pytest.raises(ValueError):
        price_with_tax_00736(1000, -1)


def test_is_valid_sku_00736():
    assert is_valid_sku_00736("abc123")
    assert not is_valid_sku_00736("")


def test_bucket_by_tag_00736():
    p = Product_00736("s1", 100, ["a"])
    assert bucket_by_tag_00736([p]) == {"a": ["s1"]}
