"""Tests for catalog_01679."""

import pytest

from cartservice.generated.catalog_01679 import (
    Product_01679,
    bucket_by_tag_01679,
    is_valid_sku_01679,
    price_with_tax_01679,
)


def test_price_with_tax_01679():
    assert price_with_tax_01679(1000, 500) == 1050


def test_price_with_tax_negative_01679():
    with pytest.raises(ValueError):
        price_with_tax_01679(1000, -1)


def test_is_valid_sku_01679():
    assert is_valid_sku_01679("abc123")
    assert not is_valid_sku_01679("")


def test_bucket_by_tag_01679():
    p = Product_01679("s1", 100, ["a"])
    assert bucket_by_tag_01679([p]) == {"a": ["s1"]}
