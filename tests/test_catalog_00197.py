"""Tests for catalog_00197."""

import pytest

from cartservice.generated.catalog_00197 import (
    Product_00197,
    bucket_by_tag_00197,
    is_valid_sku_00197,
    price_with_tax_00197,
)


def test_price_with_tax_00197():
    assert price_with_tax_00197(1000, 500) == 1050


def test_price_with_tax_negative_00197():
    with pytest.raises(ValueError):
        price_with_tax_00197(1000, -1)


def test_is_valid_sku_00197():
    assert is_valid_sku_00197("abc123")
    assert not is_valid_sku_00197("")


def test_bucket_by_tag_00197():
    p = Product_00197("s1", 100, ["a"])
    assert bucket_by_tag_00197([p]) == {"a": ["s1"]}
