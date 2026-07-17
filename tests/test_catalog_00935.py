"""Tests for catalog_00935."""

import pytest

from cartservice.generated.catalog_00935 import (
    Product_00935,
    bucket_by_tag_00935,
    is_valid_sku_00935,
    price_with_tax_00935,
)


def test_price_with_tax_00935():
    assert price_with_tax_00935(1000, 500) == 1050


def test_price_with_tax_negative_00935():
    with pytest.raises(ValueError):
        price_with_tax_00935(1000, -1)


def test_is_valid_sku_00935():
    assert is_valid_sku_00935("abc123")
    assert not is_valid_sku_00935("")


def test_bucket_by_tag_00935():
    p = Product_00935("s1", 100, ["a"])
    assert bucket_by_tag_00935([p]) == {"a": ["s1"]}
