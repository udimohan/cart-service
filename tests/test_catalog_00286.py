"""Tests for catalog_00286."""

import pytest

from cartservice.generated.catalog_00286 import (
    Product_00286,
    bucket_by_tag_00286,
    is_valid_sku_00286,
    price_with_tax_00286,
)


def test_price_with_tax_00286():
    assert price_with_tax_00286(1000, 500) == 1050


def test_price_with_tax_negative_00286():
    with pytest.raises(ValueError):
        price_with_tax_00286(1000, -1)


def test_is_valid_sku_00286():
    assert is_valid_sku_00286("abc123")
    assert not is_valid_sku_00286("")


def test_bucket_by_tag_00286():
    p = Product_00286("s1", 100, ["a"])
    assert bucket_by_tag_00286([p]) == {"a": ["s1"]}
