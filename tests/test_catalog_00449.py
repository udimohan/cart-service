"""Tests for catalog_00449."""

import pytest

from cartservice.generated.catalog_00449 import (
    Product_00449,
    bucket_by_tag_00449,
    is_valid_sku_00449,
    price_with_tax_00449,
)


def test_price_with_tax_00449():
    assert price_with_tax_00449(1000, 500) == 1050


def test_price_with_tax_negative_00449():
    with pytest.raises(ValueError):
        price_with_tax_00449(1000, -1)


def test_is_valid_sku_00449():
    assert is_valid_sku_00449("abc123")
    assert not is_valid_sku_00449("")


def test_bucket_by_tag_00449():
    p = Product_00449("s1", 100, ["a"])
    assert bucket_by_tag_00449([p]) == {"a": ["s1"]}
