"""Tests for catalog_00465."""

import pytest

from cartservice.generated.catalog_00465 import (
    Product_00465,
    bucket_by_tag_00465,
    is_valid_sku_00465,
    price_with_tax_00465,
)


def test_price_with_tax_00465():
    assert price_with_tax_00465(1000, 500) == 1050


def test_price_with_tax_negative_00465():
    with pytest.raises(ValueError):
        price_with_tax_00465(1000, -1)


def test_is_valid_sku_00465():
    assert is_valid_sku_00465("abc123")
    assert not is_valid_sku_00465("")


def test_bucket_by_tag_00465():
    p = Product_00465("s1", 100, ["a"])
    assert bucket_by_tag_00465([p]) == {"a": ["s1"]}
