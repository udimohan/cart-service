"""Tests for catalog_00679."""

import pytest

from cartservice.generated.catalog_00679 import (
    Product_00679,
    bucket_by_tag_00679,
    is_valid_sku_00679,
    price_with_tax_00679,
)


def test_price_with_tax_00679():
    assert price_with_tax_00679(1000, 500) == 1050


def test_price_with_tax_negative_00679():
    with pytest.raises(ValueError):
        price_with_tax_00679(1000, -1)


def test_is_valid_sku_00679():
    assert is_valid_sku_00679("abc123")
    assert not is_valid_sku_00679("")


def test_bucket_by_tag_00679():
    p = Product_00679("s1", 100, ["a"])
    assert bucket_by_tag_00679([p]) == {"a": ["s1"]}
