"""Tests for catalog_00307."""

import pytest

from cartservice.generated.catalog_00307 import (
    Product_00307,
    bucket_by_tag_00307,
    is_valid_sku_00307,
    price_with_tax_00307,
)


def test_price_with_tax_00307():
    assert price_with_tax_00307(1000, 500) == 1050


def test_price_with_tax_negative_00307():
    with pytest.raises(ValueError):
        price_with_tax_00307(1000, -1)


def test_is_valid_sku_00307():
    assert is_valid_sku_00307("abc123")
    assert not is_valid_sku_00307("")


def test_bucket_by_tag_00307():
    p = Product_00307("s1", 100, ["a"])
    assert bucket_by_tag_00307([p]) == {"a": ["s1"]}
