"""Tests for catalog_00502."""

import pytest

from cartservice.generated.catalog_00502 import (
    Product_00502,
    bucket_by_tag_00502,
    is_valid_sku_00502,
    price_with_tax_00502,
)


def test_price_with_tax_00502():
    assert price_with_tax_00502(1000, 500) == 1050


def test_price_with_tax_negative_00502():
    with pytest.raises(ValueError):
        price_with_tax_00502(1000, -1)


def test_is_valid_sku_00502():
    assert is_valid_sku_00502("abc123")
    assert not is_valid_sku_00502("")


def test_bucket_by_tag_00502():
    p = Product_00502("s1", 100, ["a"])
    assert bucket_by_tag_00502([p]) == {"a": ["s1"]}
