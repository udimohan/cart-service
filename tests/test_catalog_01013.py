"""Tests for catalog_01013."""

import pytest

from cartservice.generated.catalog_01013 import (
    Product_01013,
    bucket_by_tag_01013,
    is_valid_sku_01013,
    price_with_tax_01013,
)


def test_price_with_tax_01013():
    assert price_with_tax_01013(1000, 500) == 1050


def test_price_with_tax_negative_01013():
    with pytest.raises(ValueError):
        price_with_tax_01013(1000, -1)


def test_is_valid_sku_01013():
    assert is_valid_sku_01013("abc123")
    assert not is_valid_sku_01013("")


def test_bucket_by_tag_01013():
    p = Product_01013("s1", 100, ["a"])
    assert bucket_by_tag_01013([p]) == {"a": ["s1"]}
