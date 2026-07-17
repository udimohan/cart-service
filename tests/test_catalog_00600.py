"""Tests for catalog_00600."""

import pytest

from cartservice.generated.catalog_00600 import (
    Product_00600,
    bucket_by_tag_00600,
    is_valid_sku_00600,
    price_with_tax_00600,
)


def test_price_with_tax_00600():
    assert price_with_tax_00600(1000, 500) == 1050


def test_price_with_tax_negative_00600():
    with pytest.raises(ValueError):
        price_with_tax_00600(1000, -1)


def test_is_valid_sku_00600():
    assert is_valid_sku_00600("abc123")
    assert not is_valid_sku_00600("")


def test_bucket_by_tag_00600():
    p = Product_00600("s1", 100, ["a"])
    assert bucket_by_tag_00600([p]) == {"a": ["s1"]}
