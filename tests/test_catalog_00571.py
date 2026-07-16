"""Tests for catalog_00571."""

import pytest

from cartservice.generated.catalog_00571 import (
    Product_00571,
    bucket_by_tag_00571,
    is_valid_sku_00571,
    price_with_tax_00571,
)


def test_price_with_tax_00571():
    assert price_with_tax_00571(1000, 500) == 1050


def test_price_with_tax_negative_00571():
    with pytest.raises(ValueError):
        price_with_tax_00571(1000, -1)


def test_is_valid_sku_00571():
    assert is_valid_sku_00571("abc123")
    assert not is_valid_sku_00571("")


def test_bucket_by_tag_00571():
    p = Product_00571("s1", 100, ["a"])
    assert bucket_by_tag_00571([p]) == {"a": ["s1"]}
