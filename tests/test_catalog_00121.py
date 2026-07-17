"""Tests for catalog_00121."""

import pytest

from cartservice.generated.catalog_00121 import (
    Product_00121,
    bucket_by_tag_00121,
    is_valid_sku_00121,
    price_with_tax_00121,
)


def test_price_with_tax_00121():
    assert price_with_tax_00121(1000, 500) == 1050


def test_price_with_tax_negative_00121():
    with pytest.raises(ValueError):
        price_with_tax_00121(1000, -1)


def test_is_valid_sku_00121():
    assert is_valid_sku_00121("abc123")
    assert not is_valid_sku_00121("")


def test_bucket_by_tag_00121():
    p = Product_00121("s1", 100, ["a"])
    assert bucket_by_tag_00121([p]) == {"a": ["s1"]}
