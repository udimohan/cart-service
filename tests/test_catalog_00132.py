"""Tests for catalog_00132."""

import pytest

from cartservice.generated.catalog_00132 import (
    Product_00132,
    bucket_by_tag_00132,
    is_valid_sku_00132,
    price_with_tax_00132,
)


def test_price_with_tax_00132():
    assert price_with_tax_00132(1000, 500) == 1050


def test_price_with_tax_negative_00132():
    with pytest.raises(ValueError):
        price_with_tax_00132(1000, -1)


def test_is_valid_sku_00132():
    assert is_valid_sku_00132("abc123")
    assert not is_valid_sku_00132("")


def test_bucket_by_tag_00132():
    p = Product_00132("s1", 100, ["a"])
    assert bucket_by_tag_00132([p]) == {"a": ["s1"]}
