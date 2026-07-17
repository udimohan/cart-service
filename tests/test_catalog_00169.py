"""Tests for catalog_00169."""

import pytest

from cartservice.generated.catalog_00169 import (
    Product_00169,
    bucket_by_tag_00169,
    is_valid_sku_00169,
    price_with_tax_00169,
)


def test_price_with_tax_00169():
    assert price_with_tax_00169(1000, 500) == 1050


def test_price_with_tax_negative_00169():
    with pytest.raises(ValueError):
        price_with_tax_00169(1000, -1)


def test_is_valid_sku_00169():
    assert is_valid_sku_00169("abc123")
    assert not is_valid_sku_00169("")


def test_bucket_by_tag_00169():
    p = Product_00169("s1", 100, ["a"])
    assert bucket_by_tag_00169([p]) == {"a": ["s1"]}
