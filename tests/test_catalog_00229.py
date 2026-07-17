"""Tests for catalog_00229."""

import pytest

from cartservice.generated.catalog_00229 import (
    Product_00229,
    bucket_by_tag_00229,
    is_valid_sku_00229,
    price_with_tax_00229,
)


def test_price_with_tax_00229():
    assert price_with_tax_00229(1000, 500) == 1050


def test_price_with_tax_negative_00229():
    with pytest.raises(ValueError):
        price_with_tax_00229(1000, -1)


def test_is_valid_sku_00229():
    assert is_valid_sku_00229("abc123")
    assert not is_valid_sku_00229("")


def test_bucket_by_tag_00229():
    p = Product_00229("s1", 100, ["a"])
    assert bucket_by_tag_00229([p]) == {"a": ["s1"]}
