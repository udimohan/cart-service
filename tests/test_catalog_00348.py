"""Tests for catalog_00348."""

import pytest

from cartservice.generated.catalog_00348 import (
    Product_00348,
    bucket_by_tag_00348,
    is_valid_sku_00348,
    price_with_tax_00348,
)


def test_price_with_tax_00348():
    assert price_with_tax_00348(1000, 500) == 1050


def test_price_with_tax_negative_00348():
    with pytest.raises(ValueError):
        price_with_tax_00348(1000, -1)


def test_is_valid_sku_00348():
    assert is_valid_sku_00348("abc123")
    assert not is_valid_sku_00348("")


def test_bucket_by_tag_00348():
    p = Product_00348("s1", 100, ["a"])
    assert bucket_by_tag_00348([p]) == {"a": ["s1"]}
