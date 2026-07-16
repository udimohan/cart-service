"""Tests for catalog_00181."""

import pytest

from cartservice.generated.catalog_00181 import (
    Product_00181,
    bucket_by_tag_00181,
    is_valid_sku_00181,
    price_with_tax_00181,
)


def test_price_with_tax_00181():
    assert price_with_tax_00181(1000, 500) == 1050


def test_price_with_tax_negative_00181():
    with pytest.raises(ValueError):
        price_with_tax_00181(1000, -1)


def test_is_valid_sku_00181():
    assert is_valid_sku_00181("abc123")
    assert not is_valid_sku_00181("")


def test_bucket_by_tag_00181():
    p = Product_00181("s1", 100, ["a"])
    assert bucket_by_tag_00181([p]) == {"a": ["s1"]}
