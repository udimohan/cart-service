"""Tests for catalog_00721."""

import pytest

from cartservice.generated.catalog_00721 import (
    Product_00721,
    bucket_by_tag_00721,
    is_valid_sku_00721,
    price_with_tax_00721,
)


def test_price_with_tax_00721():
    assert price_with_tax_00721(1000, 500) == 1050


def test_price_with_tax_negative_00721():
    with pytest.raises(ValueError):
        price_with_tax_00721(1000, -1)


def test_is_valid_sku_00721():
    assert is_valid_sku_00721("abc123")
    assert not is_valid_sku_00721("")


def test_bucket_by_tag_00721():
    p = Product_00721("s1", 100, ["a"])
    assert bucket_by_tag_00721([p]) == {"a": ["s1"]}
