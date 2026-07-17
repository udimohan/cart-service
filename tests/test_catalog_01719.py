"""Tests for catalog_01719."""

import pytest

from cartservice.generated.catalog_01719 import (
    Product_01719,
    bucket_by_tag_01719,
    is_valid_sku_01719,
    price_with_tax_01719,
)


def test_price_with_tax_01719():
    assert price_with_tax_01719(1000, 500) == 1050


def test_price_with_tax_negative_01719():
    with pytest.raises(ValueError):
        price_with_tax_01719(1000, -1)


def test_is_valid_sku_01719():
    assert is_valid_sku_01719("abc123")
    assert not is_valid_sku_01719("")


def test_bucket_by_tag_01719():
    p = Product_01719("s1", 100, ["a"])
    assert bucket_by_tag_01719([p]) == {"a": ["s1"]}
