"""Tests for catalog_01169."""

import pytest

from cartservice.generated.catalog_01169 import (
    Product_01169,
    bucket_by_tag_01169,
    is_valid_sku_01169,
    price_with_tax_01169,
)


def test_price_with_tax_01169():
    assert price_with_tax_01169(1000, 500) == 1050


def test_price_with_tax_negative_01169():
    with pytest.raises(ValueError):
        price_with_tax_01169(1000, -1)


def test_is_valid_sku_01169():
    assert is_valid_sku_01169("abc123")
    assert not is_valid_sku_01169("")


def test_bucket_by_tag_01169():
    p = Product_01169("s1", 100, ["a"])
    assert bucket_by_tag_01169([p]) == {"a": ["s1"]}
