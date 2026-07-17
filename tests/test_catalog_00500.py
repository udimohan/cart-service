"""Tests for catalog_00500."""

import pytest

from cartservice.generated.catalog_00500 import (
    Product_00500,
    bucket_by_tag_00500,
    is_valid_sku_00500,
    price_with_tax_00500,
)


def test_price_with_tax_00500():
    assert price_with_tax_00500(1000, 500) == 1050


def test_price_with_tax_negative_00500():
    with pytest.raises(ValueError):
        price_with_tax_00500(1000, -1)


def test_is_valid_sku_00500():
    assert is_valid_sku_00500("abc123")
    assert not is_valid_sku_00500("")


def test_bucket_by_tag_00500():
    p = Product_00500("s1", 100, ["a"])
    assert bucket_by_tag_00500([p]) == {"a": ["s1"]}
