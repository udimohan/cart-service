"""Tests for catalog_00634."""

import pytest

from cartservice.generated.catalog_00634 import (
    Product_00634,
    bucket_by_tag_00634,
    is_valid_sku_00634,
    price_with_tax_00634,
)


def test_price_with_tax_00634():
    assert price_with_tax_00634(1000, 500) == 1050


def test_price_with_tax_negative_00634():
    with pytest.raises(ValueError):
        price_with_tax_00634(1000, -1)


def test_is_valid_sku_00634():
    assert is_valid_sku_00634("abc123")
    assert not is_valid_sku_00634("")


def test_bucket_by_tag_00634():
    p = Product_00634("s1", 100, ["a"])
    assert bucket_by_tag_00634([p]) == {"a": ["s1"]}
