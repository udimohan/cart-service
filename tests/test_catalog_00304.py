"""Tests for catalog_00304."""

import pytest

from cartservice.generated.catalog_00304 import (
    Product_00304,
    bucket_by_tag_00304,
    is_valid_sku_00304,
    price_with_tax_00304,
)


def test_price_with_tax_00304():
    assert price_with_tax_00304(1000, 500) == 1050


def test_price_with_tax_negative_00304():
    with pytest.raises(ValueError):
        price_with_tax_00304(1000, -1)


def test_is_valid_sku_00304():
    assert is_valid_sku_00304("abc123")
    assert not is_valid_sku_00304("")


def test_bucket_by_tag_00304():
    p = Product_00304("s1", 100, ["a"])
    assert bucket_by_tag_00304([p]) == {"a": ["s1"]}
