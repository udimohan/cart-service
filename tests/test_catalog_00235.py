"""Tests for catalog_00235."""

import pytest

from cartservice.generated.catalog_00235 import (
    Product_00235,
    bucket_by_tag_00235,
    is_valid_sku_00235,
    price_with_tax_00235,
)


def test_price_with_tax_00235():
    assert price_with_tax_00235(1000, 500) == 1050


def test_price_with_tax_negative_00235():
    with pytest.raises(ValueError):
        price_with_tax_00235(1000, -1)


def test_is_valid_sku_00235():
    assert is_valid_sku_00235("abc123")
    assert not is_valid_sku_00235("")


def test_bucket_by_tag_00235():
    p = Product_00235("s1", 100, ["a"])
    assert bucket_by_tag_00235([p]) == {"a": ["s1"]}
