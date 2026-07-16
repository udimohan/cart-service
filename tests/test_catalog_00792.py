"""Tests for catalog_00792."""

import pytest

from cartservice.generated.catalog_00792 import (
    Product_00792,
    bucket_by_tag_00792,
    is_valid_sku_00792,
    price_with_tax_00792,
)


def test_price_with_tax_00792():
    assert price_with_tax_00792(1000, 500) == 1050


def test_price_with_tax_negative_00792():
    with pytest.raises(ValueError):
        price_with_tax_00792(1000, -1)


def test_is_valid_sku_00792():
    assert is_valid_sku_00792("abc123")
    assert not is_valid_sku_00792("")


def test_bucket_by_tag_00792():
    p = Product_00792("s1", 100, ["a"])
    assert bucket_by_tag_00792([p]) == {"a": ["s1"]}
