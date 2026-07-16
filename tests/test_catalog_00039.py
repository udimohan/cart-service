"""Tests for catalog_00039."""

import pytest

from cartservice.generated.catalog_00039 import (
    Product_00039,
    bucket_by_tag_00039,
    is_valid_sku_00039,
    price_with_tax_00039,
)


def test_price_with_tax_00039():
    assert price_with_tax_00039(1000, 500) == 1050


def test_price_with_tax_negative_00039():
    with pytest.raises(ValueError):
        price_with_tax_00039(1000, -1)


def test_is_valid_sku_00039():
    assert is_valid_sku_00039("abc123")
    assert not is_valid_sku_00039("")


def test_bucket_by_tag_00039():
    p = Product_00039("s1", 100, ["a"])
    assert bucket_by_tag_00039([p]) == {"a": ["s1"]}
