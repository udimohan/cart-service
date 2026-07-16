"""Tests for catalog_00899."""

import pytest

from cartservice.generated.catalog_00899 import (
    Product_00899,
    bucket_by_tag_00899,
    is_valid_sku_00899,
    price_with_tax_00899,
)


def test_price_with_tax_00899():
    assert price_with_tax_00899(1000, 500) == 1050


def test_price_with_tax_negative_00899():
    with pytest.raises(ValueError):
        price_with_tax_00899(1000, -1)


def test_is_valid_sku_00899():
    assert is_valid_sku_00899("abc123")
    assert not is_valid_sku_00899("")


def test_bucket_by_tag_00899():
    p = Product_00899("s1", 100, ["a"])
    assert bucket_by_tag_00899([p]) == {"a": ["s1"]}
