"""Tests for catalog_00422."""

import pytest

from cartservice.generated.catalog_00422 import (
    Product_00422,
    bucket_by_tag_00422,
    is_valid_sku_00422,
    price_with_tax_00422,
)


def test_price_with_tax_00422():
    assert price_with_tax_00422(1000, 500) == 1050


def test_price_with_tax_negative_00422():
    with pytest.raises(ValueError):
        price_with_tax_00422(1000, -1)


def test_is_valid_sku_00422():
    assert is_valid_sku_00422("abc123")
    assert not is_valid_sku_00422("")


def test_bucket_by_tag_00422():
    p = Product_00422("s1", 100, ["a"])
    assert bucket_by_tag_00422([p]) == {"a": ["s1"]}
