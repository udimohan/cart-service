"""Tests for catalog_01501."""

import pytest

from cartservice.generated.catalog_01501 import (
    Product_01501,
    bucket_by_tag_01501,
    is_valid_sku_01501,
    price_with_tax_01501,
)


def test_price_with_tax_01501():
    assert price_with_tax_01501(1000, 500) == 1050


def test_price_with_tax_negative_01501():
    with pytest.raises(ValueError):
        price_with_tax_01501(1000, -1)


def test_is_valid_sku_01501():
    assert is_valid_sku_01501("abc123")
    assert not is_valid_sku_01501("")


def test_bucket_by_tag_01501():
    p = Product_01501("s1", 100, ["a"])
    assert bucket_by_tag_01501([p]) == {"a": ["s1"]}
