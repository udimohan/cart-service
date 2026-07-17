"""Tests for catalog_00013."""

import pytest

from cartservice.generated.catalog_00013 import (
    Product_00013,
    bucket_by_tag_00013,
    is_valid_sku_00013,
    price_with_tax_00013,
)


def test_price_with_tax_00013():
    assert price_with_tax_00013(1000, 500) == 1050


def test_price_with_tax_negative_00013():
    with pytest.raises(ValueError):
        price_with_tax_00013(1000, -1)


def test_is_valid_sku_00013():
    assert is_valid_sku_00013("abc123")
    assert not is_valid_sku_00013("")


def test_bucket_by_tag_00013():
    p = Product_00013("s1", 100, ["a"])
    assert bucket_by_tag_00013([p]) == {"a": ["s1"]}
